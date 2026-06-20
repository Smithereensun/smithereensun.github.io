{

  "title": "AI应用框架常见面试题",
  "has_date": false,
  "description": "LangChain 什么是 LangChain？ LangChain 是一个开源框架，专为快速构建复杂的大语言模型应用而设计。它通过模块化组件(Agents、Memor、Tools 等)和预制工具链，解决了传统LLM开发中的三大痛点 上下文管理：通过 Memory 组件(如对话历史缓存、实体关系跟踪",
  "tags": [
    "面试",
    "AI"
  ],
  "source": "local-markdown-library",
  "source_path": "interview/ai/framework - AI应用框架常见面试题.md"

}

---

## [LangChain](#langchain)

### [什么是 LangChain？](#什么是-langchain)

LangChain 是一个开源框架，专为快速构建复杂的大语言模型应用而设计。它通过模块化组件(Agents、Memor、Tools 等)和预制工具链，解决了传统LLM开发中的三大痛点

1. 上下文管理：通过 Memory 组件(如对话历史缓存、实体关系跟踪)实现长对话连贯性,

1. 多工具协同：支持动态调用外部API、数据库、搜索引擎等工具(如 GooglesearchTool)，例如在回答“2025年全球GDP排名”时自动触发实时数据查询。

1. 复杂任务编排：通过 chains(链)和 Agents(代理)将多个LLM调用和工具操作组合成工作流，例如“分析财报一提取关键指标一生成可视化建议”的端到端流程。

### [LangChain 的核心组件有哪些？](#langchain-的核心组件有哪些)

LangChain 是一个专为大语言模型(LLM)应用开发而设计的框架，其核心组件包括：

1. Models(模型)：支持多种语言模型，如 OpenAl、Anthropic、Mistral、Llama等，提供统一的接口，便于在不同模型之间切换。

1. promotTemplates《提示词模板)：允许用户创建动态提示司，提高模型的泛化能力。通过模板化的方式，可以根据不同的输入生成相应的提示词，从而引导模型生成更准确的输出。

1. Memory(记忆)：用于存储对话的上下文信息，支持短期记忆和长期记忆，短期记忆通常用于当前会话的上下文，而长期记忆则结合向量数据库，持久化存储重要信息，便于在未来的对话中调用。

1. Chains(链式调用)：将多个外理步骤围联起来，形成一个处理流程。支持 Simple Chains(单步任务)和 Sequential chains(多步任务)，使得复杂任务的外理更加模块化和可复用。

1. Agents(智能体)：通过 ReAct 框架，Agent 可以根据用户的输入动态选择合适的工具来完成任务，实现更灵活的任务处理。

1. Tools(工具)：提供访问外部资源的能力，如 API、Google 搜索、SQL 数据库等，扩展了模型的功能，使其能够处理更复杂的任务,。

### [LangChain核心架构是什么样的](#langchain核心架构是什么样的)

LangChain 的核心架构由四大关键模块组成：LangChain Libraries、LangChain Templates、LangServe 和 LangSmith。它们各自承担不同的角色，共同构建了一个完整的 LLM 应用开发、部署与监控的闭环体系

- LangChain Libraries：这是整个框架的基础，包含多个子模块:

  - langchain-core：提供核心抽象，如模型接口、工具、向量存储等，设计轻量，便于扩展。

  - langchain：构建链(Chains)和代理(Agents)的主要模块，处理复杂的业务逻辑和外部 API 交互。

  - langchain-community：整合社区贡献的第三方工县和集成，如模型操作、提示词模板、文件解析、向量化等。

- LangChain Templates：提供一系列易于部署的参考架构，适用于各种任务。这些模板预配置了常用的集成，便于快速上手和定制。

- LangServe：用于将 LangChain 构建的链部署为 REST API 的库，集成了 FastAPI，支持流式、批量处理等功能，方便将应用推向生产环境,

- LangSmith：开发者平台，提供调试、测试、评估和监控功能帮助开发者优化和部署基于LanaChain 构建的应用

### [什么是 LangChain Agent?](#什么是-langchain-agent)

langchainAgent 是 langchain 框架中的一个核心组件，它的作用是利用大语言机型 (LLM)的推理能力，根据用户的输入动态地选择并调用合适的工具或链 (Chin)，以完成复杂的任务，与传统的链式调用不同，Agent不依赖于预定义的流程，而是能够根据实际情况灵活地决策和执行操作。

