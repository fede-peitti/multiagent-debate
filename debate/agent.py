from openai import OpenAI
import os


class DebateAgent:
    def __init__(self, agent_id, model_name, system_prompt):
        self.agent_id = agent_id
        self.model_name = model_name
        self.system_prompt = system_prompt

        self.client = OpenAI(
            api_key=os.environ["OPENROUTER_API_KEY"],
            base_url="https://openrouter.ai/api/v1",
        )

    def generate(self, user_prompt):
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0,
        )
        return response.choices[0].message.content
