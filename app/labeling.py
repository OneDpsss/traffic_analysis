import re


def detect_level(position: str, experience_years: int):
    text = str(position).lower()

    if re.search(r"junior|джун", text):
        return "junior"

    if re.search(r"senior|lead|tech lead|тимлид", text):
        return "senior"

    if re.search(r"middle|мидл", text):
        return "middle"

    # fallback по опыту
    if experience_years <= 1:
        return "junior"
    if experience_years <= 4:
        return "middle"

    return "senior"
