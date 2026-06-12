# 安全工程 Skill Pack

[English](README.md)

一套面向 AI 编程代理的专注型 Skill Pack，用于证据驱动的模块化实现、上线准备决策和授权防御性安全审查。

## 包含的 Skill

### `modular-evidence-implementation`

用于功能实现、Bug 修复、重构、架构边界、仓库证据、聚焦测试，以及大型混合职责文件治理。

### `release-readiness-evidence`

用于预发布或生产上线前、部署审批、迁移或功能开关发布、能力边界验证、回滚、恢复，以及 `Go` 或 `No-Go` 决策。

### `authorized-security-review`

用于防御性、已授权的认证、恢复、授权、管理操作、租户隔离、滥用防护、敏感数据和安全测试审查。

## 为什么拆成三个 Skill？

每个 Skill 都具有更精准的触发条件，只加载当前任务需要的规则。这样能够减少过度触发、节省代理上下文，并允许独立安装或组合使用。

## 安装

从 [`skills/`](skills/) 中复制需要的 Skill 目录到目标工具的 Skill 目录。

### Codex

用户级：

```text
$HOME/.agents/skills/
```

仓库级：

```text
<repo>/.agents/skills/
```

示例：

```text
.agents/skills/
├── modular-evidence-implementation/
├── release-readiness-evidence/
└── authorized-security-review/
```

### Claude Code

个人级：

```text
~/.claude/skills/
```

项目级：

```text
.claude/skills/
```

### Cursor、Trae、Windsurf 与 GitHub Copilot

将相关 `SKILL.md` 添加为项目规则、工作区指令、代理规则或自定义指令。工具支持引用文件时，同时保留对应的 `references/` 目录。

## 仓库结构

```text
secure-engineering-skill-pack/
├── skills/
│   ├── modular-evidence-implementation/
│   ├── release-readiness-evidence/
│   └── authorized-security-review/
├── CHANGELOG.md
├── LICENSE
└── README.md
```

## 核心原则

- 提出实现结论前验证仓库证据。
- 明确业务归属和依赖边界。
- 手写源代码文件不得超过 800 个物理行。
- 停止重复尝试 Bug，主动查询权威资料。
- 跳过、未知和未测试的上线检查不能视为通过。
- 客户端可见性绝不是授权控制。
- 只有获得明确授权和范围后才能主动执行安全测试。
- 没有证据时，绝不能声称代码已修复、安全、测试完成或可以上线。

## 使用示例

- “实现这个功能，并保持清晰模块归属和聚焦测试。”使用 `modular-evidence-implementation`。
- “判断这个版本能否上线生产环境。”使用 `release-readiness-evidence`。
- “在已授权环境中审查认证和机器人注册风险。”使用 `authorized-security-review`。

## 许可证

MIT
