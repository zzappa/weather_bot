import logging
from io import BytesIO

import requests
from PIL import Image
from bs4 import BeautifulSoup

from bot_init import bot
from constants import radar_url


def get_latest_radar(message):
    r = requests.get(radar_url)
    page = BeautifulSoup(r.text, "html5lib")

    links = []
    for img in page.findAll("img", {"alt": "Радар погоды UMMN. Карта метеоявлений"}):
        links.append(img)

    try:
        url = radar_url + links[0]['src'].lstrip('.')
        title = links[0]['title']
        logging.warning(url)
        logging.warning(title)
        img = requests.get(url)
        i = Image.open(BytesIO(img.content))
    except Exception:
        i = None
        title = None
    if i:
        bot.send_photo(message.chat.id, i, title)
    else:
        bot.reply_to(message, "Sorry, seems that radar is not working at the moment, try later.")
