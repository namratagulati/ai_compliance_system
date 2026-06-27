def human_agent(state):

    score = state["risk_score"]

    reasons = []

    if score >= 80:

        decision = "MANUAL_REVIEW"

        reviewer = "Senior Compliance Officer"

    elif score >= 60:

        decision = "ENHANCED_DUE_DILIGENCE"

        reviewer = "AML Investigation Team"

    else:

        decision = "APPROVED"

        reviewer = "System Auto Approval"

    reasons.extend(
        state.get("risk_reasons", [])
    )
    trace = state.get("decision_trace", []).copy()

    trace.append(
    f"Human Agent: {decision} assigned to {reviewer}"
)
    return {

        "final_decision": decision,

        "review_by": reviewer,

        "decision_reason": ", ".join(reasons),
        "decision_trace":  [
        f"Human Agent: {decision} → {reviewer}"
        ]
    }