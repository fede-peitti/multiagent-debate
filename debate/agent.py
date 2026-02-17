from openai import OpenAI
import os


class DebateAgent:
    def __init__(self, agent_id, model_name, system_prompt):
        self.agent_id = agent_id
        self.model_name = model_name
        self.system_prompt = system_prompt

        api_key = os.environ.get("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not set")

        self.client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1",
        )

    def generate(self, user_prompt):
        full_prompt = f"""You are Agent {self.agent_id}.

{self.system_prompt}

Task:
{user_prompt}
"""

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[{"role": "user", "content": full_prompt}],
            temperature=0,
        )

        return response.choices[0].message.content
