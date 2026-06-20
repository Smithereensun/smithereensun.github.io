{

  "title": "MCP入门知识",
  "has_date": true,
  "description": "前言 LLM 是大脑，MCP 是手脚。LLM 不断提升智能下限，MCP 不断提升创意上限。 目前为止，比较公认的一个观点是：2025年是 Agent 元年。虽然 AI 在短期内依旧面临 ROI 的考验，但几乎所有人都不会怀疑他的未来，不希望错过这一场“军备竞赛”。 简介 MCP 介绍 MCP 版本历",
  "tags": [
    "AI",
    "MCP"
  ],
  "source": "local-markdown-library",
  "source_path": "ai/mcp-summary - MCP入门知识.md",
  "date": "2026-04-19"

}

## [前言](#前言)

LLM 是大脑，MCP 是手脚。LLM 不断提升智能下限，MCP 不断提升创意上限。

目前为止，比较公认的一个观点是：2025年是 Agent 元年。虽然 AI 在短期内依旧面临 ROI 的考验，但几乎所有人都不会怀疑他的未来，不希望错过这一场“军备竞赛”。

## [简介](#简介)

### [MCP 介绍](#mcp-介绍)

MCP 版本历史（2025-04-15 统计）：
版本号重大变化2024-11-05初代 MCP 协议2025-03-26 (Latest)添加了基于 OAuth 2.1 的全面授权框架用更灵活的 Streamable HTTP 传输取代了以前的 HTTP+SSE 传输增加了对 JSON-RPC 批处理的支持添加了全面的工具注释，以更好地描述工具行为，例如它是只读的还是破坏性的
MCP 官网：[https://modelcontextprotocol.io/quickstart/server](https://modelcontextprotocol.io/quickstart/server)

MCP (Model Context Protocol：模型上下文协议）其核心目标是建立类似USB-C的标准化**协议**，统一AI模型与外部资源的交互接口，实现“**一次集成，处处运行**”。

- 官方将MCP比作AI领域的USB-C接口。类比来看，不同的AI助手就像不同的电子设备，以前每个设备需要不同的数据线连不同的外设，而MCP提供了一个统一的细窄接口，让AI能够即插即用各种外设。例如，通过MCP，一个AI助手今天可以连U盘（数据库），明天插打印机（邮件系统），后天接显示器（报告生成）——接口都一样，只是功能不同。就像USB-C让我们少了无数转换头和线缆，MCP也让AI集成少了无数专有API和脚本。对于终端用户来说，这意味着AI助手将变得更加多才多艺且使用方便，因为背后复杂的连接都被这个看不见的“USB-C”标准屏蔽掉了。

![](./images/images/2321f2b6595a-202505282300113.jpeg)
没有 MCP 和有 MCP 的对比：
![](./images/images/859fdf25168f-202505282300329.jpeg)
### [MCP 核心架构](#mcp-核心架构)

MCP遵循客户端-服务器架构，包含以下几个核心部分：

- MCP 主机（MCP Hosts）：Host 是运行 AI 应用程序和 MCP 客户端的环境，是终端用户与 AI 系统交互的入口点。如 Claude Desktop、Cursor。

- MCP 客户端（MCP Clients）：Client 是 AI 应用程序内部的组件，负责与 MCP Server 通信，处理上下文、工具调用和结果展示。一般情况下 Client 是默认集成在 Host 中的。**Client 与 MCP Server 保持 1:1 的连接**。提供**两种原语**用于辅助 Server 完成复杂任务：

  - **根（Roots）**：定义了服务器可以在客户端文件系统中操作的边界，允许它们了解它们可以访问哪些目录和文件。

  - **采样（Sampling）**：允许服务器向客户端发起请求，要求客户端这侧的LLM执行操作。简单来说，这一机制运行服务器“反过来”调用客户端的模型，无需秘钥。

- MCP 服务器（MCP Servers）：Server 是提供工具、资源和功能供 AI 调用的外部服务。即是目前 MCP 插件的形态。为 MCP 客户端提供**三种原语**：

  - **工具（Tools）**：允许模型执行操作或检索信息的可执行函数

  - **资源（Resources）**：为模型提供额外上下文的结构化数据或内容

  - **提示（Prompts）**：指导语言模型交互的预定义模板或指令

![](./images/images/869a2aba9c42-202505282300031.gif)
### [MCP Server分类](#mcp-server分类)

尽量选择官方 Servers 和信任的第三方 Servers，使用社区 Servers 时要擦亮眼睛。

MCP Servers 的“应用中心”：

- [https://mcp.so/](https://mcp.so/)

- [https://glama.ai/mcp/servers](https://glama.ai/mcp/servers)

- [https://www.modelscope.cn/mcp](https://www.modelscope.cn/mcp)

![](./images/images/a977bc72dfcf-202505282300350.jpeg)
### [MCP 传输方式](#mcp-传输方式)

传输通信的生命周期：

1. Initialization：能力协商和协议版本协定

1. Operation：正常的协议通信

1. Shutdown：连接的优雅终止

#### [Standard Input/Output (stdio)](#standard-input-output-stdio)

协议版本：2024-11-05 开始支持

stdio 对于本地集成和命令行工具特别有用，通过本地进程间通信实现，**客户端以子进程形式启动服务器**，双方通过stdin/stdout交换JSON-RPC消息，每条消息以换行符分隔。

适用场景：本地工具集成、隐私数据处理、快速原型开发。

stdio 传输流程：

#### [Server-Sent Events (SSE)](#server-sent-events-sse)

协议版本：2024-11-05 开始支持，到2025-03-26 被抛弃

SSE 用HTTP POST请求实现客户端到服务器的通信

缺点：

- **不支持断线重连/恢复**：当 SSE 连接断开时，所有会话状态丢失，客户端必须重新建立连接并初始化整个会话。例如，正在执行的大型文档分析任务会因 WiFi 不稳定而完全中断，迫使用户重新开始整个过程。

- **服务器需维护长连接**：服务器必须为每个客户端维护一个长时间的 SSE 连接，大量并发用户会导致资源消耗剧增。当服务器需要重启或扩容时，所有连接都会中断，影响用户体验和系统可靠性。

- **服务器消息只能通过 SSE 传递**：即使是简单的请求-响应交互，服务器也必须通过 SSE 通道返回信息，造成不必要的复杂性和开销。对于某些环境（如云函数）不适合长时间保持 SSE 连接。

- **基础设施兼容性限制**：许多现有的 Web 基础设施如 CDN、负载均衡器、API 网关等可能不能正确处理长时间的 SSE 连接，企业防火墙可能会强制关闭超时连接，导致服务不可靠。

SSE 传输方式：

#### [Streamable HTTP](#streamable-http)

协议版本：2025-03-26 开始支持

Streamable HTTP取代了2024-11-05版本中的HTTP+SSE传输，此传输使用HTTP POST和GET请求。相比原有 HTTP+SSE 机制，Streamable HTTP 引入了几项关键改进：

- **统一 Endoint**：移除专门的 /sse 端点，所有通信通过单一端点（当前官方 sdk 实现为 /mcp）进行

- **按需流式传输**：服务器可灵活选择是返回普通 HTTP 响应还是升级为 SSE 流

- **会话标识**：引入会话 ID 机制，支持状态管理和恢复

- **灵活初始化**：客户端可通过空 GET 请求主动初始化 SSE 流

Streamable HTTP 传输流程：

### [对比](#对比)

#### [MCP vs Function Calling](#mcp-vs-function-calling)

有人说 MCP 和 Function Calling 并不是竞争关系而是互补的，但目前 Spring AI 的 Function Calling 相关 API 已经被 Deprecated 并标记为在下一个 release 将被删除了。

来自 A2A 官网的一句话：[https://google.github.io/A2A/#/topics/a2a_and_mcp](https://google.github.io/A2A/#/topics/a2a_and_mcp)

MCP 标准化了跨不同模型和框架的“Function Calling”

We already observe MCP standardizing ‘function calling’ across different models and frameworks.

![](./images/images/d5d881240285-202505282300375.jpeg)
#### [MCP vs A2A](#mcp-vs-a2a)

什么是Agent？

- 让大模型“代理/模拟”「人」的行为，使用某些“工具/功能”来完成某些“任务”的能力就可以定义为Agent。

- 从技术实现的角度对Agent进行定义：Agent = 大模型（LLM）+ 规划（Planning）+ 记忆（Memory）+ 工具使用（Tool Use）

A2A 官网：[https://google.github.io/A2A/#/](https://google.github.io/A2A/#/)

A2A协议与MCP是互补而不替代关系，A2A负责解决Agent间的通信问题，MCP解决的是Agent与工具间的通信问题。
![](./images/images/0a78bde82bf0-202505282300813.png)
A2A agents 也可以作为 MCP 中的 resources 使用：
![](./images/images/97de06d98e8f-202505282300361.png)
## [安全问题](#安全问题)

### [MCP的安全缺陷](#mcp的安全缺陷)

MCP安全问题参考：[https://mp.weixin.qq.com/s/x3N7uPV1sTRyGWPH0jnz7w](https://mp.weixin.qq.com/s/x3N7uPV1sTRyGWPH0jnz7w)

设计之初MCP协议主要是用于AI Agent调用本地工具或调用权威厂商提供的MCP服务，同时也没有过多考虑安全相关风险，2024年11月发布的初代MCP协议及主流MCP服务实现上仍然存在以下安全缺陷：

- **信息不对称**：AI模型能够看到工具描述的全部内容，包括隐藏在注释或特定标签中的细节，而在用户看到的AI Agent的前端界面出于简洁考虑往往只显示工具的基本功能描述，忽略了那些可能包含恶意指令的内容。

- **缺乏上下文隔离**：当AI Agent连接多个MCP服务器时，所有可用工具的描述信息都会被加载到当前的会话上下文中。这意味着来自恶意MCP服务器的工具描述可以影响来自可信MCP服务的工具行为。

- **大模型安全防护不足**：当前的大模型被训练为尽可能精确地理解并遵循给定的指令，包括MCP提供的工具描述。然而，模型往往缺乏针对恶意指令的批判性思维能力，特别是当这些指令被巧妙地伪装成工具的"必要前置条件"或"实现细节"时，同时即使开发者在Prompt中加入了安全防护相关指令，攻击者也可以通过各类层不出穷的越狱攻击手法绕过。

- **版本控制与更新机制不足**：MCP协议缺乏严格的版本控制和更新机制，使得所谓的"地毯式骗局"（Rug Pulls）成为可能。恶意的MCP服务可以在用户初次安装并启用后，在远程服务器上静默修改工具描述加入恶意指令，且MCP客户端无法及时感知并要求用户二次确认。

  - Rug Pulls 是一种加密货币和区块链生态中常见的欺诈行为，其核心特征是前期承诺高额收益吸引大量投资者，然后项目方在合约代码中植入后门，半路突然撤资或终止运营（卷铺盖跑路），导致投资者资金被卷走或代币价值归零。

- **授权认证机制不完善**：对于一些有敏感数据读取（如查DB、读文件）、敏感功能操作（如执行系统命令）功能的接口，MCP并没有在官方文档中明确强制要求开发者进行授权认证，这样可能导致部分暴露在公网上的MCP服务被入侵或未授权使用。

### [MCP 安全检查清单](#mcp-安全检查清单)

参考：[https://github.com/slowmist/MCP-Security-Checklist](https://github.com/slowmist/MCP-Security-Checklist)
![](./images/images/91a797cb6c19-202505282300574.png)
### [Prompt 注入](#prompt-注入)
![](./images/images/4786fa56dcb3-202505282300415.jpeg)
#### [Cursor-Prompt注入示例](#cursor-prompt注入示例)
![](./images/images/b96fd97af125-202505282300284.png)
#### [飞猪问一问-Prompt注入示例](#飞猪问一问-prompt注入示例)
![](./images/images/8195e5567cd1-202505282300433.jpeg)
#### [携程问道-Prompt注入示例](#携程问道-prompt注入示例)
![](./images/images/f7402df32c42-202505282300142.jpeg)
#### [大众点评AI搜-Prompt注入示例](#大众点评ai搜-prompt注入示例)
![](./images/images/bc846fa64176-202505282300149.jpeg)
#### [扣子空间-Prompt注入示例](#扣子空间-prompt注入示例)
![](./images/images/d7e70926a655-202505282300024.jpeg)
