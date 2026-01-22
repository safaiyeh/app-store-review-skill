---
name: legal
description: App Store Review Guidelines Section 5 - Legal (privacy, data collection, intellectual property, gambling, VPN, MDM)
---

# 5. LEGAL

## 5.1 Privacy

### 5.1.1 Data Collection and Storage

#### (i) Privacy Policies

**MUST include privacy policy link in:**
- [ ] App Store Connect metadata
- [ ] Within app (easily accessible)

**Privacy policy MUST:**
- [ ] Identify what data is collected
- [ ] Identify how data is collected
- [ ] Identify all uses of data
- [ ] Confirm third parties provide equal protection
- [ ] Explain data retention/deletion policies
- [ ] Describe how user can revoke consent and request deletion

#### (ii) Permission
- [ ] Secure user consent for data collection (even anonymous data)
- [ ] Paid functionality must NOT depend on granting data access
- [ ] Provide easy way to withdraw consent
- [ ] Purpose strings must clearly describe data use
- [ ] GDPR compliance if relying on legitimate interest

### Permission Usage Description Checklist

> **CRITICAL:** Apple reviewers will reject apps with missing or vague permission usage descriptions. Every permission your app requests MUST have a clear, specific description explaining WHY and HOW the data is used.

**Before submission, verify:**
- [ ] All required permission keys are present in Info.plist
- [ ] Each description explains the specific feature that uses the permission
- [ ] Descriptions are user-friendly (not technical jargon)
- [ ] Descriptions match actual app functionality
- [ ] No generic phrases like "for app functionality" or "required for this app"

### Complete Info.plist Permission Reference

**Info.plist purpose strings (Swift & React Native):**
```xml
<!-- REQUIRED: Clear purpose strings in Info.plist -->
<!-- These apply to BOTH native Swift AND React Native apps -->

<!-- CAMERA -->
<key>NSCameraUsageDescription</key>
<string>Camera is used to scan product barcodes for price comparison</string>

<!-- PHOTO LIBRARY -->
<key>NSPhotoLibraryUsageDescription</key>
<string>Photo access allows you to upload images for your profile</string>

<key>NSPhotoLibraryAddUsageDescription</key>
<string>Save edited photos to your photo library</string>

<!-- LOCATION -->
<key>NSLocationWhenInUseUsageDescription</key>
<string>Your location helps find nearby stores with the products you're looking for</string>

<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>Background location is used to notify you when you're near a saved store</string>

<key>NSLocationAlwaysUsageDescription</key>
<string>Background location tracks your running route even when the app is closed</string>

<!-- MICROPHONE -->
<key>NSMicrophoneUsageDescription</key>
<string>Microphone is used for voice search and video calls with support</string>

<!-- CONTACTS -->
<key>NSContactsUsageDescription</key>
<string>Contacts help you find friends already using the app</string>

<!-- CALENDARS -->
<key>NSCalendarsUsageDescription</key>
<string>Calendar access lets you add event reminders directly to your calendar</string>

<key>NSCalendarsWriteOnlyAccessUsageDescription</key>
<string>Add workout sessions to your calendar</string>

<!-- REMINDERS -->
<key>NSRemindersUsageDescription</key>
<string>Create reminders for tasks you save in the app</string>

<!-- BLUETOOTH -->
<key>NSBluetoothAlwaysUsageDescription</key>
<string>Bluetooth connects to your fitness tracker to sync workout data</string>

<key>NSBluetoothPeripheralUsageDescription</key>
<string>Connect to Bluetooth devices for data transfer</string>

<!-- HEALTH -->
<key>NSHealthShareUsageDescription</key>
<string>Read your step count and workout data to track fitness goals</string>

<key>NSHealthUpdateUsageDescription</key>
<string>Save workout sessions and calories burned to Apple Health</string>

<!-- MOTION -->
<key>NSMotionUsageDescription</key>
<string>Motion data is used to count your steps and track physical activity</string>

<!-- FACE ID -->
<key>NSFaceIDUsageDescription</key>
<string>Use Face ID to securely unlock the app and authorize payments</string>

<!-- SPEECH RECOGNITION -->
<key>NSSpeechRecognitionUsageDescription</key>
<string>Voice commands let you navigate the app hands-free</string>

<!-- SIRI -->
<key>NSSiriUsageDescription</key>
<string>Add Siri shortcuts to quickly start your favorite workout</string>

<!-- TRACKING -->
<key>NSUserTrackingUsageDescription</key>
<string>This identifier will be used to deliver personalized ads to you</string>

<!-- APPLE MUSIC -->
<key>NSAppleMusicUsageDescription</key>
<string>Access your Apple Music library to play songs during workouts</string>

<!-- HOME -->
<key>NSHomeKitUsageDescription</key>
<string>Control your smart home devices directly from the app</string>

<!-- LOCAL NETWORK -->
<key>NSLocalNetworkUsageDescription</key>
<string>Discover and connect to devices on your local network for casting</string>

<!-- NEARBY INTERACTION -->
<key>NSNearbyInteractionUsageDescription</key>
<string>Find the precise location of your connected devices</string>
```

