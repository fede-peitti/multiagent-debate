from agent import DebateAgent
from debate import run_debate
from dataset import load_gsm8k
from evaluate import majority_vote

MODELS = {
    "gemma_multilingual": "google/gemma-3-27b-it:free",
    "gpt_oss_english": "openai/gpt-oss-20b:free",
}

N_AGENTS = 7
N_ROUNDS = 2

dataset = load_gsm8k(115)  # max 1319

for label, model_name in MODELS.items():
    print("\n" + "#" * 80)
    print(f"MODEL: {label}")
    print("#" * 80)

    agents = [
        DebateAgent(
            agent_id=i,
            model_name=model_name,
            system_prompt="""You are a careful, logical problem solver. 
                            After thorough reasoning, provide a concise final answer. 
                            It should be numerical, without units. 
                            Example: 'FINAL ANSWER: 123456000', or 'FINAL ANSWER: -22.0'.""",
        )
        for i in range(N_AGENTS)
    ]

    correct = 0

    for idx, item in enumerate(dataset):
        print("\n" + "-" * 80)
        print(f"Question {idx + 1}")
        print("-" * 80)
        print(item["question"])

        answers = run_debate(item["question"], agents, N_ROUNDS)

        print("\nAgent responses:")
        for i, ans in enumerate(answers):
            print(f"\n[Agent {i}]")
            print(ans)

        final = majority_vote(answers)
        gold = item["answer"].split()[-1]

        is_correct = final == gold
        correct += int(is_correct)

        print("\nFinal extracted answer:", final)
        print("Gold answer:", gold)
        print("Correct:", is_correct)

    print("\n" + "=" * 80)
    print(f"FINAL ACCURACY for {label}: {correct}/{len(dataset)}")
    print("=" * 80)
