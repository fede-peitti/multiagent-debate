from src.data.gsm8k import load_gsm8k_subset

questions = load_gsm8k_subset(n=3)

for q in questions:
    print("ID:", q.id)
    print("Q:", q.question)
    print("A:", q.answer)
    print("-" * 40)
