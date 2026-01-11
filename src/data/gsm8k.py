from dataclasses import dataclass
from datasets import load_dataset


@dataclass
class GSM8KQuestion:
    id: int
    question: str
    answer: int

    def format(self) -> str:
        """Return the question text to present to an agent."""
        return self.question


def load_gsm8k_subset(split="test", n=5):
    dataset = load_dataset("gsm8k", "main", split=split)

    questions = []
    for i in range(n):
        item = dataset[i]
        # GSM8K format extraction
        answer_str = item["answer"]
        numeric_answer = int(answer_str.split("####")[-1].strip())

        questions.append(
            GSM8KQuestion(id=i, question=item["question"], answer=numeric_answer)
        )

    return questions
