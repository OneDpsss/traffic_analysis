from app.handlers.load_csv import LoadCSVHandler
from app.handlers.clean_salary import CleanSalaryHandler
from app.handlers.extract_age import ExtractAgeHandler
from app.handlers.encode_gender import EncodeGenderHandler
from app.handlers.vectorize_text import VectorizeTextHandler
from app.handlers.build_xy import BuildXYHandler
from app.io.save_npy import SaveNpyHandler


def build_pipeline():
    load = LoadCSVHandler()
    salary = CleanSalaryHandler()
    age = ExtractAgeHandler()
    gender = EncodeGenderHandler()
    text = VectorizeTextHandler()
    build = BuildXYHandler()
    save = SaveNpyHandler()

    load.set_next(salary)\
        .set_next(age)\
        .set_next(gender)\
        .set_next(text)\
        .set_next(build)\
        .set_next(save)

    return load
