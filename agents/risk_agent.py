def risk_agent(state):

    score = 0

    reasons = []

    if state["aml_flag"]:
        score += 60
        reasons.append(
            "Large transaction amount, AML screening triggered"
        )

    if state["kyc_status"] == "REVIEW":
        score += 20
        reasons.append(
            "KYC requires manual review"
        )
    
    if len(state.get("matched_rules", [])) > 0:
        score += 10
        reasons.append(
            "Compliance rules matched"
        )
    trace = state.get("decision_trace", []).copy()

    trace.append(
    f"Risk Agent: Final Risk Score = {score}"
    )
    return {
       
        "risk_score": score,
        "risk_reasons": reasons,
        "decision_trace": [
        f"Risk Agent: Risk Score = {score}"
        ]
    }