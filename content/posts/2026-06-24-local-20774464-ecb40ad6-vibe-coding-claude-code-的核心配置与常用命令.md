{

  "title": "Vibe Coding -- Claude Code 的核心配置与常用命令",
  "has_date": true,
  "description": "Claude Code用久了你会发现三个问题： 它怎么把文件改坏了？** → 你得学会管住它 用着用着怎么变笨了？** → 你得学会管理上下文 它对每个人都一样，怎么让它懂我？** → 你得学会个性化配置 Claude Code 的能力可以按 **7 层扩展（Harness）** 来理解。Anthr",
  "tags": [
    "Vibe Coding",
    "Claude"
  ],
  "source": "cnblogs-local-export",
  "source_path": "博客园_alineverstop_VibeCoding_Markdown/002_20774464_vibe-coding-claude-code-的核心配置与常用命令",
  "date": "2026-06-24",
  "source_url": "https://www.cnblogs.com/alineverstop/p/20774464"

}

Claude Code用久了你会发现三个问题：

1. **它怎么把文件改坏了？** → 你得学会管住它
2. **用着用着怎么变笨了？** → 你得学会管理上下文
3. **它对每个人都一样，怎么让它懂我？** → 你得学会个性化配置

Claude Code 的能力可以按 **7 层扩展（Harness）** 来理解。Anthropic 官方在 2026 年 5 月的企业级指南中总结了这个框架：

1. **CLAUDE.md** — 项目说明书，每次会话自动加载
2. **Hooks** — 事件触发器，在特定时机自动执行
3. **Skills** — 专业知识包，AI 按需加载
4. **Plugins** — 把 Skills + Hooks + MCP 打包分发
5. **LSP** — 给 AI 装上 IDE 级的代码导航
6. **MCP** — 连接外部工具和数据源
7. **子 Agent** — 独立上下文并行干活

这 7 层从底向上，每一层建立在前一层之上。**前 3 层是基础配置，后 4 层是高级扩展**。

官方反复强调一个观点：**模型能力是地板，配置质量才是天花板**。花时间把配置做好，比追最新模型版本更有实际收益。

### 3.1 模型选择与切换

**Claude 模型家族对比：**

<table> <thead> <tr> <th>模型</th> <th>速度</th> <th>代码质量</th> <th>推理能力</th> <th>成本</th> <th>推荐场景</th> </tr> </thead> <tbody> <tr> <td>Claude Haiku 4.5</td> <td>极快</td> <td>良好</td> <td>中等</td> <td>$ 较低</td> <td>简单代码补全、格式化、小修改</td> </tr> <tr> <td>Claude Sonnet 4.6</td> <td>快</td> <td>优秀</td> <td>强</td> <td>$$ 适中</td> <td>日常开发、功能实现（**默认推荐**）</td> </tr> <tr> <td>Claude Opus 4.7</td> <td>中等</td> <td>顶级</td> <td>极强</td> <td>$$$ 较高</td> <td>复杂架构设计、疑难 Bug、算法难题</td> </tr> </tbody> </table>

>

**提示**：日常开发使用 Sonnet 就足够了。只在遇到特别复杂的问题时才切换到 Opus。Haiku 适合大批量处理简单的任务。

**在 Claude Code 中切换模型（四种方式）：**

Claude Code 提供了四种模型切换方式，按优先级从高到低排列：

**方法一：启动时指定（临时使用）**

```text
# 使用模型别名（推荐，自动指向最新版本）
$ claude --model opus      # 最强推理
$ claude --model sonnet    # 日常编码（默认）
$ claude --model haiku     # 快速轻量

# 使用具体模型名时，请以当前服务商官方文档为准
$ claude --model opus
$ claude --model "deepseek-v4-pro[1m]"

```

>

**提示**：Claude Code 提供了方便的**模型别名**，常见包括 `opus`、`sonnet`、`haiku`、`default` 等。具体别名会随版本变化，使用前以 `/model` 当前显示为准。

**方法二：运行中切换（使用斜杠命令）**

在 Claude Code 对话中直接输入：

```text
> /model           # 打开模型选择器（交互式）
> /model sonnet      # 直接切换到 Sonnet
> /model opus       # 直接切换到 Opus

```

**方法三：环境变量持久设置**

```text
# 设置默认使用的模型（支持别名或具体名称）
export ANTHROPIC_MODEL="sonnet"

```