### Good vs Bad Purpose Strings

| Permission | ❌ BAD (Rejection Risk) | ✅ GOOD |
|------------|------------------------|---------|
| Camera | "Camera access needed" | "Take photos to attach to your support tickets" |
| Camera | "For app functionality" | "Scan QR codes to quickly add friends" |
| Photo Library | "Access photos" | "Choose photos from your library to create a collage" |
| Location | "Location required" | "Find coffee shops within 2 miles of your current location" |
| Location | "We need your location" | "Show your position on the delivery tracking map" |
| Microphone | "Microphone permission" | "Record voice memos to attach to your notes" |
| Contacts | "To access contacts" | "Find friends who are already using the app" |
| Bluetooth | "Bluetooth needed" | "Connect to your heart rate monitor during workouts" |
| Health | "Health data access" | "Read your daily step count to track progress toward your goal" |
| Tracking | "For a better experience" | "This identifier will be used to deliver personalized ads" |

### Common Rejection Reasons for Permissions

**Location Permission Rejections:**
```xml
<!-- ❌ REJECTION: Vague description -->
<key>NSLocationWhenInUseUsageDescription</key>
<string>This app requires location access</string>

<!-- ❌ REJECTION: No explanation of benefit to user -->
<key>NSLocationWhenInUseUsageDescription</key>
<string>Location is used by this app</string>

<!-- ❌ REJECTION: Over-requesting (Always when WhenInUse is sufficient) -->
<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>For location features</string>

<!-- ✅ GOOD: Specific, user-beneficial -->
<key>NSLocationWhenInUseUsageDescription</key>
<string>Your location is used to show nearby restaurants and calculate delivery times to your address</string>
```

**Camera/Photo Library Rejections:**
```xml
<!-- ❌ REJECTION: Missing description entirely when using camera -->
<!-- If you use react-native-image-picker or expo-image-picker, you NEED these! -->

<!-- ❌ REJECTION: Generic description -->
<key>NSCameraUsageDescription</key>
<string>Camera access is required</string>

<!-- ✅ GOOD: Explains exactly what user does with camera -->
<key>NSCameraUsageDescription</key>
<string>Take photos of receipts to submit expense reports</string>
<key>NSPhotoLibraryUsageDescription</key>
<string>Select existing photos of receipts from your library</string>
```

**React Native - Edit ios/[AppName]/Info.plist:**
```typescript
// React Native apps must configure purpose strings in:
// ios/[AppName]/Info.plist

// Common packages requiring purpose strings:
// react-native-camera → NSCameraUsageDescription
// react-native-vision-camera → NSCameraUsageDescription, NSMicrophoneUsageDescription
// react-native-image-picker → NSPhotoLibraryUsageDescription, NSCameraUsageDescription
// @react-native-community/geolocation → NSLocationWhenInUseUsageDescription
// react-native-geolocation-service → NSLocationWhenInUseUsageDescription
// expo-location → NSLocationWhenInUseUsageDescription
// react-native-contacts → NSContactsUsageDescription
// react-native-permissions → Various depending on permissions requested
// react-native-health → NSHealthShareUsageDescription, NSHealthUpdateUsageDescription
// react-native-ble-plx → NSBluetoothAlwaysUsageDescription
// react-native-touch-id → NSFaceIDUsageDescription

// ✅ GOOD: Specific, clear purpose strings
const INFO_PLIST_STRINGS = {
  NSCameraUsageDescription:
    "Camera is used to scan QR codes for quick login",
  NSPhotoLibraryUsageDescription:
    "Photo library access lets you choose a profile picture",
  NSLocationWhenInUseUsageDescription:
    "Location is used to show restaurants within 5 miles of you",
};

// ❌ BAD: Vague purpose strings
const BAD_STRINGS = {
  NSCameraUsageDescription: "Camera access needed", // REJECTION
  NSPhotoLibraryUsageDescription: "For app features", // REJECTION
  NSLocationWhenInUseUsageDescription: "Location required", // REJECTION
};
```

