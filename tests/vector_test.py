from vectorstore.chroma_client import search_regulations

results = search_regulations(
    "high value transaction AML review"
)

for doc in results:
    print(doc.metadata)
    print(doc.page_content[:300])
    print("=" * 50)