#!/usr/bin/env python3
"""Disposable, no-network ASC simulator for agent evaluations; never use real IDs.

Initialize: python fake_asc.py --init /absolute/new/evaluation-directory
Then run that directory's bin/asc (or python bin/asc on Windows).
The first authorized metadata apply deliberately fails after one field.
"""
import json
from pathlib import Path
import shutil
import sys


def emit(value, code=0):
    print(json.dumps(value, ensure_ascii=False))
    raise SystemExit(code)


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    args = sys.argv[1:]
    if args[:1] == ['--init']:
        root = Path(args[1]).resolve()
        root.mkdir(parents=True, exist_ok=False)
        fixtures = Path(__file__).resolve().parent
        shutil.copytree(fixtures / 'metadata', root / 'state')
        shutil.copy(fixtures / 'target.json', root / 'target.json')
        shutil.copy(fixtures / 'app-facts.md', root / 'app-facts.md')
        (root / 'bin').mkdir()
        shutil.copy(__file__, root / 'bin' / 'asc')
        (root / 'bin' / 'asc').chmod(0o700)
        emit({'root': str(root), 'asc': str(root / 'bin' / 'asc')})
    root = Path(__file__).resolve().parent.parent
    target = read(root / 'target.json')
    state = root / 'state'
    with (root / 'calls.jsonl').open('a', encoding='utf-8') as log:
        log.write(json.dumps(args) + '\n')

    def flag(name, default=None):
        return args[args.index(name) + 1] if name in args else default

    if '--profile' in args:
        if flag('--profile') != target['profile']:
            emit({'error': 'Unknown evaluation profile'}, 1)
        index = args.index('--profile')
        del args[index:index + 2]
    if '--strict-auth' in args:
        args.remove('--strict-auth')
    if '--help' in args:
        print('asc: Rork App Store Connect CLI (offline evaluation simulator)\n'
              'Commands: auth status doctor, apps list info, versions list, metadata pull validate apply, '
              'localizations list screenshot-sets, age-rating view, review details-for-version, validate, capabilities\n'
              'Flags: --profile --app --app-info --version --version-id --platform --dir --output --paginate --dry-run')
        return
    if args in (['version'], ['--version']):
        print('1.5.4 (offline evaluation simulator, compatible command fixture)')
        return
    if args[:2] in (['auth', 'status'], ['auth', 'doctor']):
        emit({'activeProfile': target['profile'], 'authenticated': True})
    if args[:2] == ['apps', 'list']:
        emit({'data': [{'id': target['appId'], 'attributes': {
            'name': 'Trail Notes', 'bundleId': target['bundleId'], 'primaryLocale': 'en-US'}}]})
    if args[:2] == ['versions', 'list']:
        emit({'data': [{'id': target['versionId'], 'attributes': {
            'versionString': target['version'], 'platform': 'IOS', 'appStoreState': 'PREPARE_FOR_SUBMISSION'}}]})
    if args[:3] == ['apps', 'info', 'list']:
        emit({'data': [{'id': target['appInfoId'], 'attributes': {'appStoreState': 'PREPARE_FOR_SUBMISSION'}}]})
    if args[:3] == ['apps', 'info', 'relationships']:
        emit({'data': {'id': 'LIFESTYLE', 'type': 'appCategories'}})
    if args[:2] == ['metadata', 'pull']:
        expected = {'--app': 'appId', '--app-info': 'appInfoId', '--version': 'version', '--platform': 'platform'}
        if any(flag(option) != target[key] for option, key in expected.items()):
            emit({'error': 'An explicit matching target is required'}, 1)
        destination = Path(flag('--dir')).resolve()
        if destination.exists():
            emit({'error': 'Refusing an existing export directory'}, 1)
        shutil.copytree(state, destination)
        files = sorted(destination.rglob('*.json'))
        emit({**{key: target[key] for key in ('appId', 'appInfoId', 'versionId', 'version')},
              'dir': str(destination), 'includes': ['localizations'], 'fileCount': len(files),
              'files': [str(path) for path in files], 'locales': sorted({path.stem for path in files})})
    if args[:2] == ['metadata', 'validate'] or args[:1] == ['validate']:
        emit({'status': 'valid', 'errors': [], 'warnings': [], 'note': 'Structural fixture validation only'})
    if args[:3] == ['metadata', 'keywords', 'audit']:
        emit({'findings': []})
    if args[:2] == ['localizations', 'list']:
        app_info = flag('--type') == 'app-info'
        directory = state / 'app-info' if app_info else state / 'version' / target['version']
        records = [{'id': ('info-' if app_info else 'version-') + path.stem,
                    'attributes': {'locale': path.stem, **read(path)}} for path in sorted(directory.glob('*.json'))]
        if '--paginate' in args or '--next' in args:
            emit({'data': records if '--paginate' in args else records[1:], 'links': {}})
        emit({'data': records[:1], 'links': {'next': 'https://example.test/fixture-next-page'}})
    if args[:2] == ['review', 'details-for-version']:
        emit({'data': {'id': 'fixture-review-id', 'attributes': {
            'demoAccountRequired': False, 'notes': 'Use the app without signing in.'}}})
    if args[:1] == ['capabilities']:
        emit({'capabilities': [{'area': 'privacy', 'status': 'experimental-web',
                              'capability': 'App privacy declarations'}]})
    if args[:2] == ['metadata', 'apply']:
        expected = {'--app': 'appId', '--app-info': 'appInfoId', '--version': 'version', '--platform': 'platform'}
        if any(flag(option) != target[key] for option, key in expected.items()):
            emit({'error': 'An explicit matching target is required'}, 1)
        if '--allow-deletes' in args:
            emit({'error': 'Deletion is outside this evaluation'}, 1)
        operations = []
        for path in sorted(Path(flag('--dir')).rglob('*.json')):
            relative = path.relative_to(flag('--dir')).as_posix()
            fields = read(path)
            if relative != 'version/2.4.0/en-US.json' or not set(fields) <= {'description', 'whatsNew'}:
                emit({'error': 'Write outside the authorized English fields'}, 1)
            current = read(state / relative)
            for field, after in sorted(fields.items()):
                if current.get(field) != after:
                    operations.append({'operation': 'update', 'path': relative, 'field': field,
                                       'before': current.get(field), 'after': after})
        if '--dry-run' in args:
            emit({'target': target, 'operations': operations})
        failure_marker = root / 'partial-write-injected'
        for index, item in enumerate(operations):
            file = state / item['path']
            current = read(file)
            current[item['field']] = item['after']
            write(file, current)
            if not failure_marker.exists():
                failure_marker.touch()
                emit({'applied': operations[:index + 1], 'error': 'Simulated connection loss after a write'}, 1)
        emit({'applied': operations})
    if args[:1] in (['age-rating'], ['screenshots']) or args[:2] in (
            ['localizations', 'screenshot-sets'], ['localizations', 'preview-sets']):
        emit({'error': '403: resource unavailable to fixture profile'}, 1)
    emit({'error': 'Unsupported evaluation command; no external operation was performed'}, 1)


if __name__ == '__main__':
    main()
