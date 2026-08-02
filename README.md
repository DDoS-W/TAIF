# TAIF

> **Trustworthy Agentic Investment Framework**

An AI-powered research framework for evaluating Large Language Models (LLMs) and Agentic AI systems in Taiwan stock market analysis and investment decision-making.

---

# Overview

TAIF is an open research framework designed to evaluate how modern AI models can assist financial analysis and investment decisions in the Taiwan stock market.

Unlike a traditional stock prediction project, TAIF focuses on building a **reproducible research platform** that enables fair comparison between different AI models under identical market data, news evidence, prompts, and evaluation metrics.

The long-term vision is to develop a trustworthy AI investment research framework capable of supporting academic research and practical financial analysis.

---

# Research Objectives

The primary objectives of TAIF are:

- Evaluate the financial reasoning capability of Large Language Models (LLMs)
- Compare different AI models (GPT, Gemini, Claude, etc.) under identical conditions
- Build a reproducible AI investment research workflow
- Develop standardized research outputs for AI-generated investment analysis
- Evaluate AI investment recommendations through historical backtesting
- Explore Agentic AI workflows for financial decision-making

---

# Current Features

## Phase 1 — Data Pipeline ✅

- [x] Project Setup
- [x] Taiwan Stock Data Collection
- [x] Feature Engineering
- [x] Technical Indicators

---

## Phase 2 — Evidence Pipeline ✅

- [x] Financial News Collection
- [x] RSS-based Evidence Collection
- [x] Evidence Management

---

## Phase 3 — Research Infrastructure ✅

- [x] Prompt Builder
- [x] LLM Engine (Mock)
- [x] Experiment Manager
- [x] TAIF Parser
- [x] End-to-End Research Pipeline (Mock)

---

## Phase 4 — AI Integration (Planned)

- [ ] OpenAI API Integration
- [ ] Structured Output
- [ ] Experiment Metadata
- [ ] Research Database

---

## Phase 5 — Advanced Research (Planned)

- [ ] Retrieval-Augmented Generation (RAG)
- [ ] Multi-Agent Collaboration
- [ ] Verification Agent
- [ ] Multi-LLM Benchmark
- [ ] Historical Backtesting
- [ ] Paper Trading

---

# Research Workflow

```text
Market Data
      │
      ▼
Feature Engineering
      │
      ▼
Evidence Collection
      │
      ▼
Prompt Builder
      │
      ▼
LLM Engine
      │
      ▼
Research Output
      │
      ▼
Experiment Management
      │
      ▼
Evaluation & Backtesting
```

---

# Project Structure

```text
TAIF/
│
├── notebooks/
│   ├── 01_Data_Collection.ipynb
│   ├── 02_Feature_Engineering.ipynb
│   ├── 03_Evidence_Collection.ipynb
│   ├── 04_Prompt_Builder.ipynb
│   ├── 05_LLM_Engine.ipynb
│   ├── 06_Experiment_Manager.ipynb
│   ├── 07_Parser.ipynb
│   └── 08_TAIF_Pipeline.ipynb
│
├── src/
│   ├── __init__.py
│   ├── indicators.py
│   ├── feature_builder.py
│   ├── evidence_collector.py
│   ├── prompt_builder.py
│   ├── llm_engine.py
│   ├── experiment_manager.py
│   └── parser.py
│
├── data/
│
├── experiments/
│   ├── prompts/
│   ├── outputs/
│   ├── reports/
│   └── logs/
│
├── config/
│
├── requirements.txt
│
└── README.md
```

---

# Technology Stack

## Programming

- Python 3

## Development

- Google Colab
- GitHub

## Data Processing

- Pandas
- NumPy
- Matplotlib

## Financial Data

- Yahoo Finance (yfinance)

## News Collection

- RSS Feed
- feedparser

## AI

- Prompt Engineering
- OpenAI API *(planned)*
- Multi-LLM *(planned)*

---

# Installation

Clone this repository:

```bash
git clone https://github.com/<your-account>/TAIF.git
```

Enter the project directory:

```bash
cd TAIF
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Development Progress

| Sprint | Status |
|---------|--------|
| Sprint 1 — Data Pipeline | ✅ Completed |
| Sprint 2 — Evidence Pipeline | ✅ Completed |
| Sprint 3 — Research Infrastructure | ✅ Completed |
| Sprint 4 — OpenAI Integration | 🔄 Planned |
| Sprint 5 — Multi-LLM Evaluation | 🔄 Planned |
| Sprint 6 — Backtesting | 🔄 Planned |

---

# Roadmap

## Short-term

- OpenAI API Integration
- Structured Outputs
- Configuration Management
- Experiment Metadata

## Mid-term

- GPT vs Gemini vs Claude Comparison
- RAG Integration
- Verification Agent
- Automated Evaluation

## Long-term

- Historical Backtesting
- Portfolio Simulation
- Multi-Agent Investment Framework
- Academic Publication

---

# Project Vision

TAIF aims to become an open, reproducible AI investment research platform rather than a simple stock prediction tool.

The framework is designed to support:

- Academic research
- AI benchmarking
- Financial reasoning evaluation
- Agentic AI experimentation
- Investment decision support

---

# License

This project is released under the MIT License.
