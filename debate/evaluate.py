import re
from collections import Counter


def extract_number(text):
    numbers = re.findall(r"-?\d+\.?\d*", text)
    return numbers[-1] if numbers else None


def majority_vote(answers):
    extracted = [extract_number(a) for a in answers]
    counts = Counter(extracted)
    return counts.most_common(1)[0][0]