**Swift - Verify Info.plist permissions match code usage:**
```swift
// IMPORTANT: Only request permissions you actually use
// Apple WILL reject if you request permissions without corresponding features

import AVFoundation
import Photos
import CoreLocation
import Contacts

class PermissionManager {
    // ✅ GOOD: Only request what you need, when you need it
    func requestCameraIfNeeded() {
        // Only call this when user taps "Take Photo"
        AVCaptureDevice.requestAccess(for: .video) { granted in
            // Handle permission result
        }
    }

    // ❌ BAD: Requesting all permissions at app launch
    func requestAllPermissionsAtLaunch() {
        // Don't do this - Apple will reject
        // Request permissions contextually when the feature is used
    }
}
```

**Expo - app.json/app.config.js permissions:**
```javascript
// expo app.json - Configure iOS permissions
{
  "expo": {
    "ios": {
      "infoPlist": {
        "NSCameraUsageDescription": "Take photos to share in your posts",
        "NSPhotoLibraryUsageDescription": "Choose photos from your library to share",
        "NSLocationWhenInUseUsageDescription": "Show your location on the event map",
        "NSMicrophoneUsageDescription": "Record audio for video messages",
        "NSContactsUsageDescription": "Find friends who use the app",
        "NSFaceIDUsageDescription": "Use Face ID to securely log in"
      }
    }
  }
}

// Expo plugins that automatically add permission keys:
// expo-camera → NSCameraUsageDescription, NSMicrophoneUsageDescription
// expo-image-picker → NSCameraUsageDescription, NSPhotoLibraryUsageDescription
// expo-location → NSLocationWhenInUseUsageDescription
// expo-contacts → NSContactsUsageDescription
// expo-calendar → NSCalendarsUsageDescription
// expo-local-authentication → NSFaceIDUsageDescription
```

#### (iii) Data Minimization
- [ ] Only request access to data relevant to core functionality
- [ ] Only collect data required for the task
- [ ] Use out-of-process picker/share sheet when possible instead of full access

#### (iv) Access
- [ ] Respect user permission settings
- [ ] Do NOT manipulate, trick, or force consent
- [ ] Provide alternatives for users who don't consent

#### (v) Account Sign-In
- [ ] Let users use app without login if no significant account-based features
- [ ] If app supports account creation, MUST offer account deletion within app
- [ ] Do NOT require personal info unless directly relevant to core functionality
- [ ] If not related to social network, provide access without social login
- [ ] Must include mechanism to revoke social network credentials
- [ ] May not store social credentials off device

**Swift implementation:**
```swift
// REQUIRED: Account deletion
func deleteAccount() async throws {
    // Must actually delete user data, not just deactivate
    try await api.deleteUserData(userId: currentUser.id)
    try await api.deleteUserAccount(userId: currentUser.id)
    clearLocalData()
    signOut()
}

// REQUIRED: Accessible from within app
class SettingsViewController {
    @IBAction func deleteAccountTapped() {
        presentDeleteAccountConfirmation()
    }
}
```

**React Native implementation:**
```typescript
// REQUIRED: Account deletion must be accessible in-app
// Cannot just link to website - must be actionable within app

const deleteAccount = async () => {
  // Show confirmation
  Alert.alert(
    'Delete Account',
    'This will permanently delete your account and all data. This cannot be undone.',
    [
      { text: 'Cancel', style: 'cancel' },
      {
        text: 'Delete',
        style: 'destructive',
        onPress: async () => {
          try {
            // Must actually delete, not just deactivate!
            await api.delete('/user/account');

            // Clear local data
            await AsyncStorage.clear();
            await Keychain.resetGenericPassword();

            // Sign out and redirect
            signOut();
            navigation.reset({ routes: [{ name: 'Login' }] });
          } catch (error) {
            Alert.alert('Error', 'Failed to delete account');
          }
        },
      },
    ]
  );
};

// REQUIRED: Accessible from Settings screen
const SettingsScreen = () => (
  <ScrollView>
    {/* Other settings */}
    <Button
      title="Delete Account"
      color="red"
      onPress={deleteAccount}
    />
  </ScrollView>
);

// ❌ BAD: Linking to website for deletion
const badDeleteAccount = () => {
  Linking.openURL('https://example.com/delete-account'); // NOT SUFFICIENT
};
```

