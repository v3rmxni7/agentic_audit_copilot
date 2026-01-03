# Agentic Audit Copilot

An **enterprise-grade, agentic AI system** for automated audit and compliance analysis.
The system ingests policy documents and transaction data, autonomously interprets compliance rules, evaluates transactions, assigns risk scores, and generates **auditor-style, explainable reports**.

This project demonstrates how **agentic AI systems** can be applied to real-world banking and enterprise compliance workflows using modular, production-oriented architecture.

---

## Why This Project Exists

Audit and compliance workflows in banks and enterprises are:

* Manual and time-consuming
* Expensive to scale
* Difficult to audit and explain
* Dependent on human interpretation of complex policy documents

**Agentic Audit Copilot** addresses this by introducing an autonomous, explainable AI pipeline that:

* Converts natural-language policies into enforceable rules
* Applies those rules deterministically to transaction data
* Scores and explains compliance risk in human-readable terms

This is **not a chatbot** — it is a decision-making system.

---

## Core Capabilities

* **Agentic Policy Interpretation**
  Converts policy text into structured, machine-enforceable compliance rules.

* **Transaction Ingestion & Normalization**
  Loads and validates real-world banking transaction data (CSV-based).

* **Deterministic Rule Evaluation**
  Applies extracted rules to transactions in an auditor-friendly, explainable manner.

* **Risk Scoring**
  Assigns numeric and categorical risk levels using transparent logic.

* **Human-Readable Explanations**
  Generates auditor-style explanations for every flagged violation.

* **End-to-End Orchestration**
  Modular agents coordinated through a single workflow pipeline.

---

## System Architecture

```
Policy Text / Documents
        ↓
Policy Interpreter Agent (LLM-powered)
        ↓
Structured Compliance Rules
        ↓
Rule Evaluation Agent (Deterministic)
        ↓
Compliance Violations
        ↓
Risk Scoring Agent
        ↓
Explanation Agent (LLM-powered)
        ↓
Audit Report Generator
```

The system intentionally combines **LLM-based reasoning** with **deterministic enforcement logic**, ensuring both flexibility and auditability.

---

## Agent Design

### Planner / Orchestration Layer

Coordinates the execution of all agents in sequence and manages data flow.

### Policy Interpreter Agent

* Reads natural-language compliance policies
* Extracts enforceable rules
* Outputs structured rule objects

### Transaction Analysis Agent

* Normalizes transaction data
* Prepares inputs for rule evaluation

### Rule Evaluation Agent

* Applies rules deterministically
* Flags violations with explicit reasons

### Risk Scoring Agent

* Assigns severity-based numeric risk
* Fully transparent and auditable

### Explanation Agent

* Produces professional, auditor-style explanations
* Designed for executive and compliance review

### Audit Report Generator

* Aggregates findings into a structured audit report

---

## Tech Stack

### Backend

* **Python 3.11+**
* **FastAPI** – API layer
* **Pydantic** – schema validation

### Agentic AI

* **Ollama** (local LLM runtime)
* **Mistral / LLaMA 3** (open-source LLMs)
* Modular LLM abstraction (easy to swap with hosted models)

### Data & Processing

* **Pandas** – transaction processing
* **pdfplumber** – policy ingestion
* **FAISS** – vector search (POC)
* **sentence-transformers** – embeddings

### UI

* HTML + Tailwind CSS (lightweight demo UI)

---

## Demo Flow

1. Enter or upload compliance policy text
2. Upload transaction CSV file
3. Run automated audit
4. Review:

   * Flagged transactions
   * Risk levels
   * Human-readable explanations
   * Summary audit report

This flow mirrors real internal compliance tools used by banks and enterprises.

---

## Example Output

```json
{
  "total_transactions": 3,
  "total_flagged": 1,
  "summary": "1 compliance violation detected out of 3 transactions.",
  "findings": [
    {
      "transaction_id": "TXN002",
      "rule_id": "AML_001",
      "risk_level": "HIGH",
      "explanation": "This transaction exceeds the permitted threshold and was executed without verified KYC documentation, representing a high-risk AML violation."
    }
  ]
}
```

---

## Deployment Notes

* The system is designed to run with **local open-source LLMs** for:

  * Zero inference cost
  * Full data control
  * On-prem enterprise deployment

* For public or large-scale deployment, the LLM layer can be swapped with:

  * OpenAI
  * Anthropic
  * Groq / Together.ai

No architectural changes are required — only the LLM service adapter.

---

## Scalability Considerations

* Stateless API design
* Modular agent architecture
* LLM abstraction for vendor flexibility
* Deterministic compliance logic for trust and auditability

Future extensions:

* PDF policy upload
* Multi-tenant support
* Role-based access control
* Audit report export (PDF)
* Dashboard analytics

---

## Intended Use Cases

* Banking compliance audits
* AML / KYC monitoring
* Internal enterprise audits
* Regulatory risk analysis
* Audit workflow automation

---

## Project Status

This project is a **production-quality Proof of Concept**, designed to demonstrate:

* Agentic AI reasoning
* Enterprise system design
* Real-world applicability

---

## Author

**Nischay Vermani**
AI Engineer – Agentic AI, LLM Systems, MLOps
IIT Roorkee

---

## Disclaimer

This project is for demonstration and research purposes only and is not intended for use in regulated production environments without appropriate validation, security reviews, and compliance approvals.
