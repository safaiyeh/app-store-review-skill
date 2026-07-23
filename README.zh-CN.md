# App Store 审核指南技能

[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md)

一项 AI 智能体技能，可依据 Apple 的 App Store 审核指南，针对其中的**每一项要求**全面评估 iOS、macOS、tvOS、watchOS 和 visionOS 应用代码。

**支持：** Swift、Objective-C、**React Native** 和 **Expo** 应用

**内容更新至：** Apple 于 2026 年 6 月 8 日发布的官方 App Store 审核指南更新

## 安装

### Codex

将此仓库添加为 Codex 插件市场：

```bash
codex plugin marketplace add safaiyeh/app-store-review-skill
```

然后打开 Codex，运行 `/plugins`，选择 App Store Review 市场并安装 `app-store-review` 插件。新建一个任务，然后使用 `$app-store-review` 调用该技能，或直接请求进行 App Store 合规性审查。

Codex 也会从 `~/.agents/skills` 中发现直接安装的本地技能，但对于可复用技能，建议通过插件分发。

### Claude Code 插件市场

```bash
/plugin marketplace add safaiyeh/app-store-review-skill
/plugin install app-store-review@app-store-review
```

### skills.sh

```bash
npx skills add safaiyeh/app-store-review-skill
```

## 设置

### 支持的 AI 智能体

此技能可与 Codex 以及支持 skills.sh 标准的 AI 编程智能体配合使用：

- [Codex](https://openai.com/codex/)
- [Claude Code](https://claude.ai/code)
- [Cursor](https://cursor.sh)
- [Windsurf](https://codeium.com/windsurf)
- 以及其他兼容的智能体

### 工作原理

1. 使用上面的命令在项目中**安装该技能**
2. 在项目目录中**启动 AI 智能体**
3. **请求 App Store 审查**——智能体会自动加载相关指南
4. **查看审查结果**——智能体会通过代码引用指出可能导致审核被拒的问题

### 提示词示例

```
"Review this app for App Store compliance"
"Check if my IAP implementation follows Apple's guidelines"
"Audit the privacy and data collection in this React Native app"
"What App Store issues might block my submission?"
```

### 遥测

skills CLI 会收集匿名使用情况遥测数据。如需退出：

```bash
SKILLS_NO_TELEMETRY=1 npx skills add safaiyeh/app-store-review-skill
```

## 结构

```
app-store-review-skill/
├── .agents/
│   └── plugins/marketplace.json # Codex 插件市场
├── .claude-plugin/
│   ├── marketplace.json        # Claude Code 插件市场
│   └── plugin.json             # Claude Code 插件清单
├── .codex-plugin/
│   └── plugin.json             # Codex 插件清单
├── agents/
│   └── openai.yaml             # Codex UI 元数据
├── SKILL.md                    # 包含快速参考和检查清单的索引
└── rules/
    ├── 1-safety.md             # 第 1 节：安全指南
    ├── 2-performance.md        # 第 2 节：性能指南
    ├── 3-business.md           # 第 3 节：商业指南
    ├── 4-design.md             # 第 4 节：设计指南
    └── 5-legal.md              # 第 5 节：法律指南
```

## 覆盖范围

此技能覆盖**全部 5 个主要章节**及其中的**每一项指南要求**：

### [1. 安全](rules/1-safety.md)
- 1.1 令人反感的内容（1.1.1–1.1.7）
- 1.2 用户生成内容与创作者内容
- 1.3 儿童类别（家长门控、隐私、分析）
- 1.4 人身伤害（医疗应用、药物剂量、相关物质）
- 1.5 开发者信息
- 1.6 数据安全
- 1.7 举报犯罪活动

### [2. 性能](rules/2-performance.md)
- 2.1 应用完整性（最终版本、应用内购买）
- 2.2 Beta 测试
- 2.3 准确的元数据（2.3.1–2.3.13）
- 2.4 硬件兼容性（2.4.1–2.4.5）
- 2.5 软件要求（2.5.1–2.5.18）

### [3. 商业](rules/3-business.md)
- 3.1 付款（应用内购买、订阅、外部链接、加密货币）
- 3.1.1–3.1.5 应用内购买规则
- 3.2 其他商业模式（可接受与不可接受）

### [4. 设计](rules/4-design.md)
- 4.1 山寨应用
- 4.2 最低功能要求
- 4.3 垃圾应用
- 4.4 扩展（键盘、Safari）
- 4.5 Apple 网站与服务
- 4.7 迷你应用、聊天机器人、游戏模拟器
- 4.8 登录服务
- 4.9 Apple Pay
- 4.10 内置功能的商业化

### [5. 法律](rules/5-legal.md)
- 5.1 隐私（数据收集、使用、共享、健康、儿童、位置）
- 5.2 知识产权
- 5.3 游戏、赌博、彩票
- 5.4 VPN 应用
- 5.5 移动设备管理
- 5.6 开发者行为准则（评论、开发者身份、发现欺诈、应用质量）

## 功能

- **模块化结构**——智能体只加载相关章节
- **2000 多行**全面的指南内容
- 针对每项指南要求的**检查清单**
- 同时适用于 Swift 和 React Native/Expo 的**代码模式**
- 同时涵盖 Expo 与纯 React Native 的**软件包参考**
- 面向高风险审核被拒模式的**快速参考**
- 主 SKILL.md 中的**提交前检查清单**

## React Native / Expo 支持

每个规则文件都包含：
- 需要标记的 TypeScript/JavaScript 代码模式
- Expo 软件包建议（首选）
- 纯 React Native 软件包替代方案
- React Native 专用检查清单

涵盖的主要软件包：
- `react-native-purchases`（RevenueCat——推荐用于应用内购买）/ `react-native-iap`
- `expo-tracking-transparency` / `react-native-tracking-transparency`
- `expo-secure-store` / `react-native-keychain`
- `expo-apple-authentication` / `@invertase/react-native-apple-authentication`
- `expo-local-authentication` / `react-native-biometrics`

## 检查内容

### 严重问题（立即被拒）
- 使用私有 API
- 硬编码的秘密信息/凭据
- 数字商品使用外部付款方式
- 在设备上进行加密货币挖矿
- 动态执行代码

### 高风险问题
- 缺少 App Tracking Transparency
- 允许创建账户但无法删除账户
- 应用内购买不支持恢复购买
- 用户生成内容缺少审核机制
- 用户生成内容缺少移除工作流或合规改进计划
- 儿童应用缺少家长门控
- 使用实时活动或推送通知发送垃圾信息、网络钓鱼内容或未经请求的消息

### 中等风险问题
- 用途说明含糊
- 请求过多权限
- 使用没有充分理由的后台模式
- 提及其他平台
- 使用自定义评论提示，而非系统 API

## 触发场景

在处理以下任务时，该技能会被激活：
- App Store 提交准备
- 代码合规性审查
- 付款/StoreKit 实现
- 隐私与数据处理
- 用户生成内容功能
- 儿童类别应用
- 健康/医疗应用
- VPN/MDM 应用
- 赌博/彩票应用

## 许可证

MIT
