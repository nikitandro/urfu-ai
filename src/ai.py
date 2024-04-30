from transformers import pipeline
from pathlib import Path
import re
import html
import json

current_path = Path(__file__).parent

translator_ru_to_en = pipeline("translation_ru_to_en", model="Helsinki-NLP/opus-mt-ru-en")

programming_languages = ('python', 'java', 'R', 'javascript', 'php')  # для модели попроще
specialities = json.loads((current_path / "specialities.json").read_text())  # для модели посложнее
current_model_dict = specialities

question_classification = pipeline("text-classification", model=current_path / "ready")

print("Models loaded.")


def pre_processing(text: str) -> str:
    text = re.sub('([!?])',r' \1 ',text)
    text = html.unescape(text)
    text = text.lower()
    return text


# следует сделать перевод с таймаутом, например перевод "ахй" напрягает процессор очень сильно
def translate(text: str, from_lang="ru", log=False) -> str:
    if log:
        print("Translating", from_lang, repr(text))

    if from_lang == "ru":
        translator = translator_ru_to_en
    else:
        raise ValueError("Invalid language pair")

    return translator(text)[0]["translation_text"]


def classify(text: str) -> tuple[str, float]:
    classified = question_classification.predict([pre_processing(text)])
    label = classified[0]["label"]
    converted_label = current_model_dict[int(label.split("_")[-1])]
    confidence = classified[0]["score"]
    return converted_label, confidence
