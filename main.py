from telebot import TeleBot,types
from randomn import random_n
from pathlib import Path
token = Path('token.txt').read_text().strip()
bot = TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def start(message):
    text = "Write '/random_nums' to get random numbers for your joker game(OPAP)"
    bot.send_message(message.chat.id, text, reply_markup=actions())


@bot.message_handler(commands=['random_nums'])
def random_numbers(message):
    numbers = random_n()
    text = 'Your 5 numbers: ' + str(numbers[0])[1:-1] +\
           '\n' 'Your TZOKER number: ' + str(numbers[1])
    bot.send_message(message.chat.id, text)


def actions():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    button_nums = types.KeyboardButton('/random_nums')
    keyboard.add(button_nums)

    return keyboard


bot.polling(none_stop=True, interval=0)