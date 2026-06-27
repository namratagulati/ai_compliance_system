from fastapi import APIRouter

from schemas.transaction import Transaction

from workflows.compliance_graph import app

router = APIRouter()

#When user sends POST /review, run this

@router.post("/review")
def review_transaction(txn: Transaction):

    result = app.invoke(
        {
            "transaction": txn.model_dump(),
            "decision_trace": []
        }
    )
    print(result)
    
    return {
    "transaction_id": txn.transaction_id,
    "risk_score": result.get("risk_score"),
    "risk_reasons": result.get("risk_reasons"),
    "decision": result.get("final_decision"),
    "review_by": result.get("review_by"),
    "decision_reason": result.get("decision_reason"),
    "decision_trace": result.get("decision_trace"),
    "audit_report": result.get("audit_report")
    }
    

@router.post("/explain")
def explain_transaction(txn: Transaction):

    result = app.invoke(
        {
            "transaction": txn.model_dump()
        }
    )

    return {
        "risk_score":
            result["risk_score"],

        "risk_reasons":
            result["risk_reasons"],

        "matched_rules":
            result["matched_rules"]
    }