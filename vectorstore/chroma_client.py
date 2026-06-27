# vectorstore/chroma_client.py
#use persist_directory ..Without it:Chroma.from_documents(...)..stores everything in RAM.When Python stops:All vectors lost.
#from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

PERSIST_DIRECTORY = "chroma_db"

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory=PERSIST_DIRECTORY,
    embedding_function=embedding_model
)


def search_regulations(query: str, k: int = 3):
    """
    Search compliance documents.
    """

    results = vector_db.similarity_search(
        query=query,
        k=k
    )

    return results