#### (vi) Surreptitious Data Collection
- [ ] Apps surreptitiously discovering passwords or private data will be REMOVED from Developer Program

#### (vii) SafariViewController
- [ ] Must be used to visibly present information
- [ ] May NOT be hidden or obscured
- [ ] May NOT track users without knowledge and consent

#### (viii) Unauthorized Personal Information Compilation
- [ ] Apps compiling personal info from sources not directly from user (including public databases) without explicit consent NOT permitted

#### (ix) Highly Regulated Fields
- [ ] Apps in banking, financial services, healthcare, gambling, legal cannabis, air travel, crypto exchanges should be from legal entity, not individual developer
- [ ] Cannabis apps must be geo-restricted to legal jurisdictions

#### (x) Basic Contact Information
- [ ] Request for name/email must be optional
- [ ] Features/services must NOT be conditional on providing this info

### 5.1.2 Data Use and Sharing

#### (i) Explicit Permission
- [ ] Cannot use, transmit, or share personal data without permission
- [ ] Must provide access to info about how/where data is used
- [ ] Must clearly disclose third-party sharing (including third-party AI)
- [ ] Must obtain explicit permission before sharing
- [ ] Data may only be shared to improve app or serve advertising
- [ ] Must use App Tracking Transparency APIs for cross-app tracking
- [ ] May NOT require system functionalities (push, location, tracking) for functionality or compensation
- [ ] Unauthorized data sharing may result in removal from sale and Developer Program

**Swift implementation:**
```swift
// REQUIRED: App Tracking Transparency
import AppTrackingTransparency

func requestTrackingAuthorization() {
    ATTrackingManager.requestTrackingAuthorization { status in
        switch status {
        case .authorized:
            // May track
            enableTracking()
        case .denied, .restricted, .notDetermined:
            // May NOT track
            disableTracking()
        @unknown default:
            disableTracking()
        }
    }
}
```

**React Native implementation (react-native-tracking-transparency):**
```typescript
// REQUIRED: App Tracking Transparency for iOS 14.5+
import {
  requestTrackingPermission,
  getTrackingStatus,
} from 'react-native-tracking-transparency';

// Request on app startup or before showing ads
const requestTracking = async () => {
  const status = await requestTrackingPermission();

  switch (status) {
    case 'authorized':
      // User allowed tracking
      enableTracking();
      initializeAdSDKs();
      break;
    case 'denied':
    case 'restricted':
    case 'not-determined':
      // User denied or hasn't decided - NO TRACKING
      disableTracking();
      initializeAdSDKsWithoutTracking();
      break;
  }
};

// Check status before any tracking
const checkTrackingStatus = async () => {
  const status = await getTrackingStatus();
  return status === 'authorized';
};

// ❌ BAD: Tracking without ATT prompt
import analytics from '@react-native-firebase/analytics';
analytics().setUserId(userId); // Without ATT permission = REJECTION

// ✅ GOOD: Check ATT before tracking
const trackUser = async (userId: string) => {
  const canTrack = await checkTrackingStatus();
  if (canTrack) {
    analytics().setUserId(userId);
  }
};

// Also required: Add to Info.plist
// <key>NSUserTrackingUsageDescription</key>
// <string>This identifier will be used to deliver personalized ads</string>
```

#### (ii) Purpose Limitation
- [ ] Data collected for one purpose may NOT be repurposed without consent

#### (iii) User Profile Building Restrictions
- [ ] May NOT surreptitiously build user profiles
- [ ] May NOT identify anonymous users or reconstruct profiles from "anonymized" data

#### (iv) Contact and Installation Data
- [ ] Do NOT use Contacts, Photos, or other APIs to build contact database for own use or sale
- [ ] Do NOT collect info about other installed apps for analytics or marketing

#### (v) Contact Communications
- [ ] Only contact people at explicit individual initiative (no Select All)
- [ ] Must show clear description of how message will appear

#### (vi) Sensitive Health and Fitness Data
**Data from these sources may NOT be used for marketing/advertising:**
- [ ] HomeKit API
- [ ] HealthKit
- [ ] Clinical Health Records API
- [ ] MovementDisorder APIs
- [ ] ClassKit
- [ ] ARKit depth/facial mapping
- [ ] Camera/Photo APIs (depth/facial mapping)

