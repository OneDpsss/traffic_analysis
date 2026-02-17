import re


def extract_age(text: str):
    if not isinstance(text, str):
        return None

    match = re.search(r"(\d+)", text)
    if match:
        return int(match.group(1))
    return None


def extract_experience_years(text: str):
    if not isinstance(text, str):
        return 0

    match = re.search(r"(\d+)\s*год", text)
    if match:
        return int(match.group(1))
    return 0
