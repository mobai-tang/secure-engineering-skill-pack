# 安全工程 Skill Pack

[English](README.md)

一套面向 AI 编程代理的专注型 Skill Pack，用于证据驱动实施、安全设计、依赖与隐私审查、运维准备、安全迁移、上线决策和授权防御性安全审查。

## 包含的 Skill

### `modular-evidence-implementation`

用于功能实现、Bug 修复、重构、架构边界、仓库证据、聚焦测试，以及大型混合职责文件治理。

### `release-readiness-evidence`

用于预发布或生产上线前、部署审批、迁移或功能开关发布、能力边界验证、回滚、恢复，以及 `Go` 或 `No-Go` 决策。

### `authorized-security-review`

用于防御性、已授权的认证、恢复、授权、管理操作、租户隔离、滥用防护、敏感数据和安全测试审查。

### `threat-modeling-lite`

用于在实现安全敏感功能前识别资产、入口、信任边界、滥用场景、控制、测试与剩余风险。

### `supply-chain-and-dependency-review`

用于新增或升级依赖、SDK、CI Action、构建脚本、Docker 镜像、注册表、签名与发布链路组件。

### `data-privacy-review`

用于收集、存储、记录、导出、删除、分析、上传或共享用户与敏感数据的功能。

### `observability-and-incident-readiness`

用于需要日志、指标、追踪、告警、仪表盘、Runbook、止血、回滚、恢复与数据修复的生产工作流。

### `migration-and-rollback-review`

用于数据库、Schema、数据格式、队列、缓存、配置、存储、协议和混合版本发布变更。

## 为什么使用专注型 Skill？

每个 Skill 都具有精准触发条件，只在需要时加载详细 `references/`。这样能够减少过度触发、节省代理上下文，并允许独立安装或组合使用。

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
├── authorized-security-review/
├── threat-modeling-lite/
├── supply-chain-and-dependency-review/
├── data-privacy-review/
├── observability-and-incident-readiness/
└── migration-and-rollback-review/
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

## 验证安装

运行仓库校验器：

```bash
python scripts/validate_pack.py
```

然后尝试 [`examples/quickstart.md`](examples/quickstart.md) 中的任务，确认代理会选择相关专注型 Skill、区分证据与假设、报告实际执行的验证，并且不会在没有证据时声称可以上线。

GitHub Actions 会在 Push 和 Pull Request 时运行相同校验器。

## 仓库结构

```text
secure-engineering-skill-pack/
├── skills/
│   ├── modular-evidence-implementation/
│   ├── release-readiness-evidence/
│   ├── authorized-security-review/
│   ├── threat-modeling-lite/
│   ├── supply-chain-and-dependency-review/
│   ├── data-privacy-review/
│   ├── observability-and-incident-readiness/
│   └── migration-and-rollback-review/
├── shared/
├── examples/
├── scripts/validate_pack.py
├── .github/workflows/validate.yml
├── CHANGELOG.md
├── LICENSE
└── README.md
```

每个 Skill 目录包含短小的 `SKILL.md`、可选的 `agents/openai.yaml`，以及放在 `references/` 中的详细指南。

## 共享资源

- [`shared/review-mode.md`](shared/review-mode.md)：聚焦阻塞问题、风险、可维护性、测试、安全和上线问题的 PR Review 输出模式。
- [`shared/output-contract.md`](shared/output-contract.md)：统一的证据型完成报告格式。
- [`examples/`](examples/)：覆盖无证据结论、虚假验证、过度拆分、上线阻塞与未授权测试的好坏示例。

## 核心原则

- 提出实现结论前验证仓库证据。
- 明确业务归属和依赖边界。
- 手写源代码文件不得超过 800 个物理行。
- 停止重复尝试 Bug，主动查询权威资料。
- 跳过、未知和未测试的上线检查不能视为通过。
- 客户端可见性绝不是授权控制。
- 只有获得明确授权和范围后才能主动执行安全测试。
- 将数据最小化、依赖来源、可观测性和迁移恢复视为工程要求。
- 没有证据时，绝不能声称代码已修复、安全、测试完成或可以上线。

800 行限制是一个刻意宽松的审查触发线，并不表示所有超过 800 行的文件都必然错误。详细依据、例外情况和团队自定义方式位于模块化实现参考资料中。

## 使用示例

- “实现这个功能，并保持清晰模块归属和聚焦测试。”使用 `modular-evidence-implementation`。
- “判断这个版本能否上线生产环境。”使用 `release-readiness-evidence`。
- “在已授权环境中审查认证和机器人注册风险。”使用 `authorized-security-review`。
- “实现计费 Webhook 前识别威胁。”使用 `threat-modeling-lite`。
- “审查依赖和 GitHub Actions 升级。”使用 `supply-chain-and-dependency-review`。
- “审查 AI 功能如何处理用户数据。”使用 `data-privacy-review`。
- “验证服务发生事故时能否检测与恢复。”使用 `observability-and-incident-readiness`。
- “审查数据库迁移和回滚方案。”使用 `migration-and-rollback-review`。

完整的使用前后对比示例请参阅 [`examples/quickstart.md`](examples/quickstart.md)。

## 许可证

MIT
