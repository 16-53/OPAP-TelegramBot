import re

import requests
from bs4 import BeautifulSoup


def res():
    url = "https://www.opap.org.cy/en/joker/"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    next_res = str(soup.find("div", class_="day"))
    match_nextres = re.findall(r"\d+", next_res)
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

    return cache, text, match_nextres
