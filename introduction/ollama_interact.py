from langchain_ollama import OllamaLLM
llm = OllamaLLM(model="llama3")

out = llm.invoke("Why is the sky blue?")
print(out)