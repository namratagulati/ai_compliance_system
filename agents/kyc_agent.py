
def kyc_agent(state):

    transaction = state["transaction"]

    if transaction["amount"] > 10000:
        status = "REVIEW"
    else:
        status = "PASS"

    trace = state.get("decision_trace", []).copy()

    trace.append(
        f"KYC Agent: Customer KYC status = {status}"
    )

    return {
       
        "kyc_status": status,
        "decision_trace": [
        f"KYC Agent: Status = {status}"     ]
    }
    
    #originally: Verify identity information using Aadhaar,PAN,Passport,Address