def run_debate(question, agents, n_rounds=3):
    answers = []

    # Round 0: independent answers
    for agent in agents:
        ans = agent.generate(f"Question:\n{question}\n\nAnswer step by step.")
        answers.append(ans)

    # Debate rounds
    for r in range(1, n_rounds):
        new_answers = []
        for i, agent in enumerate(agents):
            others = "\n\n".join(
                f"Agent {j} answer:\n{answers[j]}" for j in range(len(agents)) if j != i
            )

            prompt = f"""
Question:
{question}

Other agents' answers:
{others}

Carefully critique the other answers and provide a revised final answer.
"""
            revised = agent.generate(prompt)
            new_answers.append(revised)

        answers = new_answers

    return answers
