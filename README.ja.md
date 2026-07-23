# App Store 審査ガイドラインスキル

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

Apple の App Store 審査ガイドラインの**すべての項目**に照らして、iOS、macOS、tvOS、watchOS、visionOS アプリのコードを網羅的に評価する AI エージェントスキルです。

**対応対象：** Swift、Objective-C、**React Native**、**Expo** アプリ

**対応している最新版：** 2026 年 6 月 8 日付の Apple 公式 App Store 審査ガイドライン更新

## インストール

### Codex

このリポジトリを Codex プラグインマーケットプレイスとして追加します。

```bash
codex plugin marketplace add safaiyeh/app-store-review-skill
```

次に Codex を開いて `/plugins` を実行し、App Store Review マーケットプレイスを選択して `app-store-review` プラグインをインストールします。新しいタスクを開始し、`$app-store-review` でスキルを呼び出すか、App Store コンプライアンスレビューを依頼してください。

Codex は `~/.agents/skills` に直接配置されたローカルスキルも検出しますが、再利用可能なスキルの配布にはプラグインを推奨します。

### Claude Code プラグインマーケットプレイス

```bash
/plugin marketplace add safaiyeh/app-store-review-skill
/plugin install app-store-review@app-store-review
```

### skills.sh

```bash
npx skills add safaiyeh/app-store-review-skill
```

## セットアップ

### 対応 AI エージェント

このスキルは、Codex および skills.sh 標準に対応する AI コーディングエージェントで動作します。