#### (vii) Apple Pay Data Sharing
- [ ] Apple Pay data only for facilitating/improving delivery of goods/services

### 5.1.3 Health and Health Research

#### (i) Health Data Use Restrictions
- [ ] Health research data NOT for advertising, marketing, or data mining
- [ ] Only for improving health management or health research (with permission)
- [ ] May use data to provide direct benefit to user (e.g., reduced insurance premium) if:
  - Submitted by entity providing benefit
  - Data not shared with third party
- [ ] Must disclose specific health data collected

#### (ii) Data Integrity
- [ ] Must NOT write false/inaccurate data to HealthKit or health apps
- [ ] May NOT store personal health info in iCloud

#### (iii) Human Subject Research Consent
**Consent must include:**
- [ ] Nature, purpose, and duration of research
- [ ] Procedures, risks, and benefits
- [ ] Confidentiality and data handling info
- [ ] Point of contact for questions
- [ ] Withdrawal process

#### (iv) Ethics Review Board Approval
- [ ] Must secure approval from independent ethics review board
- [ ] Proof must be provided upon request

### 5.1.4 Kids

#### (a) Children's Privacy Laws and Data Collection
- [ ] Comply with COPPA, GDPR, and all applicable children's privacy laws
- [ ] May ask for birthdate/parental contact ONLY for statutory compliance
- [ ] Must include useful functionality regardless of age
- [ ] Should NOT include third-party analytics (safer experience)
- [ ] Should NOT include third-party advertising (safer experience)

#### (b) Third-Party Services in Kids Apps
- [ ] Third-party analytics/advertising permitted only if adhering to Guideline 1.3
- [ ] Apps collecting/transmitting/capable of sharing kids' personal data MUST:
  - Include privacy policy
  - Comply with all applicable children's privacy statutes
- [ ] Terms "For Kids" and "For Children" reserved for Kids Category
- [ ] Non-Kids Category apps cannot imply main audience is children

### 5.1.5 Location Services
- [ ] Use ONLY when directly relevant to features
- [ ] NOT for emergency services or autonomous control (except small devices)
- [ ] Notify and obtain consent before collecting location
- [ ] Explain purpose in app

```swift
// REQUIRED: Location purpose string
<key>NSLocationWhenInUseUsageDescription</key>
<string>Your location is used to find nearby coffee shops and show them on the map</string>

// FLAG: Over-requesting location permission
<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
// Only if truly needed for background location

// GOOD: Request minimum needed
locationManager.requestWhenInUseAuthorization() // Preferred

// FLAG: Request more than needed
locationManager.requestAlwaysAuthorization() // Only if background truly needed
```

---

## 5.2 Intellectual Property

### 5.2.1 Generally
- [ ] Only use content you created or have license for
- [ ] No protected third-party material without permission
- [ ] No misleading, false, or copycat representations
- [ ] Apps should be submitted by owner or licensee

### 5.2.2 Third-Party Sites/Services
- [ ] Ensure permission under service's terms of use
- [ ] Authorization must be provided upon request

### 5.2.3 Audio/Video Downloading
- [ ] Should NOT facilitate illegal file sharing
- [ ] No ability to save/convert/download from third-party sources without authorization
- [ ] Verify Terms of Use for streaming

### 5.2.4 Apple Endorsements

#### (a) No False Apple Association
- [ ] Don't suggest Apple is source/supplier of app
- [ ] Don't suggest Apple endorses quality or functionality

#### (b) Editor's Choice Badge
- [ ] Applied automatically by Apple if selected

### 5.2.5 Apple Products
- [ ] Don't create apps confusingly similar to Apple products/interfaces
- [ ] Apps, extensions, keyboards, Sticker packs may NOT include Apple emoji
- [ ] Music previews only with link to iTunes/Apple Music
- [ ] Activity rings should not mimic Activity control
- [ ] Apple Weather data requires proper attribution

---

## 5.3 Gaming, Gambling, and Lotteries

### 5.3.1 Sweepstakes and Contests
- [ ] Must be sponsored by developer of app

### 5.3.2 Official Rules
- [ ] Must be presented in app
- [ ] Must make clear Apple is NOT involved

### 5.3.3 In-App Purchase and Real Money Gaming
- [ ] May NOT use IAP for real money gaming credit

### 5.3.4 Real Money Gaming and Lotteries
- [ ] Must have necessary licensing/permissions
- [ ] Must be geo-restricted to licensed locations
- [ ] Must be free on App Store
- [ ] No illegal gambling aids (card counters)
- [ ] Lottery apps must have consideration, chance, and prize

