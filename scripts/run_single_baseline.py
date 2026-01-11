import time

from src.agents.agent import Agent
from src.config.prompts import BASELINE_PROMPT
from src.data.gsm8k import load_gsm8k_subset
from src.eval.answer_extractor import extract_final_number

MODEL_NAME = "aya:8b"  # "llama2:7b-chat" || "aya:8b"
N_QUESTIONS = 100

# llama2:7b-chat on 100 questions: ~0.06 accuracy, ~9.19s per question
# aya:8b on 100 questions: ~0.05 accuracy, ~37.39s per question

agent = Agent(model_name=MODEL_NAME, role_prompt=BASELINE_PROMPT)
questions = load_gsm8k_subset(n=N_QUESTIONS)

correct = 0
times = []

for q in questions:
    start = time.perf_counter()

    response = agent.respond(question=q.format())
    predicted = extract_final_number(response)

    elapsed = time.perf_counter() - start
    times.append(elapsed)

    is_correct = predicted == q.answer
    correct += int(is_correct)

    print("=" * 60)
    print("Q:", q.question)
    print("MODEL:", response.strip())
    print("PRED:", predicted, "| GOLD:", q.answer, "| CORRECT:", is_correct)
    print(f"TIME: {elapsed:.2f} seconds")

accuracy = correct / N_QUESTIONS
avg_time = sum(times) / len(times)

print("\nFINAL ACCURACY:", accuracy)
print(f"AVERAGE TIME PER QUESTION: {avg_time:.2f} seconds")
