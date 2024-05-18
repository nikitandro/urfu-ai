import model_communication
import json
import telebot

with open("src/langs.json", 'r', encoding='utf-8-sig') as file:
    langs = json.load(file)

class BotResponse:
    model_output: model_communication.ModelOutput

    def __init__(self, model_output: model_communication.ModelOutput):
        self.model_output = model_output

    def get_output(self) -> str:
        if self.model_output.probability < 0.3:
            return self.get_fallback_output()

        return telebot.formatting.format_text(
            "<strong>Вот, что удалось найти по вашему запросу</strong>",
            "",
            f"<a href='{self.get_stackoverflow_url()}'>Stackoverflow</a>",
            f"<a href='{self.get_habr_url()}'>Habr</a>",
            "",
            *self.get_formatted_doc(),
            "",
            *self.get_formatted_communities()
        )

    def get_fallback_output(self) -> str:
        return "К сожалению, по вашему запросу не удалось найти ответ :("

    def get_formatted_communities(self) -> list[str]:
        communities = self.get_communities()
        if communities is None:
            return []
        return ["<strong>Сообщества</strong>", "\n".join(communities)]

    def get_formatted_doc(self) -> list[str]:
        doc = self.get_doc()

        if doc is None:
            return []

        return ["<strong>Документация</strong>", self.get_doc()]

    def get_communities(self) -> list[str] | None:
        try:
            return langs["communities"][self.model_output.lang][self.model_output.tag]
        except KeyError:
            return None

    def get_doc(self) -> str | None:
        try:
            return langs["docs"][self.model_output.lang][self.model_output.tag]
        except KeyError:
            return None

    def get_stackoverflow_url(self) -> str:
        if self.model_output.tag == "GENERAL":
            return f"https://stackoverflow.com/questions/tagged/{self.model_output.lang}"
        return f"https://stackoverflow.com/questions/tagged/{self.model_output.lang}+{self.model_output.tag}"

    def get_habr_url(self) -> str:
        if self.model_output.tag == "GENERAL":
            return "https://habr.com/ru/search/?q={" + self.model_output.lang + "}&target_type=posts&order=relevance"
        return "https://habr.com/ru/search/?q={" + self.model_output.lang + "}+{" + self.model_output.tag + "}&target_type=posts&order=relevance"