简单来说，LangChain Agent 就像是一个智能的指挥官，接收用户的指令后，分析任务需求，制定执行计划，选择合适的工具或方法，并根据执行结果进行调整，直到完成任务。

### [什么是 LangChain model?](#什么是-langchain-model)

langchain中的Model模块，主要是为了解决和各种语言模型(LLM)打交道时的接口统一问题，它提供了一套标准化的方式，让我们可以用司样的方式去调用不同厂商的模型，比加 OpenAl、Anthropic、Huging face等，这就像是给各种不同品牌的家电配上了通用的插头，我们不需要为每个品牌单独准备一个插座。

具体来说，LangChain 的 Model 模块包括以下几个核心部分：

- LLM 和 ChatModel 接口：LLM 接口适用于传统的文本输入输出模型，而 ChatModel 接口则专为对话式模型设计，支持多轮对话的上下文管理。

- Prompt 模板系统：提供了一种灵活的方式来构建和管理提示词，支持变量替换、条件逻辑等功能，方便生成动态的输入内容。

- 输出解析器(Output Parsers)：用于将模型的原始输出转换为结构化的数据格式，比如 JSON、列表等，便于后续处理。

- 同步与异步支持：无论我们是需要同步调用还是异步处理，LangChain 都提供了相应的支持，满足不同的应用场景需求。

- 批量处理与流式输出：支持一次性处理多个输入，以及在生成过程中实时获取输出，提升了处理效率和用户体验。

### [LlamaIndex 如何与 LangChain 结合？](#llamaindex-如何与-langchain-结合)

Lamalndex和 langchain 的结合，主要是为了构建更强大、更灵活的 RAG系统，LlamaIndex 擅长数据的索引和检索，而langchain 提供了丰富的链式调用、代理和工具集成能力，通过将LlamaIndex 的检索能力作为 LangChain 的工具(Tool)进行调用，可以实现复杂的多步骤推理和动态数据访问。

### [什么是 LangGraph ？](#什么是-langgraph)

langGraph是Langchain 生态下的一个基于图结构的开源框架，专为构建状态化、多代理协同的复杂AI应用而设计。它通过将任务流程建模为有向无环图(DAG)结构对各节点 (Agent、工具、状态)及其交互进行精细控制。

它可以：

- 通过拖拽界面设计工作流，非技术人员也能快速搭建复杂逻辑(如企业级客服系统)

- 可以在关键节点(如财务审批、合规审核)插入人工确认环节，避免AI决策风险。

- 实时展示模型生成过程(如逐句输出报告内容)，提升用户信任度。

### [LangGraph 编排的原理是什么？](#langgraph-编排的原理是什么)

LangGraph 的编排原理是通过图结构将复杂的 AI 任务分解为可编排的节点(如代理、工具、流程终点)，并通过状态流转和条件边实现动态流程控制，核心包含三个要素：

- 节点 (Node)：代表独立处理单元(如 Agent 调用 LLM、Tool执行工具函数)，每个节点接收状态并返回更新后的状态

- 边(Edge)：定义节点间的流转路径，支持条件分支(如根据用户输入选择不同处理逻辑)和循环(如需要多次修正结果)

- 状态(State)：、贯穿整个流程的上下文数据(如对话历史、中间结果)，驱动节点间的动态交互

简单来说 LangGraph 像“流程图引擎”，我们通过画图(定义节点和边)描述任务逻辑，框架自动根据状态流转执行节点，支持复杂的多 Agent 协作和动态决策,

### [LangChain 和 LangGraph 有什么区别？](#langchain-和-langgraph-有什么区别)

LanaChain 是基于链式结构(Chain)，适合线性任务(如文档问答、简单客服)，通过预定义步骤顺序执行，类似工厂流水线

LangGraph：基于图结构(Graph)，支持循环、分支和动态决策，适合需要多角色协作、状态跟踪的复杂任务(如临床试验审批、多智能体投资分析)

简单来说 LangChain 更像是一个“模块化 AI 应用框架”，用于拼接模型、工具、记忆等组件。而LangGraph 是专注于流程控制和任务编排的“有状态执行图框架”

