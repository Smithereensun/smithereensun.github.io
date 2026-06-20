{

  "title": "规划与协调-TodoWrite",
  "has_date": true,
  "description": "这段代码引入了一个非常关键的概念：**“自我反思与状态管理”**。 之前的 Agent 只是单纯的“听指令 -&gt; 干活”，容易干着干着就忘了初衷，或者在复杂的任务中迷失方向。 就像是给 Agent 装了一个“记事本”和“监工”。 Java 实现代码 状态管理：TodoManager 类 为Ag",
  "tags": [
    "AI",
    "Agent"
  ],
  "source": "local-markdown-library",
  "source_path": "ai/agent/leaernclaudecode/s03 - 规划与协调-TodoWrite.md",
  "date": "2026-04-19"

}

这段代码引入了一个非常关键的概念：**“自我反思与状态管理”**。

之前的 Agent 只是单纯的“听指令 -&gt; 干活”，容易干着干着就忘了初衷，或者在复杂的任务中迷失方向。`TodoManager` 就像是给 Agent 装了一个“记事本”和“监工”。

## [Java 实现代码](#java-实现代码)

## [状态管理：TodoManager 类](#状态管理-todomanager-类)

为Agent引入**长期记忆和工作进度追踪**能力，让Agent能"记住"自己的任务列表和工作状态。

- **状态持久化**：Agent有了"记忆"，不再是完全无状态的

- **结构化表示**：用面向对象的方式管理任务状态

- **业务约束**：通过校验规则确保状态一致性

- **可视化输出**：为LLM提供人类可读的进度展示

## [Todo工具集成](#todo工具集成)

- **状态操作作为工具**：将状态管理抽象为工具调用

- **双向通信**：LLM可以通过工具更新状态，也能获取状态

- **统一接口**：与其他工具使用相同的调用模式

## [监工逻辑（Nag Reminder）](#监工逻辑-nag-reminder)

- **防遗忘机制**：LLM可能会忘记更新状态，需要外部提醒

- **渐进式提醒**：容忍短期遗忘，超过阈值再干预

- **结构化提示**：使用特殊标签`&lt;reminder&gt;`，让LLM识别这是系统提示

- **优先级**：插入到结果列表最前面，确保LLM先看到

## [架构演进与价值](#架构演进与价值)

**从 AgentWithTools 到 AgentWithTodo 的升级**：
维度AgentWithToolsAgentWithTodo状态管理无状态有状态（TodoManager）进度追踪不支持支持任务进度管理长期记忆不支持支持任务列表记忆监督机制无有监工提醒任务管理工具级项目级
