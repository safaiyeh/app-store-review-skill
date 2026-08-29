---
name: app-store-review
description: Evaluates code against Apple's App Store Review Guidelines. Use this skill when reviewing iOS, macOS, tvOS, watchOS, or visionOS app code (Swift, Objective-C, React Native, or Expo) to identify potential App Store rejection issues before submission. Triggers on tasks involving app review preparation, compliance checking, or App Store submission readiness.
license: MIT
metadata:
  author: safaiyeh
  version: "1.3.0"
---

# App Store Review Guidelines Checker

Comprehensive guide for evaluating iOS, macOS, tvOS, watchOS, and visionOS app code against Apple's App Store Review Guidelines. This skill covers EVERY guideline point to identify potential rejection issues before submission.

**Supports:** Swift, Objective-C, React Native, and Expo apps

**Guidelines current through:** Apple's June 8, 2026 App Review Guidelines update (verified still current as of August 29, 2026). Also incorporates post-June policy announcements: social media age-rating questions (mandatory September 2026), Republic of Korea age rating changes (August/October 2026), and Brazil/EU alternative payment and distribution terms.

## When to Apply

Use this skill when:
- Preparing an app for App Store submission
- Reviewing code for compliance issues
- Implementing features that may trigger review concerns
- Auditing existing apps for guideline violations
- Building features involving payments, user data, or sensitive content

## Guideline Sections

Read individual rule files for detailed explanations, checklists, and code examples:

| Section | File | Key Topics |
|---------|------|------------|
| **1. Safety** | [rules/1-safety.md](rules/1-safety.md) | Objectionable content, UGC moderation, Kids Category, physical harm, data security |
| **2. Performance** | [rules/2-performance.md](rules/2-performance.md) | App completeness, metadata accuracy, hardware compatibility, software requirements |
| **3. Business** | [rules/3-business.md](rules/3-business.md) | In-app purchase, subscriptions, cryptocurrencies, other business models |
| **4. Design** | [rules/4-design.md](rules/4-design.md) | Copycats, minimum functionality, spam, extensions, Apple services, login |
| **5. Legal** | [rules/5-legal.md](rules/5-legal.md) | Privacy, data collection, intellectual property, gambling, VPN, MDM, developer code of conduct |

## Risk Levels by Category

| Risk Level | Category | Section | Common Rejection Reasons |
|------------|----------|---------|--------------------------|
| CRITICAL | Privacy & Data | 5.1 | Missing privacy policy, unauthorized data collection |
| CRITICAL | Payments | 3.1 | Bypassing in-app purchase, unclear pricing |
| HIGH | Safety | 1.x | Objectionable content, inadequate UGC moderation |
| HIGH | Performance | 2.x | Crashes, incomplete features, deprecated APIs |
| MEDIUM | Design | 4.x | Copycat apps, minimum functionality issues |
| MEDIUM | Legal | 5.x | IP violations, gambling without license |

---

## Quick Reference: High-Risk Rejection Patterns

### Critical Issues (Immediate Rejection)

**Swift:**
```swift
// 🔴 Private API usage
let selector = NSSelectorFromString("_privateMethod")

// 🔴 Hardcoded secrets
let apiKey = "sk_live_xxxxx"

// 🔴 External payment for digital goods
func purchaseDigitalContent() {
    openStripeCheckout() // Use StoreKit instead
}
```

**React Native / Expo:**
```typescript
// 🔴 Hardcoded secrets in JS bundle
const API_KEY = 'sk_live_xxxxx'; // REJECTION

// 🔴 External payment for digital goods
Linking.openURL('https://stripe.com/checkout'); // Use react-native-iap

// 🔴 Dynamic code execution
eval(downloadedCode); // REJECTION

// 🔴 Major feature changes via CodePush/expo-updates
// OTA updates for bug fixes only, not new features!
```

### High-Risk Issues

**Swift:**
```swift
// 🟡 Missing ATT when using ad SDKs
import FacebookAds // Without ATTrackingManager

// 🟡 Account creation without deletion
func createAccount() { } // But no deleteAccount()
```

**React Native / Expo:**
```typescript
// 🟡 Missing ATT (use expo-tracking-transparency)
import analytics from '@react-native-firebase/analytics';
analytics().logEvent('event'); // Without ATT prompt = REJECTION

// 🟡 Account deletion via website only
Linking.openURL('https://example.com/delete'); // Must be in-app!

// 🟡 Social login without a privacy-preserving alternative (4.8)
<GoogleSigninButton /> // Also offer a login meeting 4.8 criteria
                       // (Sign in with Apple is the simplest option)

// 🟡 Custom review prompts (5.6.1)
showCustomAlert('Rate us 5 stars!'); // Use StoreReview.requestReview()
```

### Medium-Risk Issues

```typescript
// 🟠 Vague purpose strings in Info.plist
"This app needs camera access" // Be specific!

// 🟠 WebView-only app (insufficient native functionality)
const App = () => <WebView source={{ uri: 'https://site.com' }} />;

// 🟠 References to Android in iOS app
const text = "Also available on Android"; // REJECTION

// 🟠 console.log in production
console.log('debug'); // Remove or wrap in __DEV__
```

---

## Pre-Submission Checklist

### Privacy (Section 5.1)
- [ ] Privacy policy link in App Store Connect
- [ ] Privacy policy link accessible within app
- [ ] All purpose strings are specific and accurate
- [ ] App Privacy details completed in App Store Connect
- [ ] ATT implemented if tracking users
- [ ] Account deletion available if accounts exist
- [ ] Data minimization - only requesting necessary permissions
- [ ] User consent obtained before data collection

