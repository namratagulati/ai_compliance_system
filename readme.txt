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


Example 1:
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


Example 2 :
{
  "transaction_id": "TXN1001",
  "sender": "Alice",
  "receiver": "Amazon India",
  "amount": 5000,
  "country": "India",
  "device_id": "DEV101",
  "ip_address": "49.36.120.10",
  "bank_account": "SBIN123456789"
}

Response:

Graph Risks:
{'shared_device': {'detected': True, 'device_id': 'D1', 'other_customers': ['John']}, 'circular_flow': {'detected': False, 'cycle_count': 0}, 'mule_account': {'detected': False, 'incoming_senders': 0}}
Shared: {'detected': True, 'device_id': 'D1', 'other_customers': ['John']}
Circular: {'detected': False, 'cycle_count': 0}
Mule: {'detected': False, 'incoming_senders': 0}
{'transaction': {'transaction_id': 'TXN1001', 'sender': 'Alice', 'receiver': 'Amazon India', 'amount': 5000.0, 'country': 'India', 'device_id': 'DEV101', 'ip_address': '49.36.120.10', 'bank_account': 'SBIN123456789'}, 'kyc_status': 'PASS', 'aml_flag': True, 'aml_reasons': ['Customer shares device D1 with John'], 'graph_risks': {'shared_device': {'detected': True, 'device_id': 'D1', 'other_customers': ['John']}, 'circular_flow': {'detected': False, 'cycle_count': 0}, 'mule_account': {'detected': False, 'incoming_senders': 0}}, 'matched_rules': ['Compliance and Internal Controls', 'Resources and Compliance', '15. Reporting & Compliance'], 'risk_score': 70, 'risk_reasons': ['Large transaction amount, AML screening triggered', 'Compliance rules matched'], 'audit_report': "**Financial Compliance Audit Report**\n\n**Report Date:** October 26, 2023\n**Audit Subject:** Transaction TXN1001 – Alice to Amazon India - INR 5000.00\n\n**Prepared By:** [Your Name], Senior Financial Compliance Auditor\n\n---\n\n**1. Executive Summary**\n\nThis report details the findings of an audit conducted on transaction ID TXN1001, involving a transfer of INR 5000.00 from Alice to Amazon India in India. The transaction was flagged due to a risk score of 70, triggered by a combination of factors including a large transaction amount and associated AML screening results.  The investigation revealed a shared device (‘D1’) used by Alice and another customer (John), along with adherence to relevant compliance rules related to reporting and controls. While the transaction itself was authorized via KYC, the identified risk necessitates further scrutiny and potential enhanced due diligence procedures going forward.\n\n---\n\n**2. Transaction Details**\n\n*   **Transaction ID:** TXN1001\n*   **Sender:** Alice\n*   **Receiver:** Amazon India\n*   **Amount:** INR 5000.00\n*   **Country:** India\n*   **KYC Status:** PASS\n\n\n---\n\n**3. AML Findings**\n\nThe Anti-Money Laundering (AML) review revealed the following key findings:\n\n*   **AML Reasons:** The primary AML reason for flagging this transaction is “Customer shares device D1 with John.” This indicates a potential link between Alice and another customer via shared device usage, raising concerns about potential illicit activity.\n*   **Graph Investigation – Shared Device:**  The graph investigation confirmed the detection of shared device ‘D1’, with John listed as another customer utilizing this device alongside Alice. \n*   **Circular Flow:** No circular flow was detected during the AML review.\n*   **Mule Account:** The system did not detect any potential mule account activity associated with this transaction (incoming senders = 0).\n\n\n\n---\n\n**4. Graph Investigation**\n\nThe graph investigation focused on identifying patterns and relationships related to this transaction, specifically focusing on device usage:\n\n*   **Detected:** True – A shared device ('D1') was confirmed to be in use by both Alice and John.\n*   **Device ID:** D1 \n*   **Other Customers:** John\n\n\n---\n\n**5. Compliance Findings**\n\nThis transaction’s compliance was assessed against the following rules:\n\n*   **Compliance Rules:** ‘Compliance and Internal Controls’, ‘Resources and Compliance’, ‘15. Reporting & Compliance’. The transaction triggered a match against these rules, contributing to the overall risk score.  The AML screening being triggered also indicates adherence to standard compliance protocols.\n\n\n\n---\n\n**6. Recommendation**\n\nBased on the findings of this audit, we recommend the following actions:\n\n*   **Enhanced Due Diligence (EDD) – Device Linkage:** Conduct enhanced due diligence on Alice and John, focusing on understanding the nature of their relationship and the purpose behind shared device usage ('D1').  Investigate if there are any legitimate reasons for the shared device.\n*   **Review Shared Device Policies**: A review of existing policies concerning shared devices and potential risks is recommended to determine if stricter controls or monitoring procedures are warranted, especially in high-value transactions.\n*   **Risk Score Review:** Reassess the risk scoring methodology to ensure accurate reflection of factors like shared device usage and transaction amounts.  Consider adjusting thresholds to improve detection capabilities.\n* **Ongoing Monitoring**: Implement continuous monitoring for any further activity associated with the shared device 'D1' or John. \n\nThis report is intended solely for internal use by [Your Organization Name] and should not be distributed without authorization.\n\n\n---\n\n**End of Report**", 'final_decision': 'ENHANCED_DUE_DILIGENCE', 'review_by': 'AML Investigation Team', 'decision_reason': 'Large transaction amount, AML screening triggered, Compliance rules matched', 'decision_trace': ['AML Agent: Customer shares device D1 with John', 'Compliance Agent: 3 rules matched', 'KYC Agent: Status = PASS', 'Risk Agent: Risk Score = 70', 'Audit Agent: Audit report generated', 'Human Agent: ENHANCED_DUE_DILIGENCE → AML Investigation Team']}