**方法四：配置文件持久设置（推荐）**

在 `settings.json` 中设置 `model` 字段，重启即生效：

```text
// ~/.claude/settings.json（全局生效）
{
  "model": "sonnet"
}

```

```text
// 项目/.claude/settings.json（仅该项目生效）
{
  "model": "opus"
}

```

>

**注意**：四种方式的优先级为：`--model` 启动参数 > `ANTHROPIC_MODEL` 环境变量 > `settings.json` 中的 `model` 字段。`/model` 命令的选择会保存到用户设置文件。

**配置文件层级说明：**

<table> <thead> <tr> <th>配置文件位置</th> <th>作用范围</th> <th>是否提交 Git</th> <th>优先级</th> </tr> </thead> <tbody> <tr> <td>`~/.claude/settings.json`</td> <td>全局（所有项目）</td> <td>否</td> <td>低</td> </tr> <tr> <td>`项目/.claude/settings.json`</td> <td>当前项目（团队共享）</td> <td>是</td> <td>中</td> </tr> <tr> <td>`项目/.claude/settings.local.json`</td> <td>当前项目（个人私有）</td> <td>否（gitignore）</td> <td>高</td> </tr> </tbody> </table>

**不同模型的使用建议：**

<table> <thead> <tr> <th>场景</th> <th>推荐模型</th> <th>理由</th> </tr> </thead> <tbody> <tr> <td>日常功能开发</td> <td>Claude Sonnet</td> <td>速度和质量的最佳平衡</td> </tr> <tr> <td>简单代码修改/格式化</td> <td>Claude Haiku</td> <td>足够胜任，成本最低</td> </tr> <tr> <td>复杂架构设计</td> <td>Claude Opus</td> <td>最强推理，值得多花钱</td> </tr> <tr> <td>Bug调试（简单）</td> <td>Claude Sonnet</td> <td>通常够用</td> </tr> <tr> <td>Bug调试（复杂）</td> <td>Claude Opus 或 DeepSeek V4 Pro</td> <td>需要深度推理</td> </tr> <tr> <td>中文项目文档</td> <td>Claude Sonnet / 通义千问</td> <td>中文能力出色</td> </tr> <tr> <td>预算紧张</td> <td>DeepSeek API / GLM / Kimi</td> <td>按当前价格选择性价比方案</td> </tr> <tr> <td>离线/隐私敏感</td> <td>本地Ollama模型</td> <td>完全本地，免费</td> </tr> </tbody> </table>

### 3.2 核心配置详解

Claude Code 有多层配置体系，从全局到项目级，层层覆盖。

**配置层级：**

```text
全局配置（影响所有项目）
  └── ~/.claude/settings.json

项目级配置（只影响当前项目）
  └── 项目根目录/.claude/settings.json

项目上下文文件（告诉AI项目背景信息）
  └── 项目根目录/CLAUDE.md ← 最重要！

```

##### 3.2.1 settings.json 配置文件

Claude Code 的配置文件位于 `~/.claude/settings.json`（全局）或项目目录下的 `.claude/settings.json`（项目级）。

常用配置项：

```text
{
  // 允许 Claude Code 执行的操作（不再需要每次确认）
  "permissions": {
   "allow": [
     "Read",        // 读取文件
     "Write",       // 写入文件
     "Bash(npm *)",   // 执行 npm 命令
     "Bash(git *)",   // 执行 git 命令
     "Bash(node *)"   // 执行 node 命令
   ],
   "deny": [
     "Bash(rm -rf *)" // 禁止执行危险的删除命令
   ]
  },
  // 默认使用的模型
  "model": "sonnet",
  // 自动紧凑阈值（上下文使用超过此比例时自动压缩）
  "autoCompactThreshold": 80
}

```

>

**注意**：权限设置要谨慎。过于宽松的权限可能导致AI执行你不期望的操作。建议初学者保持默认设置，让 Claude Code 在执行每个操作前都询问你确认。

##### 3.2.2 CLAUDE.md：你的项目"说明书"

CLAUDE.md 是 Claude Code 中**最重要的配置文件之一**。它就像你给新来的实习生写的"项目入职手册" —— 告诉AI这个项目的背景、技术栈、编码规范和当前进度。

**为什么 CLAUDE.md 如此重要？**

没有 CLAUDE.md 时，Claude Code 每次开始工作都要花时间"重新认识"你的项目。有了 CLAUDE.md，它一启动就知道项目的全部背景，效率大幅提升。

