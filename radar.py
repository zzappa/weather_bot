import datetime
from io import BytesIO

import requests
from PIL import Image

from bot_init import bot
from constants import radar_base_url, radar_grodno_url


def get_latest_radar(message):
    if message.text == '/radar_grodno':
        radar_url = radar_grodno_url
        title = "Радар Гродно"
    else:
        radar_url = radar_base_url
        title = "Радар Минск"

    today = datetime.date.today().strftime("%Y%m%d")
    print(today)
    now = datetime.datetime.now()

    n = int(str(now.hour - 3) + str(now.minute))
    img = requests.get(f'{radar_url}_111111_1111.png')
    while b"""\x89PNG""" not in img.content:
        s1 = f'{n:04d}'
        img = requests.get(f'{radar_url}_{today}_{s1}.png')
        n -= 1

    i = Image.open(BytesIO(img.content))

    if i:
        bot.send_photo(message.chat.id, i, title)
    else:
        bot.reply_to(message, "Sorry, seems that radar is not working at the moment, try later.")
