# vectorstore/ingest_docs.py

from pathlib import Path

#from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import Docx2txtLoader

from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import Chroma

#from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings


DOCUMENTS_DIR = "documents"

PERSIST_DIRECTORY = "chroma_db"

def load_all_documents():

    docs = []

    docx_files = Path(DOCUMENTS_DIR).glob("*.docx")

    for file in docx_files:

        print(f"Loading {file}")

        source_name = file.name

        loader = Docx2txtLoader(str(file))

        documents = loader.load()

        for doc in documents:

            doc.metadata["source"] = source_name

            if "fatf" in source_name.lower():
                doc.metadata["regulator"] = "FATF"

            elif "rbi" in source_name.lower():
                doc.metadata["regulator"] = "RBI"

            elif "aml" in source_name.lower():
                doc.metadata["regulator"] = "AML Policy"

        docs.extend(documents)

    return docs

from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    return chunks

def create_vector_db():

    print("Loading PDFs...")

    documents = load_all_documents()

    print(f"Loaded {len(documents)} pages")

    print("Splitting into chunks...")

    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    embedding_model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Creating Chroma database...")

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=PERSIST_DIRECTORY
    )

    print("Done!")

    print(f"Stored {len(chunks)} chunks")


if __name__ == "__main__":
    create_vector_db()