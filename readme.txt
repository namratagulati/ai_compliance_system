# AI Compliance Review System
An AI-powered compliance workflow that automates KYC, AML checks, regulatory validation, risk assessment, audit report generation, and human review for financial transactions.
The project uses multiple AI agents orchestrated with LangGraph and combines Retrieval-Augmented Generation (RAG) with graph analytics to provide explainable compliance decisions.

---

## Features

* Multi-agent workflow using LangGraph
* KYC verification
* AML risk detection
* Regulatory retrieval using ChromaDB
* Graph-based fraud detection with Neo4j
* Risk scoring engine
* AI-generated audit reports using Ollama (Gemma)
* Human approval workflow
* Decision trace for explainability

---

## Tech Stack

* Python
* FastAPI
* LangGraph
* LangChain
* Ollama (Gemma 3)
* ChromaDB
* Neo4j Aura
* HuggingFace Embeddings
* Pydantic

---

## Project Structure

```
agents/
database/
schemas/
services/
vectorstore/
workflows/
api/
documents/
main.py
```

---

## Workflow

```
Transaction
      │
      ▼
 ┌────────────┐
 │ KYC Agent  │
 └────────────┘
      │
      ├─────────────┐
      ▼             ▼
 AML Agent     Compliance Agent
      │             │
      └──────┬──────┘
             ▼
        Risk Agent
             │
             ▼
       Audit Agent
             │
             ▼
    Human Approval Agent
             │
             ▼
       Final Decision
```

---

## Neo4j Graph

Each transaction is stored as a relationship graph containing:

* Customer
* Transaction
* Device
* IP Address
* Bank Account

The graph is used to identify:

* Shared devices
* Circular fund movement
* Potential mule accounts

---

## RAG Pipeline

Compliance documents are indexed in ChromaDB.

Examples include:

* RBI KYC Guidelines
* AML Rules
* FATF Guidelines

During review, the Compliance Agent retrieves the most relevant regulations and includes them in the final explanation.

---

## API Endpoints

### Review Transaction

```
POST /review
```

Returns:

* Risk score
* Risk reasons
* Final decision
* Reviewer
* Decision reason
* Audit report
* Decision trace

### Explain Transaction

```
POST /explain
```

Returns the regulations and reasoning behind the compliance decision.

---

## Sample Request

```json
{
  "transaction_id": "TXN101",
  "sender": "John",
  "receiver": "ABC Corp",
  "amount": 1500000,
  "country": "India",
  "device_id": "DEV001",
  "ip_address": "192.168.1.10",
  "bank_account": "ACC001"
}
```

---

## Running the Project

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Ollama:

```bash
ollama serve
```

Pull the model if required:

```bash
ollama pull gemma3:4b
```

Run the API:

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Future Improvements
* Customer risk profiling
* Sanctions and PEP screening
* Real-time transaction streaming
* Graph-based anomaly scoring
* Multi-document compliance support
* Dashboard for compliance analysts

---

This project was built to explore how agentic AI, graph databases, and retrieval-augmented generation can work together to support explainable financial compliance workflows.
