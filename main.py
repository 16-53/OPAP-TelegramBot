from telebot import TeleBot, types
from randomn import random_n
from pathlib import Path
import requests
from bs4 import BeautifulSoup
import re

token = Path("token.txt").read_text().strip()
bot = TeleBot(token)


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
    url = "https://www.opap.org.cy/en/joker/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    numbers = str(
        soup.find("div", class_="draw-results-numbers-wrap").find(
            "ul", class_="circles"
        )
    )
    match = re.findall(r"\d+", numbers)
    date = str(soup.find("span", class_="draw-number-warning"))[34:-7]
    text = (
        f"Last results ({date}):\n"
        f"{match[0]} {match[1]} {match[2]} {match[3]} {match[4]}\n"
        f"TZOKER number:\n"
        f"{match[5]}"
    )

    bot.send_message(message.chat.id, text)


def actions():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    button_nums = types.KeyboardButton("/random_nums")
    button_results = types.KeyboardButton("/results")
    keyboard.add(button_nums, button_results)

    return keyboard


bot.polling(none_stop=True, interval=0)
