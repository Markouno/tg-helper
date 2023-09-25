import telebot
from tokens import tg_token
from datetime import datetime

bot = telebot.TeleBot(tg_token)
run_date = datetime.now()

@bot.message_handler(commands=['start', 'старт'])
def main(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!')
    bot.send_message(message.chat.id, f'Укажи свой код ошибки, я помогу разобраться!')

@bot.message_handler()
def send_msg(message):
    try:
        bot.send_photo(message.chat.id, f'https://http.cat/{message.text}.jpg', caption='Лови!')

    except:
        bot.send_message(message.chat.id, f'Не нашел ничего по коду {message.text}. Может ошибся цифрой?')

    meta_data = f'{run_date} - {message.from_user.first_name} - {message.text}\n'

    with open('main.log', 'a', encoding='UTF-8') as log_file:
                log_file.writelines(meta_data)




bot.polling(none_stop=True)