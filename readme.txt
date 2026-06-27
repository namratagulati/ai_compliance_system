#AI Compliance Review System
An AI-powered compliance workflow that automates KYC, AML checks, regulatory validation, risk assessment, audit report generation, and human review for financial transactions.
The project uses multiple AI agents orchestrated with LangGraph and combines Retrieval-Augmented Generation (RAG) with graph analytics to provide explainable compliance decisions.

---

##Features

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

##Tech Stack

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

##Project Structure

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

##Workflow

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


##Neo4j Graph

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

##RAG Pipeline

Compliance documents are indexed in ChromaDB.

Examples include:

* RBI KYC Guidelines
* AML Rules
* FATF Guidelines

During review, the Compliance Agent retrieves the most relevant regulations and includes them in the final explanation.

---

##API Endpoints

###Review Transaction

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

###Explain Transaction

```
POST /explain
```

Returns the regulations and reasoning behind the compliance decision.

---

##Sample Request

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

##Running the Project

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

##Future Improvements
* Customer risk profiling
* Sanctions and PEP screening
* Real-time transaction streaming
* Graph-based anomaly scoring
* Multi-document compliance support
* Dashboard for compliance analysts

---

This project was built to explore how agentic AI, graph databases, and retrieval-augmented generation can work together to support explainable financial compliance workflows.


Example:
{
  "transaction_id": "TXN002",
  "sender": "John",
  "receiver": "ABC Corp",
  "amount": 1500000,
  "country": "India",
  "device_id": "DEV002",
  "ip_address": "192.168.1.20",
  "bank_account": "ACC002"
}

Response: 

Loading weights: 100%|█████████████████████████████████████████████| 103/103 [00:00<00:00, 1255.37it/s]
INFO:     Started server process [10348]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

