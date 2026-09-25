# App Store Review Guidelines Skill

An open-source agent skill for reviewing Apple-platform app code and App Store metadata against Apple's App Store Review Guidelines. Version 2 adds local and connected metadata audits, proposed text fixes, and verification of authorized App Store Connect changes.

**Supports:** Swift, Objective-C, **React Native**, and **Expo** apps; local metadata exports and screenshots; optional App Store Connect access through the Rork `asc` CLI.

**Current through:** Apple's official June 8, 2026 App Review Guidelines update

## Installation

### Codex

Add this repository as a Codex plugin marketplace:

```bash
codex plugin marketplace add safaiyeh/app-store-review-skill
```

Then open Codex, run `/plugins`, choose the App Store Review marketplace, and install the `app-store-review` plugin. Start a new thread and invoke the skill with `$app-store-review` or ask for an App Store compliance review.

Codex also discovers direct local skills from `~/.agents/skills`, but plugins are the recommended distribution path for reusable skills.

### Claude Code Plugin Marketplace

```bash
/plugin marketplace add safaiyeh/app-store-review-skill
/plugin install app-store-review@app-store-review
```

### skills.sh

```bash
npx skills add safaiyeh/app-store-review-skill
```

## Setup

Install the skill in your existing agent using one of the methods above. Code reviews and audits of supplied metadata need no Apple credentials or ASC installation. A connected audit uses your own App Store Connect access; the skill guides setup only when needed.

