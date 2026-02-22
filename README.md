# Medical Image Analysis Agent

An **agentic AI system** that analyzes medical images (X-rays, CT scans, MRIs) 
using Google's Gemini models and provides structured diagnostic reports with 
research-backed context.

## Features
- 🤖 **AI Agent** powered by Gemini 2.5 Flash
- 🔍 **Tool use**: DuckDuckGo search for medical literature
- 🖼️ **Multimodal**: Processes medical images directly
- 📊 **Structured output**: 5-part diagnostic framework


## 🏗️ System Architecture

```mermaid
graph TB
    subgraph "MEDICAL IMAGE ANALYSIS (Agentic AI App)"
        A[🤖 THE AGENT<br/>agno Framework] --> B[🧠 Brain<br/>Gemini Gen AI]
        A --> C[🔍 Tool<br/>DuckDuckGo Search]
        B --> D[📊 Analysis Results]
        C --> D
        D --> E[🖥️ Streamlit UI]
        
        style A fill:#f9f,stroke:#333,stroke-width:2px
        style B fill:#bbf,stroke:#333,stroke-width:2px
        style C fill:#bfb,stroke:#333,stroke-width:2px
        style E fill:#ffd,stroke:#333,stroke-width:2px
    end
    
    User([👤 User]) --> E
    E --> User
```

