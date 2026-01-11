from src.agents.agent import Agent
from src.config.prompts import SOLVER_PROMPT

agent = Agent(model_name="llama2:7b-chat", role_prompt=SOLVER_PROMPT)

question = "If you have 10 candies and give away 4, how many remain?"

response = agent.respond(question=question)

print("AGENT RESPONSE:")
print(response)
