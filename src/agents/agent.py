from src.ollama.client import generate
from src.config.generation import GENERATION_CONFIG


class Agent:
    def __init__(self, model_name: str, role_prompt: str):
        """
        model_name: Ollama model tag (e.g., 'llama2:7b-chat')
        role_prompt: Prompt template defining the agent's role
        """
        self.model_name = model_name
        self.role_prompt = role_prompt
        self.history = []

    def respond(self, **prompt_vars) -> str:
        """
        Generate a response given prompt variables.
        The formatted prompt is appended to history.
        """
        prompt = self.role_prompt.format(**prompt_vars)

        response = generate(
            model=self.model_name,
            prompt=prompt,
            max_tokens=GENERATION_CONFIG["max_tokens"],
            temperature=GENERATION_CONFIG["temperature"],
        )

        self.history.append({"prompt": prompt, "response": response})

        return response
