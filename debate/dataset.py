from datasets import load_dataset


def load_gsm8k(n=10):
    data = load_dataset("gsm8k", "main", split="test")
    return data.select(range(n))
