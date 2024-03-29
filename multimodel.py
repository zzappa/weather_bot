from io import BytesIO

import requests
from PIL import Image

from bot_init import bot
from constants import meteogram_link, multimodel_link, multimodel_verbose_link


def get_image(message, link, txt):
    try:
        r = requests.get(link)
        i = Image.open(BytesIO(r.content))
        text = f'{txt} [Source]({link})'
    except Exception:
        bot.reply_to(message, "Sorry, seems that something is broken, try later.")
    else:
        bot.send_photo(message.chat.id, i, text, parse_mode='Markdown')


def get_multimodel(message, mode):
    if mode == 'multimodel':
        txt = 'Multimodel ensemble forecast for Minsk for 7 days.'
        get_image(message, multimodel_link, txt)
    elif mode == 'multimodel_verbose':
        txt = 'Multimodel ensemble forecast for Minsk for 3 days.'
        get_image(message, multimodel_verbose_link, txt)
    elif mode == "meteogram":
        txt = 'Meteogram for Minsk for 5 days.'
        get_image(message, meteogram_link, txt)
