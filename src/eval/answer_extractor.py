import re


def extract_final_number(text: str):
    """
    Extract the final integer appearing in the text.
    Returns None if no integer is found.
    """
    numbers = re.findall(r"-?\d+", text)
    if not numbers:
        return None
    return int(numbers[-1])
