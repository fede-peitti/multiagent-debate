import time
from experiment_grid import EXPERIMENT_GRID
from agent import DebateAgent
from debate import run_debate
from dataset import load_gsm8k
from evaluate import majority_vote
from results.logger import log_result

# -----------------------------
# Global experiment parameters
# -----------------------------
NUM_QUESTIONS = 10
SYSTEM_PROMPT = "You are a careful, logical problem solver."
SLEEP_BETWEEN_CALLS = 1.0  # rate-limit safety


def run_single_config(config, dataset):
    agents = [
        DebateAgent(agent_id=i, model_name=config["model"], system_prompt=SYSTEM_PROMPT)
        for i in range(config["agents"])
    ]

    correct = 0
    per_question = []

    for idx, item in enumerate(dataset):
        answers = run_debate(
            question=item["question"], agents=agents, n_rounds=config["rounds"]
        )

        final_answer = majority_vote(answers)
        gold_answer = item["answer"].split()[-1]

        is_correct = final_answer == gold_answer
        correct += int(is_correct)

        per_question.append(
            {
                "question_id": idx,
                "final_answer": final_answer,
                "gold_answer": gold_answer,
                "correct": is_correct,
            }
        )

        time.sleep(SLEEP_BETWEEN_CALLS)

    accuracy = correct / len(dataset)

    return {
        "model": config["model"],
        "model_label": config["model_label"],
        "num_agents": config["agents"],
        "num_rounds": config["rounds"],
        "dataset": "gsm8k",
        "num_questions": len(dataset),
        "accuracy": accuracy,
        "correct": correct,
        "details": per_question,
    }


def main():
    dataset = load_gsm8k(NUM_QUESTIONS)

    for i, config in enumerate(EXPERIMENT_GRID):
        print(
            f"\n[{i+1}/{len(EXPERIMENT_GRID)}] "
            f"Model={config['model_label']} | "
            f"Agents={config['agents']} | "
            f"Rounds={config['rounds']}"
        )

        result = run_single_config(config, dataset)
        log_result(result)

        print(f"→ Accuracy: {result['accuracy']:.2f}")


if __name__ == "__main__":
    main()
