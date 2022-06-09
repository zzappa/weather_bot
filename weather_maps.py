import datetime
from io import BytesIO

import requests
from PIL import Image

from bot_init import bot
from constants import weather_modes


def get_weather_map(message, mode):

    if mode in ('temp', 'led'):
        img = requests.get(weather_modes[mode])
    elif mode == 'satellite':
        today = datetime.date.today().strftime("%Y%m%d")
        print(today)
        now = datetime.datetime.now()
        n = now.hour - 3
        img = requests.get(f'{weather_modes[mode]}-{today}1100.jpg')
        while b"""\xff""" not in img.content:
            s1 = f'{n:02d}'
            img = requests.get(f'{weather_modes[mode]}_{today}00_{s1}.png')
            n -= 1
    else:
        today = datetime.date.today().strftime("%Y%m%d")
        print(today)
        now = datetime.datetime.now()
        n = now.hour - 3
        img = requests.get(f'{weather_modes[mode]}_11111111_11.png')
        while b"""\x89PNG""" not in img.content:
            s1 = f'{n:02d}'
            img = requests.get(f'{weather_modes[mode]}_{today}00_{s1}.png')
            n -= 1
    title = None
    i = Image.open(BytesIO(img.content))
    try:
        bot.send_photo(message.from_user.id, i, title)
    except:
        bot.reply_to(message, "Sorry, seems that radar is not working at the moment, try later.")
