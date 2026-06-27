# test_graph.py

from workflows.compliance_graph import app

txn = {
    "transaction_id": "TXN001",
    "sender": "John",
    "receiver": "ABC Corp",
    "amount": 1500000,
    "country": "India"
}

result = app.invoke({
    "transaction": txn.model_dump()
})

print(result)