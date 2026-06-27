from graph.neo4j_client import  Neo4jClient

client = Neo4jClient()

client.create_transaction(
    txn_id="TXN001",
    sender="John",
    receiver="ABC Corp",
    amount=1500000,
    country="India"
)

print("Transaction inserted")