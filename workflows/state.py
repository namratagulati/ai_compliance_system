# workflows/state.py
#dictionary should contain these keys and these types
#type checking
from typing import TypedDict, Annotated
import operator

class ComplianceState(TypedDict):

    transaction: dict
    kyc_status: str
    aml_flag: bool
    aml_reasons: list
    graph_risks: dict
    matched_rules: list
    risk_score: int
    risk_reasons: list
    audit_report: str
    final_decision: str
    review_by: str
    decision_reason: str
    # Merge lists coming from parallel nodes
    decision_trace: Annotated[list[str], operator.add]