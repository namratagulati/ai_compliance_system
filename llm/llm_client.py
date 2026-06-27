from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# load_dotenv()
# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0
# )

from langchain_ollama import ChatOllama
llm = ChatOllama(
    model="gemma3:4b"
)