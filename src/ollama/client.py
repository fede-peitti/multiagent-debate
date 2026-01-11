import requests

OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"


def generate(
    model: str,
    prompt: str,
    max_tokens: int = 128,
    temperature: float = 0.0,
):
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "options": {
            "temperature": temperature,
            "num_predict": max_tokens,
            "stop": ["\n"],
        },
        "stream": False,
    }

    response = requests.post(OLLAMA_CHAT_URL, json=payload)
    response.raise_for_status()

    return response.json()["message"]["content"]
