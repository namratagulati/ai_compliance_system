from langgraph.graph import StateGraph, START, END
from workflows.state import ComplianceState
from agents.kyc_agent import kyc_agent
from agents.aml_agent import aml_agent
from agents.risk_agent import risk_agent
from agents.compliance_agent import compliance_agent
from agents.audit_agent import audit_agent
from agents.human_agent import human_agent


#State earlier- a dictionary 
graph = StateGraph(ComplianceState)

#Add nodes
graph.add_node("kyc", kyc_agent)
graph.add_node("aml", aml_agent)
graph.add_node("compliance", compliance_agent)
graph.add_node("risk", risk_agent)
graph.add_node("audit", audit_agent)
graph.add_node("human", human_agent)

# -----------------------------
# Parallel execution
# -----------------------------

graph.add_edge(START, "kyc")
graph.add_edge(START, "aml")
graph.add_edge(START, "compliance")

# -----------------------------
# Merge into Risk Agent
# -----------------------------

graph.add_edge("kyc", "risk")
graph.add_edge("aml", "risk")
graph.add_edge("compliance", "risk")

# -----------------------------
# Final pipeline
# -----------------------------

graph.add_edge("risk", "audit")
graph.add_edge("audit", "human")
graph.add_edge("human", END)

app = graph.compile()