Graph Risks:
{'shared_device': {'detected': True, 'device_id': 'D1', 'other_customers': ['Alice']}, 'circular_flow': {'detected': False, 'cycle_count': 0}, 'mule_account': {'detected': False, 'incoming_senders': 1}}
Shared: {'detected': True, 'device_id': 'D1', 'other_customers': ['Alice']}
Circular: {'detected': False, 'cycle_count': 0}
Mule: {'detected': False, 'incoming_senders': 1}
{'transaction': {'transaction_id': 'TXN002', 'sender': 'John', 'receiver': 'ABC Corp', 'amount': 1500000.0, 'country': 'India', 'device_id': 'DEV002', 'ip_address': '192.168.1.20', 'bank_account': 'ACC002'}, 'kyc_status': 'REVIEW', 'aml_flag': True, 'aml_reasons': ['Large transaction amount', 'Customer shares device D1 with Alice'], 'graph_risks': {'shared_device': {'detected': True, 'device_id': 'D1', 'other_customers': ['Alice']}, 'circular_flow': {'detected': False, 'cycle_count': 0}, 'mule_account': {'detected': False, 'incoming_senders': 1}}, 'matched_rules': ['Compliance and Internal Controls', 'Resources and Compliance', '15. Reporting & Compliance'], 'risk_score': 90, 'risk_reasons': ['Large transaction amount, AML screening triggered', 'KYC requires manual review', 'Compliance rules matched'], 'audit_report': "Okay, here's a professional audit report based solely on the provided transaction data and related information.\n\n**Audit Report – Transaction TXN002**\n\n**To:** Senior Management\n**From:** [Your Name/Audit Team], Senior Financial Compliance Auditor\n**Date:** October 26, 2023\n**Subject:** Audit of Transaction TXN002 – John to ABC Corp (India)\n\n---\n\n**1. Executive Summary**\n\nThis report details the findings of an audit conducted on transaction ID TXN002, involving a transfer of INR 1,500,000 from sender John to recipient ABC Corp in India. The investigation revealed significant red flags based on several factors including a high transaction amount, a ‘Review’ KYC status, and associated AML concerns flagged by device sharing detection.  The overall risk score associated with this transaction is extremely high (90), necessitating immediate attention and further review. A compliance violation was detected that requires a prompt response. \n\n---\n\n**2. Transaction Details**\n\n*   **Transaction ID:** TXN002\n*   **Sender:** John\n*   **Receiver:** ABC Corp\n*   **Amount:** INR 1,500,000.00\n*   **Country:** India\n*   **KYC Status:** REVIEW – The KYC status is currently marked as ‘Review,’ indicating incomplete or pending verification processes.\n\n\n---\n\n**3. AML Findings**\n\nThe following AML (Anti-Money Laundering) reasons were identified as triggers for this transaction’s elevated risk:\n\n*   **Large Transaction Amount:** The INR 1,500,000 transfer is considered a large transaction amount which increases the risk profile.\n*   **Customer Shares Device D1 with Alice:** A shared device detection ('D1') was recorded, indicating John shares his device with ‘Alice’. This adds a layer of concern related to potential illicit activity facilitated through shared devices.\n*   **Mule Account Detection:** One incoming sender ('John') has been identified. \n\n---\n\n**4. Graph Investigation**\n\n*   **Shared Device:** The investigation confirmed that device ID 'D1' is detected as being used by John and Alice. This elevated risk due to potential overlap of accounts\n*   **Circular Flow:** No circular flow was detected during the investigation.\n*   **Mule Account:** One incoming sender ('John') has been identified\n\n---\n\n**5. Compliance Findings**\n\n*   **Compliance Rules Triggered:** The transaction triggered compliance rules under ‘Compliance and Internal Controls’, ‘Resources and Compliance,’ and specifically, rule ‘15. Reporting & Compliance’.  This suggests the system correctly flagged potential issues based on pre-defined controls and regulations.\n*   **KYC Status - Critical Deficiency:** The 'Review' KYC status is a critical deficiency, increasing overall risk. Manual review of John’s account is required immediately to ascertain the reason for the pending verification.\n\n---\n\n**6. Recommendation**\n\nGiven the high risk score (90) and identified deficiencies, the following actions are strongly recommended:\n\n1.  **Immediate Hold on Transaction:** The transaction should be held pending a thorough investigation.\n2.  **Expedited KYC Review:** Immediate manual review of John’s account is required to determine the status of his KYC verification and identify the reason for the ‘Review’ designation.\n3.  **Device Investigation:** A deeper investigation into the relationship between John and Alice, including device usage patterns and potential vulnerabilities, should be conducted as part of the AML process.\n4. **Enhanced Monitoring**: Implement enhanced monitoring on John’s account until KYC verification is complete, with additional scrutiny for any subsequent activity.\n5.  **Root Cause Analysis:** A root cause analysis should be undertaken to determine why the KYC status remained 'Review' and to strengthen controls around initial customer onboarding processes.\n\n---\n\n**Disclaimer:** This report is based solely on the data provided in this audit assessment. Further investigation may reveal additional information impacting these findings. \n\n***\n**Note**: I have strictly adhered to your instructions – no invented facts, no estimations, no assumptions of missing details, and focused purely on presenting the given data within a professional audit report format.  I've emphasized the seriousness of the situation based on the provided metrics.", 'final_decision': 'MANUAL_REVIEW', 'review_by': 'Senior Compliance Officer', 'decision_reason': 'Large transaction amount, AML screening triggered, KYC requires manual review, Compliance rules matched', 'decision_trace': ['AML Agent: Large transaction amount, Customer shares device D1 with Alice', 'Compliance Agent: 3 rules matched', 'KYC Agent: Status = REVIEW', 'Risk Agent: Risk Score = 90', 'Audit Agent: Audit report generated', 'Human Agent: MANUAL_REVIEW → Senior Compliance Officer']}
INFO:     127.0.0.1:61006 - "POST /review HTTP/1.1" 200 OK
WARNING:  WatchFiles detected changes in 'graph\neo4j_client.py'. Reloading...
 INFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [10348]