- [Codex](https://openai.com/codex/)
- [Claude Code](https://claude.ai/code)
- [Cursor](https://cursor.sh)
- [Windsurf](https://codeium.com/windsurf)
- その他の互換エージェント

### 仕組み

1. 上記のコマンドを使用して、プロジェクトに**スキルをインストール**します
2. プロジェクトディレクトリで **AI エージェントを起動**します
3. **App Store 審査を依頼**します。エージェントが関連するガイドラインを自動的に読み込みます
4. **検出結果を確認**します。エージェントは、審査で却下される可能性がある問題をコード参照付きで特定します

### プロンプト例

```
"Review this app for App Store compliance"
"Check if my IAP implementation follows Apple's guidelines"
"Audit the privacy and data collection in this React Native app"
"What App Store issues might block my submission?"
```

### テレメトリ

skills CLI は匿名の利用状況テレメトリを収集します。無効にするには、次のように実行します。

```bash
SKILLS_NO_TELEMETRY=1 npx skills add safaiyeh/app-store-review-skill
```

## 構成

```
app-store-review-skill/
├── .agents/
│   └── plugins/marketplace.json # Codex プラグインマーケットプレイス
├── .claude-plugin/
│   ├── marketplace.json        # Claude Code プラグインマーケットプレイス
│   └── plugin.json             # Claude Code プラグインマニフェスト
├── .codex-plugin/
│   └── plugin.json             # Codex プラグインマニフェスト
├── agents/
│   └── openai.yaml             # Codex UI メタデータ
├── SKILL.md                    # クイックリファレンスとチェックリストを含む索引
└── rules/
    ├── 1-safety.md             # セクション 1：安全性ガイドライン
    ├── 2-performance.md        # セクション 2：パフォーマンスガイドライン
    ├── 3-business.md           # セクション 3：ビジネスガイドライン
    ├── 4-design.md             # セクション 4：デザインガイドライン
    └── 5-legal.md              # セクション 5：法的要件ガイドライン
```

## 対応範囲

このスキルは、**5 つの主要セクションすべて**と、そこに含まれる**すべてのガイドライン項目**を網羅します。

### [1. 安全性](rules/1-safety.md)
- 1.1 不適切なコンテンツ（1.1.1～1.1.7）
- 1.2 ユーザー生成コンテンツとクリエイターコンテンツ
- 1.3 「子ども向け」カテゴリ（ペアレンタルゲート、プライバシー、分析）
- 1.4 身体への危害（医療アプリ、薬の用量、薬物）
- 1.5 デベロッパ情報
- 1.6 データセキュリティ
- 1.7 犯罪行為の報告

### [2. パフォーマンス](rules/2-performance.md)
- 2.1 アプリの完全性（完成版、アプリ内課金）
- 2.2 Beta 版テスト
- 2.3 正確なメタデータ（2.3.1～2.3.13）
- 2.4 ハードウェアの互換性（2.4.1～2.4.5）
- 2.5 ソフトウェア要件（2.5.1～2.5.18）

### [3. ビジネス](rules/3-business.md)
- 3.1 支払い（アプリ内課金、サブスクリプション、外部リンク、暗号資産）
- 3.1.1～3.1.5 アプリ内課金のルール
- 3.2 その他のビジネスモデル（許容されるもの／されないもの）

### [4. デザイン](rules/4-design.md)
- 4.1 模倣
- 4.2 最低限の機能
- 4.3 スパム
- 4.4 機能拡張（キーボード、Safari）
- 4.5 Apple のサイトとサービス
- 4.7 ミニアプリ、チャットボット、ゲームエミュレータ
- 4.8 ログインサービス
- 4.9 Apple Pay
- 4.10 内蔵機能の収益化

### [5. 法的要件](rules/5-legal.md)
- 5.1 プライバシー（データの収集、使用、共有、健康、子ども、位置情報）
- 5.2 知的財産
- 5.3 ゲーム、ギャンブル、宝くじ
- 5.4 VPN アプリ
- 5.5 モバイルデバイス管理
- 5.6 デベロッパ行動規範（レビュー、デベロッパの身元、検索に関する不正、アプリの品質）

## 特長

- **モジュール構成** — エージェントは関連するセクションだけを読み込みます
- **2,000 行以上**にわたる包括的なガイドライン
- すべてのガイドライン項目に対応する**チェックリスト**
- Swift と React Native/Expo の両方に対応した**コードパターン**
- Expo とベア React Native の両方に対応した**パッケージリファレンス**
- 却下リスクが高いパターンの**クイックリファレンス**
- メインの SKILL.md にある**提出前チェックリスト**

## React Native / Expo 対応

各ルールファイルには以下が含まれています。
- フラグ対象となる TypeScript/JavaScript コードパターン
- Expo パッケージの推奨事項（推奨）
- ベア React Native パッケージの代替候補
- React Native 固有のチェックリスト

対象となる主要パッケージ：
- `react-native-purchases`（RevenueCat — アプリ内課金での使用を推奨）/ `react-native-iap`
- `expo-tracking-transparency` / `react-native-tracking-transparency`
- `expo-secure-store` / `react-native-keychain`
- `expo-apple-authentication` / `@invertase/react-native-apple-authentication`
- `expo-local-authentication` / `react-native-biometrics`

## チェック内容

### 致命的な問題（即時却下）
- プライベート API の使用
- ハードコードされたシークレット／認証情報
- デジタル商品に対する外部決済
- デバイス上での暗号資産マイニング
- 動的なコード実行

### リスクの高い問題
- App Tracking Transparency の欠如
- アカウントを作成できるが削除できない
- アプリ内課金に「購入を復元」がない
- ユーザー生成コンテンツにモデレーションがない
- ユーザー生成コンテンツに削除ワークフローまたはコンプライアンス改善計画がない
- 子ども向けアプリにペアレンタルゲートがない
- Live Activities またはプッシュ通知を、スパム、フィッシング、未承諾メッセージに使用している

### 中程度のリスクがある問題
- 目的を示す文字列が曖昧
- 過剰な権限要求
- 正当な理由のないバックグラウンドモード
- 他のプラットフォームへの言及
- システム API ではなく独自のレビュープロンプトを使用

## 起動する場面

このスキルは、以下の作業時に起動します。
- App Store への提出準備
- コードのコンプライアンスレビュー
- 決済／StoreKit の実装
- プライバシーとデータの取り扱い
- ユーザー生成コンテンツ機能
- 「子ども向け」カテゴリのアプリ
- 健康／医療アプリ
- VPN／MDM アプリ
- ギャンブル／宝くじアプリ

## ライセンス

MIT
