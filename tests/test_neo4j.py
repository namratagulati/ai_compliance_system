from dotenv import load_dotenv
import os

load_dotenv()

# print("URI =", repr(os.getenv("NEO4J_URI")))
# print("USER =", repr(os.getenv("NEO4J_USER")))
# print("PASSWORD =", bool(os.getenv("NEO4J_PASSWORD")))

from graph.neo4j_client import Neo4jClient

client = Neo4jClient()

print(
    client.test_connection()
)

#print(repr(os.getenv("NEO4J_URI")))