**CLAUDE.md 模板（可直接复制修改）：**

```text
# 项目名称

## 项目概述
一句话描述这个项目做什么。

## 技术栈
- 前端：Next.js 14 + TypeScript + Tailwind CSS
- 后端：Next.js API Routes
- 数据库：Prisma + SQLite
- 部署：Vercel

## 项目结构
​```
src/
├── app/         # Next.js App Router 页面
│   ├── api/      # API 路由
│   ├── layout.tsx # 全局布局
│   └── page.tsx   # 首页
├── components/   # React 组件
│   ├── ui/      # 通用UI组件
│   └── features/  # 业务组件
├── lib/         # 工具函数和配置
├── prisma/      # 数据库 schema 和迁移
└── types/       # TypeScript 类型定义
​```

## 编码规范
- 使用函数式组件 + React Hooks
- 组件文件使用 PascalCase 命名（如 BookmarkCard.tsx）
- 工具函数使用 camelCase 命名
- API 路由返回统一格式：{ success: boolean, data?: any, error?: string }
- 所有数据库操作通过 Prisma Client 执行

## 当前开发状态
-  项目初始化完成
-  数据库 Schema 设计完成
-  书签 CRUD API 开发中
-  前端页面待开发
-  搜索功能待开发

## 注意事项
- SQLite 数据库文件在 prisma/dev.db，不要提交到 Git
- 环境变量在 .env 文件中，不要提交到 Git
- 所有新功能先创建 Git 分支再开发

```

**CLAUDE.md 的三个层级（由顶向下叠加生效）：**

很多人只知道 CLAUDE.md 可以放在项目根目录，其实官方设计了 **3 个层级的 CLAUDE.md**，它们会同时生效、不冲突：

<table> <thead> <tr> <th>层级</th> <th>路径</th> <th>作用范围</th> <th>适合写什么</th> </tr> </thead> <tbody> <tr> <td>**全局级**</td> <td>`~/.claude/CLAUDE.md`</td> <td>所有项目都会读</td> <td>个人习惯、身份、翻译偏好（如"永远用中文回答"、"我是 xx、从事 xx"）</td> </tr> <tr> <td>**项目级**</td> <td>项目根目录/`CLAUDE.md`</td> <td>仅本项目</td> <td>项目技术栈、架构、规范、进度（可提交 Git，团队共享）</td> </tr> <tr> <td>**文件夹级**</td> <td>子目录/`CLAUDE.md`</td> <td>仅该子目录</td> <td>模块专属约定（如 `src/payment/CLAUDE.md` 写支付模块踩过的坑）</td> </tr> </tbody> </table>

三层叠加生效，不冲突。优先级：文件夹级 > 项目级 > 全局级。

**两个官方推荐的创建姿势：**

- **`/init` 创建项目级**：在项目根目录下运行 `claude` 后输入 `/init`，cc 会自动扫描项目并生成一份 CLAUDE.md 初稿，你再调整。官方建议：**项目有一定规模再 `/init` 效果更好**（太空它扫不出什么东西）。
- **`/memory` 编辑全局级**：在 cc 会话里输入 `/memory` 选择“全局 CLAUDE.md”，会用默认编辑器打开该文件供你修改。**修改全局后需重启 cc 才生效。**

**最佳实践：**

1.

**保持更新**：项目级 CLAUDE.md 应该是动态的——项目加了功能、踩了坑，就同步更新

2.

**足够具体**：技术栈写明具体版本号，目录结构要与实际一致

3.

**写明禁忌**：把"不要做什么"也写清楚（如"不要修改数据库迁移文件"）

4.

**适度简洁**：不要写成论文，AI需要的是关键信息而非赘述

5.

**只放"顶层不变原则"**：随着实践你会发现，CLAUDE.md 不该塞太多。卡帕西发布的「claude.skills」几百行通用规则就能拿 10 万+ Star——写点 “顶层、不变、须严守" 的东西就够了。

```text
https://github.com/multica-ai/andrej-karpathy-skills

```

##### 3.2.3 第二层记忆：Auto Memory（cc 自己的笔记本）

如果说 CLAUDE.md 是**你主动立下的规矩**，那 Auto Memory 就是 **cc 在干活过程中默默记下的设计笔记**。你没显式写进 CLAUDE.md 的习惯、反馈、项目踩坑，会被一个后台 agent 静静记录。

