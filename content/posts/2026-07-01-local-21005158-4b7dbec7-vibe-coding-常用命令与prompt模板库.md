{

  "title": "Vibe Coding -- 常用命令与Prompt模板库",
  "has_date": true,
  "description": "Claude Code 命令速查 命令 功能 启动交互式会话 使用指定模型启动 单次执行模式 显示帮助 查看/切换模型 压缩上下文 清空对话 管理记忆 查看费用 代码审查 初始化CLAUDE.md 中断操作 取消生成 Git 命令速查 命令 功能 初始化仓库 查看状态 暂存所有修改 提交 推送到远程",
  "tags": [
    "Vibe Coding",
    "Prompt"
  ],
  "source": "cnblogs-local-export",
  "source_path": "博客园_alineverstop_VibeCoding_Markdown/007_21005158_vibe-coding-常用命令与prompt模板库",
  "date": "2026-07-01",
  "source_url": "https://www.cnblogs.com/alineverstop/p/21005158"

}

#### Claude Code 命令速查

<table> <thead> <tr> <th>命令</th> <th>功能</th> </tr> </thead> <tbody> <tr> <td>`claude`</td> <td>启动交互式会话</td> </tr> <tr> <td>`claude --model <model>`</td> <td>使用指定模型启动</td> </tr> <tr> <td>`claude -p "prompt"`</td> <td>单次执行模式</td> </tr> <tr> <td>`/help`</td> <td>显示帮助</td> </tr> <tr> <td>`/model`</td> <td>查看/切换模型</td> </tr> <tr> <td>`/compact`</td> <td>压缩上下文</td> </tr> <tr> <td>`/clear`</td> <td>清空对话</td> </tr> <tr> <td>`/memory`</td> <td>管理记忆</td> </tr> <tr> <td>`/cost`</td> <td>查看费用</td> </tr> <tr> <td>`/review`</td> <td>代码审查</td> </tr> <tr> <td>`/init`</td> <td>初始化CLAUDE.md</td> </tr> <tr> <td>`Ctrl+C`</td> <td>中断操作</td> </tr> <tr> <td>`Esc`</td> <td>取消生成</td> </tr> </tbody> </table>

#### Git 命令速查

<table> <thead> <tr> <th>命令</th> <th>功能</th> </tr> </thead> <tbody> <tr> <td>`git init`</td> <td>初始化仓库</td> </tr> <tr> <td>`git status`</td> <td>查看状态</td> </tr> <tr> <td>`git add .`</td> <td>暂存所有修改</td> </tr> <tr> <td>`git commit -m "msg"`</td> <td>提交</td> </tr> <tr> <td>`git push`</td> <td>推送到远程</td> </tr> <tr> <td>`git pull`</td> <td>拉取远程更新</td> </tr> <tr> <td>`git checkout .`</td> <td>撤销所有未提交的修改</td> </tr> <tr> <td>`git log --oneline`</td> <td>查看提交历史</td> </tr> <tr> <td>`git diff`</td> <td>查看修改内容</td> </tr> </tbody> </table>

#### npm 命令速查

<table> <thead> <tr> <th>命令</th> <th>功能</th> </tr> </thead> <tbody> <tr> <td>`npm init -y`</td> <td>初始化项目</td> </tr> <tr> <td>`npm install <包名>`</td> <td>安装依赖</td> </tr> <tr> <td>`npm install -g <包名>`</td> <td>全局安装</td> </tr> <tr> <td>`npm run dev`</td> <td>启动开发服务器</td> </tr> <tr> <td>`npm run build`</td> <td>构建项目</td> </tr> <tr> <td>`npm test`</td> <td>运行测试</td> </tr> </tbody> </table>

#### 终端基础命令速查

<table> <thead> <tr> <th>命令</th> <th>功能</th> <th>Windows 替代</th> </tr> </thead> <tbody> <tr> <td>`pwd`</td> <td>查看当前目录</td> <td>`pwd` (PowerShell)</td> </tr> <tr> <td>`ls`</td> <td>列出文件</td> <td>`dir`</td> </tr> <tr> <td>`cd <路径>`</td> <td>切换目录</td> <td>同左</td> </tr> <tr> <td>`mkdir <名称>`</td> <td>创建目录</td> <td>同左</td> </tr> <tr> <td>`clear`</td> <td>清屏</td> <td>`cls`</td> </tr> </tbody> </table>

### 附录B：Prompt 模板库

#### 项目初始化模板