在我们实际开发中，可根据任务复杂度选择：简单任务用LangChnain，复杂任务用langGraph，超复杂场景结合两者，如用Langchnain 处理基础链，LangGraph管理全局流程(要注意哈，两者并非替代关系，而是互补! langGraph可作为 LangChain 的扩展，在需要动态控制流和状态管理的场景中提升应用的灵活性和可靠性)。

### [什么是 Manus？说说你对它的了解](#什么是-manus-说说你对它的了解)

Manus是咱们由中国团队 [Monica.im](http://Monica.im) 于2025年3月推出的 全球首款通用型AI智能体，其核心突破在于能够独立思考、规划并执行复杂任务，直接交付完整成果(如股票分析报告、简历筛选结果)，而非仅提供对话式建议。

它通过一个 中央 模块、将用户的高层指令拆解为多个子午务，再由不同的内部智能体(Agent)或工具执行，形成端到端的自动化执行流程，底层还是调用大模型例如 Glaude、Qwen等来实现规划与决策。

### [Computer Use 是什么？说说它的原理](#computer-use-是什么-说说它的原理)

Computer Use 是 Anthropic 在 Claude 3.5 Sonnet 中推出的 AI 操作计算机的能力，允许 AI 直接通过 模拟鼠标点击键盘输入 等方式与操作系统和软件交互，实现从“文字对话”到“实际操作”的跨越
 核心原理如下：

1. API驱动的自动化交互：通过 操作系统级 API(如 Windows AP、macOs 系统调用)，将自然语言指令转化为计算机可执行的操作(如“打开 Chrome 搜索一 启动浏览器并输入关键词)。

1. 多智能体协作：内置 任务规划代理(分解任务)、工具调用代理(执行操作)、验证代理(校验结果)，形成流水线式处理(如“生成报告”一 拆分为“数据获取”“图表绘制”“格式校验”)。

1. 视觉与语义结合：利用 OCR 技术 识别屏幕内容，结合 语义理解 定位目标(如“点击页面右上角的“登录”按钮”一 分析页面结构并模拟点击)

### [解释LangChain框架中的Chain和Agent概念，并举例说明各自的应用场景](#解释langchain框架中的chain和agent概念-并举例说明各自的应用场景)

LangChain框架中的Chain和Agent是两个核心组件，它们的主要区别在于执行方式:

- Chain(链)：Chain是一个预定义的固定操作序列，按照既定的顺序执行任务。类似于一条生产线，每个步骤都是预先设定好的，按部就班地执行。

- Agent(代理)：Agent则是一个能够动态决策的智能体，它可以根据当前情况自主选择使用什么工具、采取什么行动来完成任务。Agent使用语言模型作为推理引擎，能够实时判断和选择最优的行动序列。

### [使用LangChain实现RAG系统时，如何处理PDF文档中的表格数据召回问题？](#使用langchain实现rag系统时-如何处理pdf文档中的表格数据召回问题)

处理 PDF 文档中的表格数据召回问题，需要采用多步骤处理策略：

- 精确提取：使用专业的 PDF 解析工具(如 [Unstructured.io](http://Unstructured.io))提取表格数据，确保表格结构完整性。

- 上下文增强，为每个表格生成上下文描述，包含:

  - 表格主题和用途

  - 关键列名解释

  - 数据单位说明

  - 与文档其他部分的关联

- 格式标准化：将表格转换为统一的 Markdown 格式，提升向量化效果和模型理解能力。

- 统一嵌入：将上下文描述和标准化后的表格合并为"表格块"，优化向量数据库存储和检索效果

## [SpringAI](#springai)

### [什么是 Spring AI 框架？它有哪些核心特性？](#什么是-spring-ai-框架-它有哪些核心特性)

Spring AI 是一个基于 Sprng生态系统的 AI 应用开发框架，主要目标是简化AI功能与Spring应用的集成，它通过提供统一的 API 和抽象，让 Java 开发者可以更便捷地接入和使用各种 AI 大模型及相关技术，忽路底层实现的差异。通过官网，我们可以了解到 Spring Al 框架有以下核心特性：

- 跨 AI 供应商的可移植 API 支持：为聊天、文本转图像和嵌入模型提供了统一的 API，支持同步和流式调用，支持访问特定模型的功能

- 广泛的 AI 模型供应商支持：支持包括 OpenAI、微软 Azure、Anthropic、Google、Ollama 在内的主流 AI 模型供应商。

- 结构化输出：能够将 AI模型的输出自动映射到 POJO，方便在 Java 应用中处理。

- 向量数据库集成：支持与多种主流向量数据库的集成，还提供了跨向量存储的可移植 API

- 工具/函数调用 (Tool/Function Calling)：支持模型请求执行客户端定义的工具和函数，扩展模型的能力

- ETL框架：提供了文档抽取、转换和加载(ETL)的组件，用于数据工程和 RAG 知识库的构建。

- Spring Boot 自动配置与启动器：为 AI 模型和向量存储提供了自动配置和 Starter 依赖，简化项目配置

- ChatClient API：提供了类似于 WebClient 和 RestClient 的流式AP|，提高与 AI 模型交互的便捷性。

- Advisors API： 一种拦截器机制，封装了常见的 AI 功能，如对话记忆、RAG 等，还支持自定义，可以在调用 AI 前后执行额外操作

这些特性共同构成了 Spring Al 框架的基础,提升 AI 应用的开发效率和可维护性

### [你在 AI 智能体项目中如何利用 Spring AI 开发应用？用到了哪些特性？](#你在-ai-智能体项目中如何利用-spring-ai-开发应用-用到了哪些特性)

- 大模型接入与调用：使用 spring-ai-alibaba-starter 和 spring-ai-ollama-spring-boot-starter 简化大模型的配置和集成。通过 Spring Al 的 chatmodel 和更高级的 chatclient API 与 Al 大模型交互，实现对话功能。

- Advisors：

  - 利用 MessagechatMemoryAdvisor 实现了多轮对话中的上下文记忆功能。

  - 为了增强应用的可观测性，我还自定义了Advisor，例如用于记录 AI 请求和响应日志的MyLoggerAdvisor，以及用于尝试提高模型推理能力的 ReReadingAdvisor。

- 对话记忆：

  - 项目初期使用了基于内存的 InMemorychatMemory

  - 为了实现对话记忆的持久化，我自定义了 FileBasedChatmemory，并使用 Kryo 序列化库解决了 message 对象层级复杂难以直接序列化的问题

- 结构化输出：通过 Spring Al 的结构化输出转换器，我把 AI 模型的文本输出直接转换为Java 对象，方便后端处理和使用。

- Prompt 模板：利用promptTemplate 管理和动态生成提示词，比如使用占位符替换变量、从外部文件加载复杂的提示词模板，提高了提示词的可维护性和灵活性。

- RAG (检索增强生成):

  - 文档EL：使用了 SpningAl 的 ETL Pipeine 组件，如 MarkdownDocumentReader 加载本地Markdowm知识库文档、TokenTextspliter 进行文本分割、keywordMetadatatEnricher 自动为文档添加关键词元数据。

  - 向量存储：集成 simplevectorstore 和 pgvectorstore 用于存储和检索文档向量，在集成pgvectorstore 时，我还解决了多个Embedingpodel Bean 冲突的问题。

  - 检索与增强：使用 QuestionAnswernAdvisor 和更灵活的 RetrievalAugmentationAdvisor 实现 RAG 流程，后者还结合了 VectorstoreDocumentRetriever 和 ContextualQuenyAugmenter 等组件进行查询优化和空上下文处理，还实践了查询重写(RewriteQueryTransformer)等预检索优化技术。

- 工具调用(Tool Calling)：

  - 通过 @Rool 和 @Toolparam 注解定义了多种外部工具，如文件操作、联网搜索、PDF生成等，并使用 chatclient 的 too1s()方法将这些工具注册给 AI 模型，让AI 能够调用这些工具完成特定任务。

  - 在构建智能体时，我手动控制了工具的执行流程(ReAct模式)，通过 DashScopeChatOptions 禁用 Sping Al 内部的自动工具执行，更方便、更精细地管理思考-行动循环。

- MCP(模型上下文协议)集成：

  - MCP客户端：使用spring-ai-mcp-client-spring-boot-starter，配置 stdio 和 SSE 连接方式来调用外部MCP服务，通过 Toolcallbackprovider 将 MCP服务提供的工具无缝集成到chatclient的工具调用机制中。

  - MCP服务端：基于 spring-ai-mcp-server-webmvc-spring-boot-starter 开发了自定义的图片搜索 MCP 服务，使用 @Tolls 注解暴露工具，然后通过 Toolcallbackprovider Bean 进行注册。

我综合使用了 Spring Al 的这些特性，大大简化了开发过程。

### [如何实现程序和 AI 大模型的集成？有哪些方式？](#如何实现程序和-ai-大模型的集成-有哪些方式)
![](/imported/markdown/undated-markdown-ef122b89-ai应用框架常见面试题/images/32bd7102d952-202508031752056.png)
最终，在项目中我主要使用的是 Spring Al框架接入:

- 它属于 Spring 生态，更主流

- 利用官方提供的 Spring Boot Starter 可以轻松整合各种第三方依赖(比如向量数据库和 MCP)

- 简单易用，满足大多数 AI项目的开发需求

### [如何实现 AI 多轮对话功能？如何解决对话记忆持久化问题？](#如何实现-ai-多轮对话功能-如何解决对话记忆持久化问题)

多轮对话功能的关键在于让AI具备“记亿能力”，即能够记住与用户之前的对话内容并保持上下文连贯。

在我做的AI项目中，我使用了 Sping AI 框架提供的对话记忆(Chat Memory) 和 Advisor 特性来实现这个功能。

具体实现操作上来说，我主要通过构造 chatclient 来实现功能更丰富、更灵活的AI对话。chatclient支持使用Advisors，可以理解为一系列可插拔的拦载器，在调用 Al 前后执行额外操作，其中MessageChatMemoryAdvisor 就是实现多轮对话的关键Advisor，它的作用是从对话记忆中检索历史对话，并将对话历史作为消息集合添加到当前的提示词中，实现让 AI 模型能够“记住”之前的交流。

MessageChatMemoryAdvisor 依赖于 chatmemory 接口的实现来存取对话历史。 chatmemory 接口中定义了保存消息、查询消息和清空历史的方法。默认情况下会使用 InMemoryChatMemory 实现，从这个类名可以看出对话记忆仅存在于内存中，一旦服务重启，记忆就会丢失。为了解决这个问题，需要将对话记忆持久化。Sping AI 提供了多种特久化方案，例如 JdbChatMemory 可以将对话保存在关系型数据库中，但是在本项目中，考虑到 spring-ai-starter-model-chat-memory-jdbc 依赖版本较少且缺乏相关介绍，我选择了自定义实现chatMemory 接口的方式：

1. 开发一个 FileBasedchatMemory类，它实现了 chatMemory 接囗。

1. 使用高性能的 Kyro 序列化库将对话消息(Message 对象及其子类)序列化后保存到本地文件中，读取时再进行反序列化。选择 Kyro 是因为 Message 接口有多种实现，结构不一，且没有无参构造和 Serializable 接口，普通的JSON 序列化难以处理。

通过这种方式，我将对话的上下文信息持久化到了指定的文件目录，解决了内存记忆丢失的问题.

### [什么是结构化输出？Spring AI 是怎么实现结构化输出的？](#什么是结构化输出-spring-ai-是怎么实现结构化输出的)

结构化翰出是指将大语言模型返回的自由文本输出转换为预定义的数据格式，像JSON、XML 或特定的 Java 类(POJO)，对于需要可靠解析 AI 输出值并进行后续处理的需求来说非常重要Spring Al 通过 StructuredOutputConverter 机制实现结构化输出，其工作流程可以分为调用前和调用后两个阶段：

- 调用前：StructuredOutputConverter 实现了 FormatProvider 接口。FormatProvider 的作用是提供特定的格式指令给 AI 模型，这些指令会附加到用户的提示词后面，明确告诉模型应该生成何种结构的输出。举个例子。它可能会包含类例"Your esponse should be in JSON format. The data structure for the JSON should match this Java claas:com.example.Mybean” 这样的描述，并可能带一个 JSON Schema 定义，引导模型生成符合指定格式的响应。

- 调用后：StructuredOutputConverter 同时也实现了 `Converter&lt;string, T&gt;` 接口。这个Converter 负责将大模型返回的文本输出(通常是JSON 字符串)转换为开发者指定的目标类型T(比如一个Java Bean 对象、Map 或 List)。Spring Al提供了多种内置的转换器实现，如Beanoutputconverter(用于转换为JavaBean，内部基于ObjectMapper)、MapOutputconverter和ListOutputconverter 。

![](/imported/markdown/undated-markdown-ef122b89-ai应用框架常见面试题/images/c34e5db138c1-202508031806120.png)
也就是说，Sping Al 的结构化输出转换器首先通过修改提示词来规定模型按特定格式生成文本，然后将该文本转换为Java对象。使用chatclient的`.entity(Myclass.class)`方法时，框架会自动处理这个过程，将模型的 JSON 输出映射到 Myclass 的实例。但是，这只是“尽最大努力” 的转换，模型并不保证一定能严格按要求返回结构化数据！

### [什么是 Re-Reading？如何基于 Spring AI 实现 Re-Reading Advisor？](#什么是-re-reading-如何基于-spring-ai-实现-re-reading-advisor)

Re-Reading(重读,，也称为 Re2，是种通过让大语言模型重新阅读问题来提高其推理能力的技术，核心思想是，对于复杂问题，重复阅读和审视问题有助于模型更好地理解题意和约束，从而生成更准确、更深入的回答，有文献研究证明这是有一定效果的。不过，这种方法会因为重复处理输入导致成本加倍，所以在面向C端开放的应用中需要谨慎使用。

在 Spring Al 中，可以通过自定义 Advisor 来实现 Re-Reading 功能：

- 创建自定义 Advisor 类：该类需要同时实现 CallAroundAdvisor(用于同步请求)和 StreamAroundAdvisor(用于流式请求)接口，让该类更通用(在 Spring Al 1.0 版本中，上述两个接口需要更改为 CallAdvisor 和 StreamAdvisor )

- 修改用户提示词：在Advisor的前置处理逻辑中(例如 aroundCall或aroundStream 方法调用之前)，对用户的原始输入文本进行改写，改写的格式通常是将原始输入重复一遍，并用明确的指令引导模型重新阅读，通过看源码能够看到提示词，其中，{Input_query} 是用户原始的提问内容

- 传递给模型：将改写后的提示词传递给大语言模型进行处理。

### [什么是查询重写？它有什么作用？如何基于 Spring AI 实现查询重写？](#什么是查询重写-它有什么作用-如何基于-spring-ai-实现查询重写)

查询重写是 RAG 预检索阶段的优化手段。它利用 AI 大模型对用户原始输入的查询进行改写润色，然后生成一个对后续文档检索更有效、更精确的新查询。

查询重写可以提高检索的准确性和相关性，尤其是当用户查询较为模糊、口语化、不完整，或者和知识库语言风格不一致时，通过重写可以将查询变得更规范、更详细，更容易在向量数据库中匹配到最相关的文档,。

Sping AI 主要通过 QueryTransformer 接口及其实现类来支持查询重写，比如 RewriteQueryTransformer，可以将简单查询改写得更具体更专业；而CompressionQueryTransformer 则专注于处理多轮对话场景，将对话历史和当前问题压缩成一个独立的、包含完整上下文的新查询，使用时，需要为这些转换器配置一个 chatclient 或 chatrodel，然后调用其 transform 方法传入原始查询即可得到重写后的查询。
![](/imported/markdown/undated-markdown-ef122b89-ai应用框架常见面试题/images/29ad86334d29-202507271810144.png)
### [什么是上下文查询增强？它有什么作用？如何基于 Spring AI 实现上下文查询增强来处理无关问题？](#什么是上下文查询增强-它有什么作用-如何基于-spring-ai-实现上下文查询增强来处理无关问题)

上下文查询增湿是 RAG流程中的一个核心环节，指的是把用户的原始查询与从知识库中检索到的相关文档进行结合，形成一个信息更丰富的增强提示，然后将这个增强提示提供给AI，让模型能基于这些特定知识生成回答。主要作用是为大模型提供必要的、实时的外部知识，这样 AI 的回答就不仅仅依赖于其预训练的通用知识，提高答案的准确性、相关性和时效性。

Spring Al 的 RetrievalAugmentationAdvisor 内部使用 ContextualQueryAugmenter 来实现上下文查询增强，当处理用户提出的无关问题时，ContextualQueryAugmenter 提供了空上下文处理机制。
![](/imported/markdown/undated-markdown-ef122b89-ai应用框架常见面试题/images/5dc75ea6160f-202507271813458.png)
我们可以配置 ContextualQueryAugmenter 的 allowEmptycontext(false)，检索不到相关文档时，系统会使用这个自定义模板来指示大模型如何回应。

### [什么是 Spring AI 提出的模块化 RAG 架构？预检索、检索和后检索阶段各自负责什么？](#什么是-spring-ai-提出的模块化-rag-架构-预检索、检索和后检索阶段各自负责什么)

Spring AI 提出的模块化 RAG架构是将整个检索增强生成过程分解为 *预检索、检索、检索后* 三个核心阶段，每个阶段包含可配置的组件，以提升大模型响应的准确件和灵活件。

1. 预检索阶段(Pre-Retrieval)：

  - 职责：接收用户的原始查询，并对其进行优化和转换，生成更适合后续检索的查询版本。

  - 组件：包括各种 QueryTransformer，如 RewriteQueryTransformer(改写查询使其更清晰)、TranslationQueryTransformer(翻译查询)、CompressionQueryTransformer(在多轮对话中压缩历史和当前问题)、以及MultiQueryTransformer(将单查询扩展为多查询，提高召回)。

1. 检索阶段(Retrieval)：

  - 职责：使用预检索阶段优化后的查询，从知识库中搜索并召回最相关的文档片段。

  - 组件：核心是 DocumentRetriever(如 VectorStoreDocumentRetriever)，它负责执行相似件搜索并根据元数据过滤结果、如果涉及多源检索，还可能用到 DocumentJoiner 来合并结果

1. 检索后阶段(Post-Retrieval)：

  - 职责：对检索到的文档集进行进一步处理和优化，筛选出最适合提供给大模型的上下文，可以解决上下文丢失问题、上下文长度限制，并减少冗余内容。

  - 组件：可能包括文档重排序、无关文档移除、文档内容压缩或摘要等。Spring Al提供了 DocumentProcessor API 来支持自定义的后处理逻辑，但目前并不成熟。

### [什么是工具调用 Tool Calling？如何利用 Spring AI 实现工具调用？](#什么是工具调用-tool-calling-如何利用-spring-ai-实现工具调用)

工具调用 (Tool Caling)，也常被称为 Function Calling，是一种允许 AI 大模型在对话过程中，根据需要请求执行外部工具来完成特定任务的机制，AI 模型本身可能不具备实时查询天气、操作数据库或访问特定 API 的能力，通过工具调用，它可以识别出什么时候需要这些外部能力，并生成一个包含工具名称和所需参数的请求。应用程序接收到这个请求后，实际执行相应的工具，并将执行结果返回给 AI 模型，模型再基于这个结果继续对话或生成最终答案。

注意，真正执行工具的是我们的应用程序，而非 AI服务器本身。Spring Al极大地简化了工具调用的实现：
![](/imported/markdown/undated-markdown-ef122b89-ai应用框架常见面试题/images/059387b56b18-202508031629452.png)

1. 定义工具：通常使用注解方式，在一个Java 类中，将希望作为工具的方法标记上 @Tool 注解。方法的参数可以使用 @ToolParam 注解来提供描述和指定是否必需。Spring Al 支持多种 Java 类型作为参数和返回值，但返回值需要可序列化。

1. 注册与使用工具：

  - 按需使用：在构建 chatclient 请求时，通过 `.tools()` 方法直接传入工具类的实例。

  - 全局使用：在构建chatclient 时，通过 `.defaultTools()` 注册默认工具，这些工具对该 chatclient 发起的所有对话都可用。

  - 集中注册：可以创建一个配置类，使用@Bean方法将所有工具实例化并通过 `ToolCallbacks.from()` 统一注册为一个 `ToolCallback[]` 数组，方便管理和注入。

1. 调用流程：当使用配置了工具的 chatclient 进行对话时，如果 AI 模型判断需要使用某个工具，Spring Al 框架会自动执行以下步骤，无需开发者关心：

  - 解析 AI 模型返回的工具调用请求(包含工具名和参数)。

  - 根据工具名找到对应的 Java 方法并执行。

  - 将工具执行的结果转换并返回给 AI模型。

  - AI模型根据工具结果生成最终回复