**如何启用：**

```text
# 在 cc 会话中输入
/memory

# 在弹出的菜单里选第一个选项 “启用 Auto Memory”
# 启用后菜单里会多出“打开自动记忆文件夹”选项

```

**Auto Memory 会记哪几类东西：**

<table> <thead> <tr> <th>类型</th> <th>含义</th> <th>举例</th> </tr> </thead> <tbody> <tr> <td>`user`</td> <td>关于你</td> <td>你的角色、偏好（如“不喜欢深色 UI”）</td> </tr> <tr> <td>`feedback`</td> <td>你给过的反馈</td> <td>“不要这样做"、“对，就这样"</td> </tr> <tr> <td>`project`</td> <td>项目相关</td> <td>进度、决策、技术选型</td> </tr> <tr> <td>`reference`</td> <td>外部资源索引</td> <td>“某份设计文档在 docs/design.md”</td> </tr> </tbody> </table>

**使用手感（重要）：**

- 它只在当前项目生效（文件存在项目目录下），换项目需重新积累
- 启用后 cc 不会每次都把所有记忆全部加载进上下文，只会读一份 `memory.md` 索引——**遇到具体问题才去读对应的子文件**，占 token 很少
- 随时可以用快捷键 `Ctrl+O` 在会话中查看实际被调用过的记忆内容
- 记错了就跟它说：“忘掉刚刚说的不喜欢深色主题”，它会自己删掉

>

提示： **一句话区分 CLAUDE.md vs Auto Memory**：CLAUDE.md 是**第一优先级、全量注入的明规则**；Auto Memory 是**第二优先级、按需注入的隐规则**。两者配合，cc 越用越懂你。

##### 3.2.4 第三层记忆：自建参考文档（渐进式披露）

除了上面两层，你还可以仿照 Skill 的"**渐进式披露**"机制为 cc 手动打造一套**专项参考文档**。

**应用场景**：某些东西不适合全部塞进 CLAUDE.md（太长、太专门），但 cc 需要的时候必须能查到。比如做个产品，你希望：

- **品牌视觉规范**：颜色、字体、间距 → `docs/brand-visual.md`
- **产品文本风格**：语调、术语表 → `docs/copywriting-style.md`
- **API 约定**：请求响应格式、错误码 → `docs/api-conventions.md`

然后在 CLAUDE.md 里加上指引：

```text
## 外部参考文档

- 修改前端视觉、调颜色、调间距时 → 必读 `docs/brand-visual.md`
- 写产品文案、按钮文字、提示语时 → 必读 `docs/copywriting-style.md`
- 写 API 、定义返回格式时 → 必读 `docs/api-conventions.md`

```

这样 cc 只在"需要的时候"才去读完整文档，既保证了准确性，又不占多余上下文。

##### 3.2.5 三层记忆总览

Claude Code 的三层记忆体系：第一层 CLAUDE.md（你主动写，全量加载）→ 第二层 Auto Memory（cc 自己记，按需读取）→ 第三层自建参考文档（你写，cc 遇到对应任务才读）。

<table> <thead> <tr> <th>层</th> <th>位置</th> <th>优先级</th> <th>加载方式</th> <th>谁在维护</th> </tr> </thead> <tbody> <tr> <td>1</td> <td>CLAUDE.md（三级）</td> <td>高</td> <td>会话启动全量加载</td> <td>你手动维护</td> </tr> <tr> <td>2</td> <td>Auto Memory</td> <td>中</td> <td>先读索引、按需读子文件</td> <td>cc 自己写、你校对修改</td> </tr> <tr> <td>3</td> <td>参考文档</td> <td>按需</td> <td>cc 遇到对应任务才读</td> <td>你手动维护</td> </tr> </tbody> </table>

>

**本质认知**：agent 的所有"记忆"，本质上都是在**合适的时候向大模型注入压缩过的上下文**。粗暴点说 —— 这些记忆机制本质上还是提示词工程，只不过由 cc 帮你组织了层次。

##### 3.2.6 .claudeignore 文件

类似于 `.gitignore`，用来告诉 Claude Code 哪些文件/目录不需要关注：

```text
# .claudeignore 示例
node_modules/      # 依赖包目录（太大了，AI不需要看）
.next/            # Next.js 构建产物
dist/            # 编译输出
*.log            # 日志文件
.env             # 环境变量（包含敏感信息）

```

