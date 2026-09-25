# Optional App Store Connect setup

Use this reference only for a connected metadata audit or remote fixes. A code review or review of supplied files can proceed without ASC, Python, an Apple account, or another skill pack.

## Detect and preserve existing setup

1. Check whether the host supports shell commands and, for visual review, image inspection. Without those capabilities, review supplied text/assets and state the limits. Do not install a different agent or silently change its configuration.
2. Locate `asc`, run `asc version` and `asc --help`, and identify the **Rork App-Store-Connect-CLI** (formerly under rudrankriyam). Other executables named `asc` are not interchangeable.
3. Inspect the needed command's `--help`. The reference recipes were checked against **1.5.4, commit a29ab94**. This is a tested command baseline, not a claim that every newer release is compatible. Check `metadata pull`, `metadata apply`, `metadata validate`, `validate`, and their target/output flags before using them. Optional command gaps should reduce coverage, not trigger unrelated upgrades.
4. Run `asc auth status --output json` without `--verbose`. If setup is broken, `asc auth doctor` diagnoses it; do not add `--fix` automatically. Avoid printing credential configuration files or `asc auth token`.
5. Preserve profiles, environment-based CI credentials, and repository-local configuration. Use `asc --profile PROFILE ...` for the chosen account instead of switching the global default. A profile may still obtain missing fields from environment variables; use supported `--strict-auth` when verifying an unambiguous credential source. Do not enumerate every stored account with network validation when only one is in scope.

Classify failures: a missing executable needs installation; unsupported flags need compatible recipes; 401 needs credential diagnosis; 403 means insufficient access, not missing app metadata; a timeout is a failed fetch. Repeated identical failures are a reason to report the gap and continue independently, not to reset credentials or escalate roles automatically.

## When the CLI is absent

Explain that connected review uses the optional CLI and offer local-file review as well. If installation is authorized, use the [upstream installation instructions](https://github.com/rorkai/App-Store-Connect-CLI#quick-start) for the user's OS and architecture. Homebrew currently offers:

```sh
brew install asc
asc version
asc --help
```

For other environments, use an upstream release/package appropriate to the platform and verify its published integrity information when available. Do not install Homebrew, run a remote shell installer, or replace an existing binary merely because it is convenient. An authorized setup task can proceed without requesting approval for every step.

No `asc init`, `asc docs init`, or `asc install-skills` is required. These create repository or global agent files. Use `--help` and the existing skill references instead; install upstream skills only if the user requests that integration.

## Authentication onboarding

Reuse existing credentials first. If missing, guide the user to [Apple's API key setup](https://developer.apple.com/help/app-store-connect/get-started/app-store-connect-api/). Request account access/key creation from the appropriate account owner when necessary. Prefer the least access that supports the task; do not assume every key has access to every resource. Apple team keys are role-based and apply across all apps in the account; individual keys follow the user's access.

Ask for a local `.p8` file path and the non-secret identifiers, not the private key's contents. With a team key, the verified baseline recipe is:

```sh
asc auth login --name PROFILE --key-id KEY_ID --issuer-id ISSUER_ID \
  --private-key /absolute/path/to/AuthKey.p8 --network
```

Current upstream also supports individual keys without an issuer ID, using `--key-type individual`. That flag is absent in the tested 1.5.4 binary: inspect `asc auth login --help` before offering it. Do not manufacture an issuer ID for an individual key. See [upstream authentication](https://github.com/rorkai/App-Store-Connect-CLI/blob/main/authentication.mdx).

Use the CLI's supported keychain storage on desktops or the user's existing protected CI credentials. Do not copy keys into the app repository, reports, shell history, or skill files. A host that cannot register credentials securely should leave that step to the user and continue with local evidence.

## Resolve one target

Use the bundle ID from the user's request or repository where unambiguous, then verify:

```sh
asc --profile PROFILE apps list --bundle-id BUNDLE_ID --paginate --output json
asc --profile PROFILE versions list --app APP_ID --platform IOS --paginate --output json
asc --profile PROFILE apps info list --app APP_ID --output json
```

Choose the intended platform/version and the app-info record matching its state. Ask only if context cannot resolve multiple accounts, apps, versions, or records. Do not choose the first record or automatically select a live version. Record profile, bundle ID, app ID, platform, version string, version ID, app-info ID, CLI version, and fetch time. Commands accepting `--version` are inconsistent: metadata pull/apply use a **version string**, while localization commands use a **version resource ID**.

Confirm field editability for the chosen state before preparing a remote operation. A locked field does not authorize creating a new version or changing submission state. Once resolved, use explicit targets in every connected command and proceed to [Metadata audit](metadata-audit.md).

## Local workspace

Use a private, task-specific directory outside the repository by default. On POSIX hosts, for example:

```sh
umask 077
AUDIT_DIR=$(mktemp -d "${TMPDIR:-/tmp}/app-store-review.XXXXXX")
```

Use the host's equivalent temporary-directory facility elsewhere. If the user wants artifacts in their repo, use a dedicated ignored directory and check its ignore status before storing data. This repository ignores `.app-store-review/`; that ignore rule does not automatically exist in the user's app repository.

Public text exports and redacted reports may be committed when requested. Raw review details can contain credentials and contact information: keep them private and redact before reporting. Record what was fetched without archiving unrelated account data.
