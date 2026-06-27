from services.graph_risk_service import (
    check_graph_risks
)

def aml_agent(state):

    txn = state["transaction"]

    risks = check_graph_risks(
        txn["sender"],
        txn["receiver"]
    )
    print("\nGraph Risks:")
    print(risks)
    
    reasons = []

    if txn["amount"] > 50000:
        reasons.append("Large transaction amount")

    shared = risks["shared_device"]
    print("Shared:", shared)
    circular = risks["circular_flow"]
    print("Circular:", circular)

    mule = risks["mule_account"]
    print("Mule:", mule)
    
    if shared["detected"]:
        reasons.append(
            f"Customer shares device {shared['device_id']} with "
            + ", ".join(shared["other_customers"])
        )

    circular = risks["circular_flow"]

    if circular["detected"]:
        reasons.append(
            f"Circular money flow detected ({circular['cycle_count']} cycle(s))"
        )

    mule = risks["mule_account"]

    if mule["detected"]:
        reasons.append(
            f"Receiver has funds from {mule['incoming_senders']} different senders"
        )

    trace = state.get("decision_trace", []).copy()

    trace.append(
    "AML Agent: " +
    (", ".join(reasons) if reasons else "No AML issues detected")
)
    
    return {
   
    "aml_flag": len(reasons) > 0,
    "aml_reasons": reasons,
    "graph_risks": risks,
    "decision_trace": [
        "AML Agent: " +
        (", ".join(reasons) if reasons else "No AML issues")
    ]
}