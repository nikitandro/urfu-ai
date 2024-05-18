from typing import Tuple

import ai

welcome_message = "Здравствуйте! Я - бот. Напишите что-нибудь."
accepted_characters = [
    ["а", "я"],
    ["А", "Я"],
    ["0", "9"],
    ["a", "z"],
    ["A", "Z"],
    ".,?!: ",
]

class ModelOutput:
    lang: str
    tag: str
    probability: float

    def __init__(self, lang: str, tag: str, probability: float):
        self.lang = lang
        self.tag = tag
        self.probability = probability

    def __str__(self):
        return f"lang: {self.lang}, tag: {self.tag}, probability: {self.probability}"

def process_input(message_text: str) -> ModelOutput:
    response = ai.classify(ai.translate(message_text))
    lang_tag = response[0].split('-', 1)
    lang = lang_tag[0]
    tag = lang_tag[1]
    probability = response[1]
    return ModelOutput(lang, tag, probability)
