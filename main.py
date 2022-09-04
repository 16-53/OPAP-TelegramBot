import datetime
import logging
from pathlib import Path

from randomn import random_n
from result import res
from telebot import TeleBot, types

token = Path("token.txt").read_text().strip()
bot = TeleBot(token)
cache = None
next_result = None

@bot.message_handler(commands=["start", "help"])
def start(message):
    text = (
        "Commands:\n"
        "'/random_nums' - to get random numbers for your TZOKER Game (OPAP)\n"
        "'/results' - to get last results "
    )

    bot.send_message(message.chat.id, text, reply_markup=actions())


@bot.message_handler(commands=["random_nums"])
def random_numbers(message):
    numbers = random_n()
    text = f"Your 5 numbers: {str(numbers[0])[1:-1]}\nYour TZOKER number: {numbers[1]}"

    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["results"])
def last_results(message):
    global cache
    global next_result
    if cache is None:
        logging.info("Cache is empty")
        cache, text, next_result = res()[0], res()[1], res()[2]
        bot.send_message(message.chat.id, text)
    else:
        logging.info("Cache isn't empty")
        if (
            datetime.datetime.today().day < int(next_result[0])
            and datetime.datetime.today().month <= int(next_result[1])
            and datetime.datetime.today().year <= int(next_result[2])
        ) or (
            datetime.datetime.today().day == int(next_result[0])
            and datetime.datetime.today().month <= int(next_result[1])
            and datetime.datetime.today().year <= int(next_result[2])
            and datetime.datetime.today().hour < 20
        ):
            text = (
                f"Last results ({cache[0]}):\n"
                f"{cache[1][0]} {cache[1][1]} {cache[1][2]} {cache[1][3]} {cache[1][4]}\n"
                f"TZOKER number:\n"
                f"{cache[1][5]}"
            )
            bot.send_message(message.chat.id, text)
        else:
            cache, text, next_result = res()[0], res()[1], res()[2]
            bot.send_message(message.chat.id, text)


def actions():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    button_nums = types.KeyboardButton("/random_nums")
    button_results = types.KeyboardButton("/results")
    keyboard.add(button_nums, button_results)

    return keyboard


bot.polling(none_stop=True, interval=0)
