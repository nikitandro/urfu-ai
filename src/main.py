import telebot
from model_communication import welcome_message, accepted_characters, process_input
import bot_response

with open("src/token.txt") as file:
    bot = telebot.TeleBot(file.read())

def filter_text(message_text: str):
    return_text = ""
    for char in message_text:
        for char_range in accepted_characters:
            if (isinstance(char_range, list) and
                char_range[0] <= char <= char_range[1]) \
                    or (isinstance(char_range, str) and char in char_range):
                return_text += char
    return return_text


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, welcome_message)
    else:
        try:
            bot.send_message(message.chat.id, get_output(message.text), parse_mode='HTML')
        except Exception as e:
            print(e)

def get_output(input_str: str) -> str:
    model_response = process_input(filter_text(input_str))
    bot_res = bot_response.BotResponse(model_response)
    output = bot_res.get_output()
    return output

print("Bot is starting")
bot.polling(none_stop=True, interval=0)