```text
我要创建一个 [项目类型] 项目。

项目名称：[名称]
简述：[一句话描述]
技术栈：[前端框架] + [后端框架] + [数据库]

核心功能（MVP）：
1. [功能1]
2. [功能2]
3. [功能3]

请先创建项目结构和基础配置文件，暂不实现具体功能。

```

#### 功能实现模板

```text
请在 [指定目录/文件] 中实现 [功能名称]。

具体需求：
1. [需求点1]
2. [需求点2]
3. [需求点3]

技术约束：
- 参考 [已有文件/模块] 的风格
- 使用 [指定技术/库]
- 返回格式遵循 [项目约定的格式]

请先说明实现计划，确认后再开始编码。

```

#### Bug 修复模板

```text
发现一个Bug，需要修复：

现象：[实际看到的行为]
期望：[应该是什么行为]
复现步骤：
1. [步骤1]
2. [步骤2]

错误信息：
[粘贴完整的错误堆栈]

我已经尝试过：[你尝试的解决方案]

请定位问题原因并修复。

```

#### 代码审查模板

```text
请对 [文件路径或范围] 进行代码审查。

审查重点：
1. 安全性（输入验证、XSS防护、SQL注入）
2. 错误处理（异常是否被正确捕获和处理）
3. 性能（是否有明显的性能问题）
4. 代码质量（可读性、命名规范、重复代码）

请按严重程度分级：Critical / Warning / Info
并给出具体的修复建议。

```

#### 架构设计模板

```text
我需要设计一个 [系统/功能] 的架构。

业务需求：[描述]
性能要求：[QPS/响应时间/并发用户数]
技术约束：[必须使用的技术/限制条件]

请给出：
1. 系统架构图（文字描述即可）
2. 技术选型建议及理由
3. 数据模型设计
4. API 接口设计
5. 潜在的技术风险和应对方案

```

###

### 附录E：术语表

<table> <thead> <tr> <th>英文术语</th> <th>中文释义</th> <th>简要说明</th> </tr> </thead> <tbody> <tr> <td>AI-Assisted Programming</td> <td>AI辅助编程</td> <td>使用AI工具帮助编写代码</td> </tr> <tr> <td>Agent</td> <td>智能体</td> <td>能自主执行任务的AI系统</td> </tr> <tr> <td>Agentic Engineering</td> <td>智能体工程化</td> <td>系统化的AI驱动开发方法论</td> </tr> <tr> <td>API</td> <td>应用程序接口</td> <td>程序之间通信的规则</td> </tr> <tr> <td>API Key</td> <td>API密钥</td> <td>访问AI服务的身份凭证</td> </tr> <tr> <td>CLI</td> <td>命令行界面</td> <td>通过文字命令操作电脑</td> </tr> <tr> <td>Context Window</td> <td>上下文窗口</td> <td>AI一次能处理的最大内容量</td> </tr> <tr> <td>CRUD</td> <td>增删改查</td> <td>Create/Read/Update/Delete</td> </tr> <tr> <td>Hallucination</td> <td>幻觉</td> <td>AI编造不存在的信息</td> </tr> <tr> <td>IDE</td> <td>集成开发环境</td> <td>编写代码的专业软件</td> </tr> <tr> <td>LLM</td> <td>大语言模型</td> <td>如Claude、GPT等AI模型</td> </tr> <tr> <td>MCP</td> <td>模型上下文协议</td> <td>AI工具的扩展能力标准</td> </tr> <tr> <td>MVP</td> <td>最小可行产品</td> <td>只包含核心功能的第一个版本</td> </tr> <tr> <td>ORM</td> <td>对象关系映射</td> <td>用代码操作数据库的工具（如Prisma）</td> </tr> <tr> <td>PRD</td> <td>产品需求文档</td> <td>描述产品"做什么"的文档</td> </tr> <tr> <td>Prompt</td> <td>提示词</td> <td>给AI的指令/问题</td> </tr> <tr> <td>RAG</td> <td>检索增强生成</td> <td>结合搜索和AI生成的技术</td> </tr> <tr> <td>SDD</td> <td>规范驱动开发</td> <td>先写规范再让AI执行的方法</td> </tr> <tr> <td>Skill</td> <td>技能</td> <td>封装的可复用AI指令集</td> </tr> <tr> <td>SPEC</td> <td>技术规范</td> <td>描述产品"怎么做"的文档</td> </tr> <tr> <td>Token</td> <td>令牌</td> <td>AI处理文本的基本单位</td> </tr> <tr> <td>Vibe Coding</td> <td>氛围编程</td> <td>凭感觉和意图驱动的AI编程方式</td> </tr> </tbody> </table>