### Payments (Section 3.1)
- [ ] StoreKit used for all digital purchases
- [ ] Restore purchases implemented
- [ ] Subscription terms clearly displayed
- [ ] Loot box odds disclosed if applicable
- [ ] No external payment for digital goods (unless entitled)
- [ ] Credits/currencies don't expire

### Safety (Section 1.x)
- [ ] No objectionable content
- [ ] UGC moderation implemented (filter, report, block, contact)
- [ ] UGC violations can be removed quickly and backed by a remediation plan
- [ ] Kids and teens receive age-appropriate experiences inside the app
- [ ] Parental gates for Kids Category apps
- [ ] No false information or prank features
- [ ] Medical disclaimers if applicable
- [ ] No substance promotion

### Performance (Section 2.x)
- [ ] Age rating questionnaire's social media capability questions answered (mandatory for submissions starting September 2026; apps with a social feed get a "Social Media" descriptor and Time Allowances category)
- [ ] No crashes or bugs
- [ ] Tested on both iPhone and iPad — App Review currently reviews on iPad Air 11-inch (M3) and iPhone 17 Pro Max (as of August 2026)
- [ ] All features complete and functional
- [ ] No placeholder content
- [ ] IPv6 tested and functional
- [ ] Demo account provided if needed
- [ ] Using only public APIs
- [ ] No deprecated APIs
- [ ] Proper background mode usage

### Design (Section 4.x)
- [ ] Sufficient native functionality (not just web wrapper)
- [ ] No copycat concerns
- [ ] Original app name and branding
- [ ] No duplicate Bundle ID spam or low-effort saturated-category clones
- [ ] Live Activities, push notifications, and Game Center are not used for spam, phishing, or unsolicited messages
- [ ] Extensions comply with guidelines
- [ ] Login alternatives if using social login
- [ ] Not monetizing built-in capabilities

### Legal (Section 5.x)
- [ ] No unlicensed third-party content
- [ ] Proper Apple trademark usage
- [ ] Gambling license if applicable (with real location-based geo-restriction)
- [ ] VPN uses NEVPNManager API
- [ ] COPPA/GDPR compliance for kids
- [ ] Review prompts use the system API only (no custom prompts)
- [ ] No review, chart, search, or referral manipulation (5.6)

---

## Reporting Skill Issues (Feedback)

This skill improves through user reports. If during a session you observe that this skill failed the user, offer — once per session — to report it to the maintainer.

**Offer feedback when you observe any of these.** Classify with the category name — it goes in the issue title as `[Feedback] <category>: <short description>`.

*Accuracy*
- **False positive** — the skill flagged code that is actually compliant (guidance too aggressive)
- **False negative** — the user's app was rejected for something the skill reviewed but didn't flag
- **Wrong citation** — a real issue, but attributed to the wrong guideline section or given the wrong risk level
- **Outdated** — a rule here contradicts Apple's current published guidelines

*Usefulness*
- **Too noisy** — a flood of low-value or duplicate findings drowned out the ones that mattered
- **Not actionable** — a finding lacked the detail, code reference, or concrete fix needed to act on it
- **Bad fix** — a suggested remediation was wrong, deprecated, didn't work, or would itself be rejected (including Swift vs React Native/Expo specifics)

*Coverage*
- **Missing rule** — a review scenario, API, or storefront-specific requirement (EU, Brazil, Korea, US, ...) the skill doesn't cover
- **Contradiction** — two parts of this skill disagree with each other

*Behavior*
- **Trigger/weight** — the skill activated when irrelevant, failed to activate when it should have, or consumed excessive context
- **Unclear** — the user found guidance confusing, ambiguous, or hard to apply

Softer signals count too: if the user repeatedly dismisses the same kind of finding, overrides the skill's advice and turns out to be right, or visibly works around a checklist item, that is feedback worth offering to file — micro-friction is as valuable as a wrong rule.

**Consent rules — all mandatory, no exceptions:**
1. **Ask first.** Say something like: "This looks like a gap in the app-store-review skill itself. Want me to draft a GitHub issue so the maintainer can fix it?" If the user declines, drop it for the rest of the session.
2. **Show the full draft** (exact title and body) before anything is sent.
3. **Never include the user's code, app name, bundle IDs, file paths, credentials, or proprietary details.** The report is about this skill's rules, not the user's app. Only include such details if the user explicitly writes them into the draft themselves.
4. **Send only after the user approves the exact text**, using `gh issue create --repo safaiyeh/app-store-review-skill --title "..." --body "..."`. If `gh` is unavailable or unauthenticated, give the user this link to file it themselves: https://github.com/safaiyeh/app-store-review-skill/issues/new?template=skill-feedback.yml
5. **Never send feedback silently, automatically, or as a side effect of another task.** A declined permission prompt means no — do not retry or find another route.

**Issue content:** skill version (from the frontmatter above), the feedback category, the rule section involved (e.g. "3.1.1"), what the skill said or did, what should have happened instead, and today's date. Nothing else unless the user adds it.

---

## References

- [App Store Review Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Apple Developer Program License Agreement](https://developer.apple.com/support/terms/apple-developer-program-license-agreement/)
- [June 8, 2026 App Review Guidelines update](https://developer.apple.com/news/?id=a233fmpw)
- [Age rating questionnaire: social media questions (July 2026)](https://developer.apple.com/news/?id=tlur8uvi)
- [Age rating updates for the Republic of Korea (August 2026)](https://developer.apple.com/news/?id=oj3r9pvw)
- [Changes for apps in the European Union (August 2026)](https://developer.apple.com/news/?id=gmws0jgp)
- [Changes to iOS in Brazil (June 2026)](https://developer.apple.com/news/?id=dhwadr2x)
- [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- [App Store Connect Help](https://developer.apple.com/help/app-store-connect/)
- [Apple Developer Documentation](https://developer.apple.com/documentation/)