### 3.3 核心命令与日常使用

##### 3.3.1 启动与基本交互

```text
# 最基本的启动方式（在当前目录启动）
$ claude

# 指定项目目录启动
$ claude --project-dir /path/to/your/project

# 使用指定模型启动
$ claude --model sonnet

# 单次执行模式（执行完就退出，适合脚本调用）
$ claude -p "请列出当前目录下所有的 JavaScript 文件"

```

##### 3.3.2 对话交互基础

启动 Claude Code 后，你就进入了一个交互式对话界面。你输入需求，AI分析后执行。

**典型的交互流程：**

```text
你：帮我创建一个简单的 HTML 页面，显示"Hello AI Coding"

AI：好的，我来创建这个页面。

[AI 分析需求]
[AI 请求确认：我将创建文件 index.html，是否允许？]

你：是（按 Enter 确认）

AI： 已创建 index.html，包含以下内容：
   - 基本 HTML5 结构
   - 一个标题显示"Hello AI Coding"
   - 简单的居中样式

```

**权限确认机制：**

Claude Code 在执行以下操作前会先询问你：

<table> <thead> <tr> <th>操作类型</th> <th>示例</th> <th>提示信息</th> </tr> </thead> <tbody> <tr> <td>创建文件</td> <td>创建 `index.html`</td> <td>"Will create file: index.html"</td> </tr> <tr> <td>修改文件</td> <td>修改 `app.js` 的第10行</td> <td>"Will edit file: app.js"</td> </tr> <tr> <td>执行命令</td> <td>运行 `npm install express`</td> <td>"Will run: npm install express"</td> </tr> <tr> <td>删除文件</td> <td>删除 `temp.txt`</td> <td>"Will delete file: temp.txt"</td> </tr> </tbody> </table>

你可以：

- 按 **Enter** 或输入 **y** → 确认执行
- 输入 **n** → 拒绝执行
- 输入补充信息 → 修改AI的计划

>

**提示**：如果你发现每次确认很烦，可以在 `settings.json` 中配置自动允许的操作（见 4.2 节）。但初学者建议保持默认，让自己有机会审查AI的每一步操作。

##### 3.3.3 核心斜杠命令详解

在 Claude Code 对话中，以 `/` 开头的命令是“斜杠命令”，用来控制Claude Code 的行为。在输入框里打一个 `/` 就会弹出完整命令清单；`/help` 列出所有可用指令。

**基础高频命令：**

<table> <thead> <tr> <th>命令</th> <th>作用</th> <th>使用场景</th> </tr> </thead> <tbody> <tr> <td>`/help`</td> <td>显示帮助信息</td> <td>忘记命令时查看</td> </tr> <tr> <td>`/model`</td> <td>查看/切换当前模型（高/中/低档）</td> <td>需要换用更强/更快的模型时</td> </tr> <tr> <td>`/compact`</td> <td>压缩当前对话的上下文</td> <td>对话太长，AI开始“遗忘”早期内容时</td> </tr> <tr> <td>`/clear`</td> <td>完全清空当前对话</td> <td>开始全新的任务时</td> </tr> <tr> <td>`/context`</td> <td>详细查看上下文占比（各 MCP/Skill 各占多少）</td> <td>优化 token、诊断哪里挨上下文</td> </tr> <tr> <td>`/memory`</td> <td>查看/编辑 CLAUDE.md 与自动记忆</td> <td>管理项目/全局记忆、开启 Auto Memory</td> </tr> <tr> <td>`/status`</td> <td>查看会话状态</td> <td>确认模型、Token 消耗</td> </tr> <tr> <td>`/cost`</td> <td>查看当前会话费用</td> <td>监控花了多少钱</td> </tr> <tr> <td>`/review`</td> <td>对当前项目进行代码审查</td> <td>完成功能后检查质量</td> </tr> <tr> <td>`/init`</td> <td>自动生成项目的 CLAUDE.md</td> <td>进入新项目后的第一件事</td> </tr> <tr> <td>`/plan`</td> <td>切入 Plan Mode（只读规划模式）</td> <td>复杂任务起手（详见 4.9 节）</td> </tr> <tr> <td>`/rewind`</td> <td>回滚 cc 之前的修改</td> <td>“后悔药”，下面重点讲</td> </tr> <tr> <td>`/resume`</td> <td>选择历史会话恢复</td> <td>上次话题还没聊完</td> </tr> <tr> <td>`/btw`</td> <td>“顺便问一句”，不污染主上下文</td> <td>主任务进行中想问个无关问题</td> </tr> </tbody> </table>

