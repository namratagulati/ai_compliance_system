# test_llm.py


from llm.llm_client import llm

response = llm.invoke("Say hello")

print(response.content)