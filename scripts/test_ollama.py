from src.ollama.client import generate

question = "There are 10 apples and you eat 3. How many are left?"

print("LLaMA-2:")
print(generate("llama2:7b-chat", question, max_tokens=64))

print("\nAya:")
print(generate("aya:8b", question, max_tokens=64))
