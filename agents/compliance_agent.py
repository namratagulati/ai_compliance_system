from vectorstore.chroma_client import search_regulations


def compliance_agent(state):

    txn = state["transaction"]

    query = f"""
    Compliance Review
    Amount: {txn['amount']}
    Country: {txn['country']}

    Check:

    - AML obligations
    - KYC requirements
    - FATF regulations
    - High value transaction rules
    """

    results = search_regulations(
        query=query,
        k=3
    )

    # matched_rules = [
    #     doc.page_content
    #     for doc in results
    # ]
    matched_rules = [
    doc.page_content.split("\n")[0]
    for doc in results
    ]

    trace = state.get("decision_trace", []).copy()

    trace.append(
    f"Compliance Agent: Matched {len(matched_rules)} regulations"
    )

    # return {
    #     #**state,  #LangGraph merges state automatically.
    #     "matched_rules": matched_rules
    # }
    return {
    #**state,
    "matched_rules": matched_rules,
    "decision_trace":  [
        f"Compliance Agent: {len(matched_rules)} rules matched"
    ]
    }