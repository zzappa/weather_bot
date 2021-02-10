import logging
from io import BytesIO

import requests
from PIL import Image
from bs4 import BeautifulSoup

from bot_init import bot
from constants import radar_base_url, radar_minsk_gif_url, radar_grodno_url, radar_grodno_gif_url


def get_latest_radar(message):
    if message.text == '/radar_grodno':
        radar_url = radar_grodno_url
    else:
        radar_url = radar_base_url
    r = requests.get(radar_url)
    page = BeautifulSoup(r.text, "html5lib")

    links = []
    if 'grodno' in message.text:
        for img in page.findAll("img", {"alt": "Радар погоды UMMG. Карта метеоявлений"}):
            links.append(img)
    else:
        for img in page.findAll("img", {"alt": "Радар погоды UMMN. Карта метеоявлений"}):
            links.append(img)

    try:
        if 'grodno' in message.text:
            url = radar_base_url + links[0]['src'].lstrip('.')
        else:
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


def get_radar_gif(message):
    if message.text == '/radar_grodno_gif':
        radar_url = radar_grodno_gif_url
        title = f'[Анимация погодного радара ДМРЛ Гродно]({radar_url})'
    else:
        radar_url = radar_minsk_gif_url
        title = f'[Анимация погодного радара ДМРЛ Минск]({radar_url})'
    try:
        img = requests.get(radar_url)
        i = Image.open(BytesIO(img.content))
    except Exception:
        i = None
    if i:
        bot.send_message(message.from_user.id, title, parse_mode='Markdown')
    else:
        bot.reply_to(message, "Sorry, seems that radar is not working at the moment, try later.")