| Workflow | Requirements |
|---|---|
| Code review | App source and an agent that can read it |
| Local metadata audit | Supplied text/export; image inspection for screenshot review |
| Connected metadata audit | Shell access, compatible [Rork asc CLI](https://github.com/rorkai/App-Store-Connect-CLI), and access to the chosen app |
| Prepare/apply text fixes | Agent file tools; compatible ASC CLI and app access for connected writes |

The command recipes were checked against ASC **1.5.4 (a29ab94)**. The agent checks installed command help rather than assuming every version uses the same flags, and preserves the actual export layout. Other executables named `asc` are not interchangeable. See [setup and compatibility](references/asc-setup.md).

Your local agent runs `asc` directly and uses its existing tools to inspect and edit files. The skill has no runtime scripts or Python dependency. No additional agent runtime, MCP server, ASC skill pack, or global configuration change is required. Onboarding preserves existing authentication profiles. Keys stay in your supported credential storage, outside reports and repositories.

### Supported AI Agents

This skill works with Codex and AI coding agents that support the skills.sh standard:

- [Codex](https://openai.com/codex/)
- [Claude Code](https://claude.ai/code)
- [Cursor](https://cursor.sh)
- [Windsurf](https://codeium.com/windsurf)
- And other compatible agents

### How It Works

1. **Ask for a code, local metadata, or connected review.** The agent loads the relevant workflow and rule files.
2. **Collect scoped evidence.** Connected reviews resolve the account, app, platform, version, and locales before fetching metadata.
3. **Review findings and coverage.** Confirmed issues, items needing verification, optional improvements, and unavailable evidence are distinguished.
4. **Prepare fixes when requested.** Text changes are proposed locally with before/after diffs and a CLI dry-run.
5. **Apply within your authorization and verify.** Refresh current state, stage only changed fields, apply the reviewed changes, and fetch the result. Submission and release remain separate actions.

The main text workflow handles nonempty field updates to existing localizations. Locale creation/deletion, clearing fields, screenshot replacement, category/age declarations, and privacy-label edits have separate guidance. The agent uses verified app facts and respects submission-state limits. See [audit workflow](references/metadata-audit.md) and [fix workflow](references/metadata-fixes.md).

### Example Prompts

```
"Review this app for App Store compliance"
"Check if my IAP implementation follows Apple's guidelines"
"Audit the privacy and data collection in this React Native app"
"What App Store issues might block my submission?"
"Audit this local metadata export and screenshots without connecting to Apple."
"Audit the iOS 2.4.0 metadata for my app in ASC. Do not change anything."
"Prepare fixes for these metadata findings and show the exact changes."
"Apply the agreed English description changes and verify them in ASC."
```

### Telemetry

The skills CLI collects anonymous usage telemetry. To opt out:

```bash
SKILLS_NO_TELEMETRY=1 npx skills add safaiyeh/app-store-review-skill
```

**This skill collects no telemetry.** Optional connected workflows have your agent invoke ASC to access Apple. Agents may also fetch public rules, support pages, privacy policies, or media when the task calls for them. Third-party CLI/agent behavior is governed by those tools. Working exports and reviewer details stay in a private task directory by default; public reports omit credentials and unrelated account information.

### Feedback

All feedback is welcome, big or small: false positives, findings the skill missed, guidance that was too aggressive, too noisy, too vague, or outdated, wrong section citations, bad suggested fixes, missing coverage, or the skill triggering when it shouldn't. If anything felt off — especially if your app was rejected despite following the skill — please [file a feedback issue](https://github.com/safaiyeh/app-store-review-skill/issues/new?template=skill-feedback.yml).

The skill also instructs your AI agent to *offer* to draft such an issue when it notices the skill failed you. This is strictly consent-based: the agent must ask first, show you the exact issue text, and only submit with your approval (via `gh`, which you can also deny at the permission prompt). It never sends anything automatically, and drafts never include your code or app details.

## Structure

```
app-store-review-skill/
├── .agents/
│   └── plugins/marketplace.json # Codex plugin marketplace
├── .claude-plugin/
│   ├── marketplace.json        # Claude Code plugin marketplace
│   └── plugin.json             # Claude Code plugin manifest
├── .codex-plugin/
│   └── plugin.json              # Codex plugin manifest
├── agents/
│   └── openai.yaml             # Codex UI metadata
├── SKILL.md                    # Workflow routing, quick reference & checklist
├── references/
│   ├── asc-setup.md            # Optional installation, auth, target selection
│   ├── metadata-audit.md       # Collection, evidence, coverage, findings
│   └── metadata-fixes.md       # Proposals, dry-run, writes, recovery
├── tests/                     # Maintainer-only fixtures and agent evaluations
├── release-notes/             # Prepared release notes
└── rules/
    ├── 1-safety.md             # Section 1: Safety guidelines
    ├── 2-performance.md        # Section 2: Performance guidelines
    ├── 3-business.md           # Section 3: Business guidelines
    ├── 4-design.md             # Section 4: Design guidelines
    └── 5-legal.md              # Section 5: Legal guidelines
```

## Coverage

This skill covers **ALL 5 major sections** with **EVERY guideline point**:

### [1. Safety](rules/1-safety.md)
- 1.1 Objectionable Content (1.1.1-1.1.7)
- 1.2 User-Generated Content & Creator Content
- 1.3 Kids Category (parental gates, privacy, analytics)
- 1.4 Physical Harm (medical apps, drug dosage, substances)
- 1.5 Developer Information
- 1.6 Data Security
- 1.7 Reporting Criminal Activity

### [2. Performance](rules/2-performance.md)
- 2.1 App Completeness (final versions, IAP)
- 2.2 Beta Testing
- 2.3 Accurate Metadata (2.3.1-2.3.13)
- 2.4 Hardware Compatibility (2.4.1-2.4.5)
- 2.5 Software Requirements (2.5.1-2.5.18)

### [3. Business](rules/3-business.md)
- 3.1 Payments (IAP, subscriptions, external links, crypto)
- 3.1.1-3.1.5 In-App Purchase rules
- 3.2 Other Business Models (acceptable/unacceptable)

### [4. Design](rules/4-design.md)
- 4.1 Copycats
- 4.2 Minimum Functionality
- 4.3 Spam
- 4.4 Extensions (keyboard, Safari)
- 4.5 Apple Sites and Services
- 4.7 Mini Apps, Chatbots, Game Emulators
- 4.8 Login Services
- 4.9 Apple Pay
- 4.10 Monetizing Built-In Capabilities

### [5. Legal](rules/5-legal.md)
- 5.1 Privacy (data collection, use, sharing, health, kids, location)
- 5.2 Intellectual Property
- 5.3 Gaming, Gambling, Lotteries
- 5.4 VPN Apps
- 5.5 Mobile Device Management
- 5.6 Developer Code of Conduct (reviews, developer identity, discovery fraud, app quality)

## Features

- **Modular structure** - Agent loads only relevant sections
- **2000+ lines** of comprehensive guidelines
- **Checklists** for every guideline point
- **Code patterns** for Swift AND React Native/Expo
- **Package references** for both Expo and bare React Native
- **Quick reference** for high-risk rejection patterns
- **Pre-submission checklist** in main SKILL.md
- **Metadata reviews** from local exports or a selected App Store Connect version
- **Evidence and coverage reporting** with field/locale references
- **Narrow text updates** with target checks, drift detection, partial-result recovery, and read-back verification

## React Native / Expo Support

Each rule file includes:
- TypeScript/JavaScript code patterns to flag
- Expo package recommendations (preferred)
- Bare React Native package alternatives
- React Native-specific checklists

Key packages covered:
- `react-native-purchases` (RevenueCat — recommended for IAP) / `react-native-iap`
- `expo-tracking-transparency` / `react-native-tracking-transparency`
- `expo-secure-store` / `react-native-keychain`
- `expo-apple-authentication` / `@invertase/react-native-apple-authentication`
- `expo-local-authentication` / `react-native-biometrics`

## What It Checks

### Critical Issues (Immediate Rejection)
- Private API usage
- Hardcoded secrets/credentials
- External payment for digital goods
- On-device cryptocurrency mining
- Dynamic code execution

### High-Risk Issues
- Missing App Tracking Transparency
- Account creation without deletion
- IAP without restore purchases
- UGC without moderation
- UGC without removal workflows or a compliance improvement plan
- Kids apps without parental gates
- Live Activities or push notifications used for spam, phishing, or unsolicited messages

### Medium-Risk Issues
- Vague purpose strings
- Over-requesting permissions
- Unjustified background modes
- References to other platforms
- Custom review prompts instead of the system API

## When It Triggers

The skill activates when working on:
- App Store submission preparation
- Metadata and screenshot audits, including offline exports
- Preparing and applying authorized metadata fixes
- Code compliance review
- Payment/StoreKit implementation
- Privacy and data handling
- User-generated content features
- Kids Category apps
- Health/medical apps
- VPN/MDM apps
- Gambling/lottery apps

## Development and validation

Maintainers can run packaging and evaluation-harness tests with Python 3.10+ and its standard library. Python is a development dependency only; skill users need neither Python nor this test harness. No Apple account is required:

```sh
python3 -m unittest discover -s tests -v
```

With the compatible ASC CLI installed, also exercise its offline metadata validator:

```sh
ASC_OFFLINE_TESTS=1 python3 -m unittest discover -s tests -v
```

The optional check does not authenticate or access a real app. CI runs the offline suite on Linux, macOS, and Windows with Python 3.10 and 3.13. [Behavioral scenarios](tests/scenarios/README.md) cover fresh setup, audit-only execution, partial access, ambiguous targets, source disagreements, and recovery. These evaluate an agent following the skill through a simulated CLI. Passing packaging and harness tests alone does not establish correct agent behavior.

Keep policy guidance in `rules/`, workflow instructions in `references/`, and real secrets/customer artifacts out of fixtures. Change command recipes only with help/source verification and update the tested compatibility notes. [v2.0.0 release notes](release-notes/v2.0.0.md) describe the new workflows and migration.

## License

MIT
