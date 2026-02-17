import pandas as pd
import re
from app.utils import extract_age, extract_experience_years
from app.labeling import detect_level


def parse_salary(s):
    if not isinstance(s, str):
        return 0
    s = s.replace("\xa0", "").replace(" ", "")
    match = re.search(r"\d+", s)
    if match:
        return float(match.group())
    return 0


def load_and_prepare(path):
    df = pd.read_csv(path)

    df["age"] = df["Пол, возраст"].apply(extract_age)
    df["experience_years"] = df[
        "Опыт (двойное нажатие для полной версии)"
    ].apply(extract_experience_years)

    df["position"] = df["Ищет работу на должность:"]
    df["city"] = df["Город"]
    df["salary"] = df["ЗП"].apply(parse_salary)

    df["y"] = df.apply(
        lambda row: detect_level(
            row["position"],
            row["experience_years"],
        ),
        axis=1,
    )

    df = df.dropna(subset=["position"])

    return df
