# TIMRUN: Efficient Engine for Long-horizon Reasoning

<div align="center">

<a href="https://www.subconscious.dev/" style="text-decoration: none;">
  <img src="assets/imgs/logo.png" alt="Subconscious Systems" width="80" height="80" style="border-radius: 12px; margin-bottom: 8px;">
</a>

<h3 style="margin: 8px 0;">
  <a href="https://www.subconscious.dev/" style="text-decoration: none; color: inherit;">
    Try on Subconscious Systems
  </a>
  <a href="https://www.subconscious.dev/" style="text-decoration: none; color: #007acc; font-size: 0.8em; margin-left: 4px;">
    [link]
  </a>
</h3>

[![Paper](https://img.shields.io/badge/paper-arXiv-red.svg)](https://arxiv.org/pdf/2507.16784)
[![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Models-yellow)](https://huggingface.co/SubconsciousDev/TIM-8b-preview)

*Enabling efficient multi-hop reasoning and tool use for extended problem-solving*

</div>

## 🚀 Overview

**TIMRUN** (TIM Runtime) is a high-performance inference engine that orchestrates the **TIM (Thread Inference Model)** for unprecedented long-horizon reasoning capabilities. TIMRUN manages the entire inference pipeline, using TIM to predict next tokens while performing intelligent structure checks to extract tool calls and identify prunable subtasks. This enables efficient end-to-end multi-hop tool use and makes complex problem-solving tasks more scalable.

### Key Features

- 🔗 **Multi-hop Reasoning**: Chain complex reasoning steps across extended contexts
- 🛠️ **End-to-End Tool Integration**: Seamlessly incorporate external tools and APIs
- ⚡ **Optimized Inference**: Efficient sparse attention mechanisms for long sequences with intelligent KV cache pruning
- 🎯 **Long-horizon Planning**: Handle tasks requiring extended planning and execution
- 🔄 **Iterative Refinement**: Continuously improve solutions through feedback loops
- 🧠 **Intelligent Orchestration**: Structure checks for tool calls and subtask pruning during inference

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────────────────────────────┐
│   Input Query   │───▶│              TIMRUN Engine              │
│                 │    │                                         │
└─────────────────┘    │  ┌─────────────────┐                    │
                       │  │   TIM Model     │                    │
                       │  │                 │                    │
                       │  │  • Sparse Attn  │                    │
                       │  │  • Multi-hop    │                    │
                       │  │  • Token Pred   │                    │
                       │  └─────────────────┘                    │
                       │           │                             │
                       │           ▼                             │
                       │  ┌─────────────────┐                    │
                       │  │ Structure Check │                    │
                       │  │                 │                    │
                       │  │ • Tool Calls    │ ----------         │
                       │  │ • Prunable      │          │         │
                       │  │   Subtasks      │          │         │
                       │  └─────────────────┘          │         │
                       │           │                   │         │
                       │           ▼                   ▼         │
┌─────────────────┐    │  ┌─────────────────┐    ┌─────────────┐ │
│   Tool Usage    │◀───┼──│  Tool Execution │    │ KV Cache    │ │
│                 │    │  │                 │    │ Pruning     │ │
│  • External APIs│    │  │ • Call Tools    │    │             │ │
│  • Tool Calls   │    │  │ • Encode        │    │ • Memory    │ │
│  • Data Sources │    │  │   Response      │    │   Mgmt      │ │
└─────────────────┘    │  └─────────────────┘    └─────────────┘ │
                       │           │                      │      │
                       │           ▼                      ▼      │
                       │  ┌─────────────────────────────────────┐│
                       │  │         Continue Decoding           ││
                       │  │      (with updated context)         ││
                       │  └─────────────────────────────────────┘│
                       └─────────────────────────────────────────┘
                                        │
                                        ▼
                               ┌─────────────────┐
                               │   Final Result  │
                               │                 │
                               └─────────────────┘
```

## 🚀 Quick Start

### OpenAI Compatible API

```python
client = OpenAI(
    base_url = "https://api.subconscious.dev",
    api_key = # get API KEY from https://subconscious.dev
)
```

### Reasoning with Multi-hop Search Tool Calls

```python
resp = client.chat.completions.create(
    model = "tim-large",
    messages = [
        {
            'role': 'user',
            'content': 'find 10 most influencial research papers in dog walking.'
        }
    ],
    top_p = 0.95,
    max_completion_tokens = 10000,
    temperature = 0.6,
    tools = [
        {
            "type": "function",
            "name": "SearchTool",
            "description": "a general search engine returns title, url, and desciription of 10 webpages",
            "url": URL_TO_TOOL, # the server url of your own tool
            "method": "POST",
            "timeout": 10,
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "A natural language query for the search engine."
                    }
                },
                "required": [
                    "query"
                ],
                "additionalProperties": False
            }
        }
    ]
    stream = False # if true, same as OpenAI's streaming
)
print(json.loads(resp.choices[0].message.content)['answer'])
```

## 🛠️ Available Tools

coming soon

## 📊 Performance

### Optimization Features

- **Selective Working Memory**: 50% reduction in memory usage for long sequences
- **Tool Caching**: 30% faster repeated tool calls
- **Batched Processing**: Multi-threaded tool execution when possible
- **Memory Management**: Efficient handling of large reasoning chains

## 📚 Documentation

- [Getting Started Guide](https://docs.subconscious.dev/quickstart)
- [Available Models](https://docs.subconscious.dev/platform/models)
- [Tool Development](https://docs.subconscious.dev/platform/tools)
- [API Reference](https://docs.subconscious.dev/platform/using-subconscious)

## 🔬 Research & Papers

If you use found our work helpful in your research, please cite:

```bibtex
@article{tim-timrun,
  title={Beyond Context Limits: Subconscious Threads for Long-Horizon Reasoning},
  author={Hongyin Luo, Nathaniel Morgan, Tina Li, Derek Zhao, Ai Vy Ngo, Philip Schroeder, Lijie Yang, Assaf Ben-Kish, Jack O'Brien, James Glass},
  journal={arXiv preprint arXiv:2507.16784},
  year={2024}
}
```

## 📄 License

This TIM-8b-preview model is licensed under the MIT License.

## 📞 Support

- 📧 Email: hongyin OR jack AT subconscious DOT dev
- 🐛 Issues: [GitHub Issues](https://github.com/subconscious-systems/TIMRUN/issues)
- 📖 Documentation: [docs.subconscious.dev/](https://docs.subconscious.dev/)

---

<div align="center">
<strong>Ready to unlock the power of long-horizon reasoning? Get started with TIMRUN today!</strong>
</div>