**扩展管理命令：**

<table> <thead> <tr> <th>命令</th> <th>作用</th> <th>使用场景</th> </tr> </thead> <tbody> <tr> <td>`/skill <名称>`</td> <td>直接调用某个 Skill</td> <td>手动触发，不要等 AI 自己决定</td> </tr> <tr> <td>`/agent`</td> <td>创建、查看、调用子代理（SubAgent）</td> <td>手工创建专项 SubAgent</td> </tr> <tr> <td>`/plugin`</td> <td>插件管理界面（discover / installed）</td> <td>发现、安装、卸载插件</td> </tr> <tr> <td>`/login`</td> <td>使用 Claude 官方订阅会员登录</td> <td>有 Claude Pro/Max 会员时首选</td> </tr> <tr> <td>`/simplify`</td> <td>派 3 个子 Agent 从代码质量/性能/复用性三个角度优化</td> <td>快速全面优化已有代码</td> </tr> </tbody> </table>

**最常用的三个命令详解：**

**`/compact` —— 上下文压缩**

这是解决”用久了 AI 变笨”的核心武器。用 cc 一段时间会发现回答变慢、质量下降——这是因为你聊的每句话、它读的每个文件、它执行的每个操作的结果，都在挤占上下文空间。模型上下文虽然有 200K，但实际有效比例只有 60%-80%，且会随上下文增多能力下降。脑子里塞多了东西，它就容易把握不住重点。

`/compact` 命令会帮你”整理桌面” —— 把前面的对话压缩成摘要，腾出空间。

```text
> /compact

AI: 上下文已压缩。当前对话摘要：
   - 我们正在开发一个书签管理器项目
   - 已完成：数据库设计、API端点
   - 当前正在：前端页面开发

```

**配套命令：`/context` —— 监控上下文余量**

在 `/compact` 之前，先用 `/context` 看看当前状况：它会详细展示上下文占比，包括各个 MCP、Skill 各占用了多少 token，让你知道是什么在”吃掉”上下文。

```text
> /context

上下文使用情况：
  已使用: 142,000 / 200,000 tokens (71%)
  ├── 对话历史: 89,000 tokens
  ├── CLAUDE.md: 2,100 tokens
  ├── Skills: 12,500 tokens
  └── MCP 工具: 4,800 tokens

```

>

提示： **我的习惯**：看到上下文高于 60% 了，就 `/compact` 一下。别等到接近满载、cc 自动压缩才动手——那时候它已经开始”遗忘”了。也可以让 cc 帮你打开常驻显示，重启终端后底部就会一直显示上下文余量。

**`/compact` vs `/clear` —— 什么时候用哪个？**

<table> <thead> <tr> <th>命令</th> <th>效果</th> <th>适用时机</th> </tr> </thead> <tbody> <tr> <td>`/compact`</td> <td>压缩历史为摘要，保留关键决策</td> <td>同一任务对话过长、但还要继续做</td> </tr> <tr> <td>`/clear`</td> <td>彻底清空，等于重开</td> <td>一个独立任务彻底结束，要开始全新任务</td> </tr> </tbody> </table>

>

**心法**：宁可”多 `/clear` 几次重新介绍背景”，也不要”一直聊一直聊”。每个 `/clear` 都是给 AI 一次重新聚焦的机会。

**`/rewind` —— “后悔药”（双击 ESC 快捷启动）**

当你让 cc 改了一些代码、过后发现不满意（或者项目被改坏了），cc 自带一个回滚机制：**在对话里输入 `/rewind`，或者直接双击 `ESC`**，就会进入回滚界面：

```text
[Rewind] 选择回滚方式：
  1. 仅回滚对话        → 文件保留，只清除后面几轮对话
  2. 回滚对话 与 文件编辑 → 推荐！全部返回某个节点
  3. 仅回滚文件        → 保留对话，只还原文件

```

>

注意： **底线提醒**：`/rewind` 只能撤销 **cc 自己编辑过的文件**。它跑过的终端命令（安装依赖、下载文件、修改数据库）**撤不了**。真正靠谱的“后悔药”还是 Git。

**`/memory` —— 记忆管理**

