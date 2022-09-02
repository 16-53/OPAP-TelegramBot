import requests
from bs4 import BeautifulSoup
import re


def res():
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
    cache = [date, match]

    return cache, text