```swift
// REQUIRED: Geo-restriction for gambling apps
func checkGamblingEligibility() -> Bool {
    guard let region = Locale.current.region?.identifier else {
        return false
    }

    let licensedRegions = ["US-NJ", "US-NV", "GB"] // Example
    return licensedRegions.contains(region)
}
```

---

## 5.4 VPN Apps

- [ ] Must use NEVPNManager API
- [ ] Must be from developer enrolled as organization
- [ ] Must declare data collection clearly before any user action
- [ ] May NOT sell, use, or disclose data to third parties
- [ ] Must commit to this in privacy policy
- [ ] Must NOT violate local laws
- [ ] If requiring VPN license in territory, provide in App Review Notes

```swift
// REQUIRED: NEVPNManager API
import NetworkExtension

let manager = NEVPNManager.shared()
// Use official API, not custom VPN implementation
```

---

## 5.5 Mobile Device Management

**May only be offered by:**
- Commercial enterprises
- Educational institutions
- Government agencies
- Companies using MDM for parental control or device security (limited cases)

**Requirements:**
- [ ] Request MDM capability from Apple
- [ ] Declare data collection clearly before any user action
- [ ] May NOT sell, use, or disclose data except for improving services to organization
- [ ] Must commit to restrictions in privacy policy
- [ ] Must NOT violate applicable laws

---

## React Native Packages Reference

| Guideline | Expo Package | Bare RN Package |
|-----------|-------------|-----------------|
| App Tracking Transparency | `expo-tracking-transparency` | `react-native-tracking-transparency` |
| Permissions | Built-in with each expo-* package | `react-native-permissions` |
| Secure Storage | `expo-secure-store` | `react-native-keychain` |
| Analytics | Use `@react-native-firebase/analytics` (config plugin) | `@react-native-firebase/analytics` |
| Location | `expo-location` | `react-native-geolocation-service` |
| Contacts | `expo-contacts` | `react-native-contacts` |
| Camera | `expo-camera` | `react-native-vision-camera` |
| Image Picker | `expo-image-picker` | `react-native-image-picker` |

## React Native Privacy Checklist

### Permission Usage Descriptions (Critical - Common Rejection Reason)
- [ ] Verified ALL required Info.plist permission keys are present
- [ ] Each permission description explains the SPECIFIC feature using it
- [ ] No vague descriptions ("for app functionality", "required", "needed")
- [ ] Descriptions are written from user's perspective (benefit to them)
- [ ] Only requesting permissions the app actually uses
- [ ] Permissions requested contextually (not all at app launch)

### Tracking & Privacy
- [ ] ATT prompt shown before any tracking (iOS 14.5+)
- [ ] NSUserTrackingUsageDescription in Info.plist
- [ ] No tracking if user denies ATT
- [ ] Privacy policy link in app settings

### Account & Data
- [ ] Account deletion accessible within app (not just website link)
- [ ] Sensitive data stored in Keychain, not AsyncStorage
- [ ] HTTPS for all API calls
- [ ] No hardcoded secrets in JavaScript bundle

## React Native Privacy Implementation

```typescript
// Complete privacy setup for React Native

// 1. ATT on startup (before any tracking)
// Expo:
import { requestTrackingPermissionsAsync } from 'expo-tracking-transparency';
// Or bare RN:
import { requestTrackingPermission } from 'react-native-tracking-transparency';

useEffect(() => {
  const initPrivacy = async () => {
    // Request ATT first
    const trackingStatus = await requestTrackingPermission();

    // Only initialize tracking SDKs if authorized
    if (trackingStatus === 'authorized') {
      await initializeAnalytics();
      await initializeAdSDKs();
    }
  };
  initPrivacy();
}, []);

// 2. Secure storage for sensitive data
import * as Keychain from 'react-native-keychain';

// ✅ GOOD: Store tokens in Keychain
await Keychain.setGenericPassword('auth', token);

// ❌ BAD: Store tokens in AsyncStorage
await AsyncStorage.setItem('token', token); // Not secure!

// 3. Privacy policy in settings
const SettingsScreen = () => (
  <View>
    <Button
      title="Privacy Policy"
      onPress={() => Linking.openURL('https://example.com/privacy')}
    />
    <Button
      title="Delete Account"
      onPress={deleteAccount}
      color="red"
    />
  </View>
);
```