Claude Code 有一个跨会话的“长期记忆”系统。它会自动记住你的偏好和项目信息，下次启动时依然记得。`/memory` 进去后可以编辑全局 / 项目 CLAUDE.md、开启自动记忆。

**`/review` —— 代码审查**

完成功能开发后，让 AI 审查你的代码质量：

```text
> /review

AI: 正在审查项目代码...

审查结果：
 代码结构清晰
注意： api/bookmarks.ts 第15行：缺少输入验证
注意： components/BookmarkList.tsx：建议添加 loading 状态
 发现潜在安全问题：SQL 查询未使用参数化查询

```

##### 3.3.4 快捷键速查

<table> <thead> <tr> <th>快捷键</th> <th>作用</th> </tr> </thead> <tbody> <tr> <td>`Enter`</td> <td>发送消息 / 确认操作</td> </tr> <tr> <td>`Shift + Enter`</td> <td>**也是发送**（不是换行！超多新手在这里发出了半截提示词）</td> </tr> <tr> <td>`Option + Enter`（Mac）</td> <td>换行输入（在提示词里换行不发送）</td> </tr> <tr> <td>`Ctrl + Enter`（Windows）</td> <td>换行输入（同上）</td> </tr> <tr> <td>`Ctrl + C`</td> <td>中断当前操作</td> </tr> <tr> <td>`Esc`</td> <td>取消正在生成的内容</td> </tr> <tr> <td>`Esc × 2`（双击）</td> <td>启动 `/rewind` 回滚界面</td> </tr> <tr> <td>`Shift + Tab`</td> <td>三种运行模式循环切换（Normal/Auto-Accept/Plan，详见 4.9）</td> </tr> <tr> <td>`↑` / `↓`</td> <td>浏览历史消息</td> </tr> <tr> <td>`Ctrl + B`</td> <td>让当前运行的命令到**后台**跑（不阻塞对话）</td> </tr> <tr> <td>`Ctrl + O`</td> <td>查看 Auto Memory 记录的具体内容</td> </tr> </tbody> </table>

##### 3.3.5 输入与交互高级技巧

除了打字对话，cc 还有几种交互方式能大幅提升效率。

**1. `!` 进入 Bash 模式（不用新开终端跑命令）**

在 cc 对话窗口里输入文字默认是在跟 cc 对话，不是跑 shell 命令。要跑命令有两种常见做法：

```text
 推荐：在 cc 会话里以 ! 开头，进入 Bash 模式跑命令
> !npm run dev
> !node app.js

# 取代方案：另外开一个终端跑命令

```

>

提示： **后台运行**：运行中的命令会阻塞跟 cc 的对话（比如 dev 服务起来后不会退出）。这时按 `Ctrl+B`，cc 会把它交到后台跑，你可以继续与 cc 对话。

**2. `@文件/目录` 引用（给 cc 精准上下文）**

cc 不会一直把所有项目文件加载到上下文里（项目一大也加不进去），需要时会现场 grep。**你明确 `@` 一个文件，就是在节省 cc 探路的 token 成本**。

```text
# 直接 @ 文件路径（输入时会自动弹出候选）
> 参考 @src/auth/login.ts 的风格，在 @src/auth/ 下加个 register.ts

# 提示词太长、命令行里打不下？先写到 .md 文档里，再 @ 它
> 按 @docs/feature-spec.md 的需求实现

```

>

提示： **反直觉小常识**：你给 cc 的指令**越短，它反而可能花越多 token**——因为它要多费力探索项目才能猜到你想要什么。描述越具体 + 明确 @ 文件，成本反而低，效果反而准。

**3. 贴图片（多模态能力）**

直接将图片拖拽到对话框、或者 Ctrl+V 粘贴。适合：

- 给设计参考图让 cc 实现一个类似的 UI
- 贴报错截图让 cc 判读
- 贴架架构图让 cc 按图实现

**4. 三种启动参数（命令行启动时）**

```text
claude                        # 默认启动
claude -c                      # = --continue，启动时直接接上次会话
claude --permission-mode plan       # 启动后直接进 Plan Mode
claude --dangerously-skip-permissions # "危险模式"：一路绿灯不问任何确认

```

>

注意： **危险模式使用须谨慎**：`--dangerously-skip-permissions`（绿灯模式）适合在**沙箱环境 / 有 Git 存档 / 不重要的练手项目**中使用。生产项目里不推荐，新手也请从默认模式起手。
