from llm.llm_client import llm

def audit_agent(state):

    # Get transaction
    txn = state["transaction"]

    # Get graph results from AML agent
    graph = state.get("graph_risks", {})

    # Build a readable graph summary
    graph_summary = f"""
    Shared Device:
    {graph.get("shared_device")}

    Circular Flow:
    {graph.get("circular_flow")}

    Mule Account:
    {graph.get("mule_account")}
    """

    # Build LLM prompt
    prompt = f"""
    You are a Senior Financial Compliance Auditor.

    Generate a professional audit report.

    Transaction
    -----------
    Transaction ID: {txn["transaction_id"]}
    Sender: {txn["sender"]}
    Receiver: {txn["receiver"]}
    Amount: {txn["amount"]}
    Country: {txn["country"]}

    KYC Status:
    {state.get("kyc_status")}

    AML Reasons:
    {state.get("aml_reasons", [])}

    Compliance Rules:
    {state.get("matched_rules", [])}

    Graph Investigation:
    {graph_summary}

    Risk Score:
    {state.get("risk_score")}

    Risk Reasons:
    {state.get("risk_reasons", [])}

    Write a professional audit report with:
    1. Executive Summary
    2. Transaction Details
    3. AML Findings
    4. Graph Investigation
    5. Compliance Findings
    6. Recommendation
    
    Do not invent facts.Do not estimate values.Do not assume missing information.
    """

    response = llm.invoke(prompt)
    trace = state.get("decision_trace", []).copy()

    trace.append(
    "Audit Agent: Audit report generated"
    )
    return {
       
        "audit_report": response.content,
        "decision_trace": [
        "Audit Agent: Audit report generated"
        ]
    }