Example 3: 
{
  "transaction_id": "TXN2003",
  "sender": "John",
  "receiver": "FoxDigit",
  "amount": 1800000,
  "country": "Uzbekistan",
  "device_id": "DEV999",
 
  "bank_account": "INTL998877665"
}

Response:

Graph Risks:
{'shared_device': {'detected': True, 'device_id': 'D1', 'other_customers': ['Alice']}, 'circular_flow': {'detected': False, 'cycle_count': 0}, 'mule_account': {'detected': False, 'incoming_senders': 0}}
Shared: {'detected': True, 'device_id': 'D1', 'other_customers': ['Alice']}
Circular: {'detected': False, 'cycle_count': 0}
Mule: {'detected': False, 'incoming_senders': 0}
{'transaction': {'transaction_id': 'TXN2003', 'sender': 'John', 'receiver': 'FoxDigit', 'amount': 1800000.0, 'country': 'Uzbekistan', 'device_id': 'DEV999', 'ip_address': None, 'bank_account': 'INTL998877665'}, 'kyc_status': 'REVIEW', 'aml_flag': True, 'aml_reasons': ['Large transaction amount', 'Customer shares device D1 with Alice'], 'graph_risks': {'shared_device': {'detected': True, 'device_id': 'D1', 'other_customers': ['Alice']}, 'circular_flow': {'detected': False, 'cycle_count': 0}, 'mule_account': {'detected': False, 'incoming_senders': 0}}, 'matched_rules': ['Compliance and Internal Controls', 'Resources and Compliance', 'Know Your Customer (KYC)'], 'risk_score': 90, 'risk_reasons': ['Large transaction amount, AML screening triggered', 'KYC requires manual review', 'Compliance rules matched'], 'audit_report': "Okay, here's a professional audit report based on the provided transaction data and analysis, adhering to your specifications – no invention or estimation of values is included:\n\n**Audit Report - Transaction TXN2003**\n\n**Date:** October 26, 2023\n**Prepared by:** [Your Name/Senior Financial Compliance Auditor]\n**Department:** Financial Compliance & Risk Management\n\n---\n\n**1. Executive Summary**\n\nThis report details the findings of an audit conducted on Transaction ID TXN2003 involving a transfer of $1,800,000 from John to FoxDigit in Uzbekistan with a KYC status of ‘REVIEW’.  The transaction triggered significant risk concerns due to a high transaction amount combined with identified AML indicators and incomplete KYC documentation. A shared device linked to an additional customer (Alice) was detected, escalating the risk profile. The resulting Risk Score of 90 necessitates immediate escalation and thorough investigation to mitigate potential illicit activity.\n\n---\n\n**2. Transaction Details**\n\n*   **Transaction ID:** TXN2003\n*   **Sender:** John\n*   **Receiver:** FoxDigit\n*   **Amount:** $1,800,000.00\n*   **Country of Origin:** Uzbekistan\n*   **KYC Status:** REVIEW\n\n\n---\n\n**3. AML Findings**\n\nThe following AML (Anti-Money Laundering) reasons were identified in relation to this transaction:\n\n*   **Reason 1:** Large Transaction Amount – The $1,800,000 transfer represents a significantly high amount that immediately triggered standard AML screening protocols.\n*   **Reason 2:** Shared Device –  The system detected that the device used for initiating the transaction (Device ID D1) is also shared with another customer, Alice. This raises concerns about potential collusion or money laundering activity.\n\n---\n\n**4. Graph Investigation**\n\n*   **Shared Device Detection:** The investigation confirmed that ‘Device D1’ was identified as being associated with another customer: Alice.\n    *   **Detected:** True\n    *   **Device ID:** D1\n    *   **Other Customers:** Alice\n*   **Circular Flow Analysis:** The circular flow analysis revealed no detected cyclical transactions, with a cycle count of 0.\n*   **Mule Account Detection:**  No indicators were found suggesting the involvement of a mule account; incoming senders were 0.\n\n\n\n---\n\n**5. Compliance Findings**\n\n*   **Rule Adherence:** The transaction was flagged due to matching against several compliance rules:\n    *   Compliance and Internal Controls\n    *   Resources and Compliance\n    *   Know Your Customer (KYC) –  Specifically, the KYC status of ‘REVIEW’ indicated a gap in required verification.\n\n*   **Risk Score Calculation:** Based on the identified factors, a Risk Score of 90 was calculated reflecting the elevated risk associated with this transaction.\n\n\n---\n\n**6. Recommendation**\n\nGiven the significant risk score and the findings detailed above, we strongly recommend the following immediate actions:\n\n1.  **Immediate Escalation:** This transaction requires urgent escalation to Senior Management for review and further action.\n2.  **KYC Completion:** The KYC process for both John and FoxDigit must be completed immediately with priority. Specific attention needs to be given to understanding the source of funds and confirming compliance requirements.\n3. **Device Investigation:** A thorough investigation into the shared device usage is essential, including a review of all transactions linked to Device D1 and an assessment of Alice’s relationship with John. \n4.  **Enhanced Monitoring:** Increase monitoring of this account and any related activity until a complete understanding of the transaction's origin and purpose can be established.\n\n---\n\n**End of Report**\n\n**Disclaimer:** This report is based solely on the provided data and analysis at the time of preparation. Further investigation may reveal additional information impacting these findings.\n\n---\n\nDo you want me to modify or expand upon any aspect of this report? Perhaps focusing on a particular element, or adding a section about potential next steps for the investigation team?", 'final_decision': 'MANUAL_REVIEW', 'review_by': 'Senior Compliance Officer', 'decision_reason': 'Large transaction amount, AML screening triggered, KYC requires manual review, Compliance rules matched', 'decision_trace': ['AML Agent: Large transaction amount, Customer shares device D1 with Alice', 'Compliance Agent: 3 rules matched', 'KYC Agent: Status = REVIEW', 'Risk Agent: Risk Score = 90', 'Audit Agent: Audit report generated', 'Human Agent: MANUAL_REVIEW → Senior Compliance Officer']}
