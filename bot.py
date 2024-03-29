import random

from bot_init import bot
from cities import cities
from constants import weather_modes, stickers
from current_weather import get_current_weather
from forecast import get_forecast
from multimodel import get_multimodel
from radar import get_latest_radar
from weather_maps import get_weather_map


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    def _send_error_msg():
        bot.send_sticker(message.chat.id, random.choice(stickers))
        bot.send_message(message.from_user.id, "smth went wrong :(")

    msg = message.text.split(' ')
    if msg[0][1:] in weather_modes:
        get_weather_map(message, msg[0][1:])
    elif msg[0].lower() in cities:
        current_weather = get_current_weather(cities[msg[0].lower()])
        if current_weather:
            bot.reply_to(message, current_weather)
        else:
            _send_error_msg()
    elif msg[0] == '/forecast':
        get_forecast(message)
    elif msg[0] in ('/radar_minsk', '/radar_grodno'):
        get_latest_radar(message)
    elif msg[0] == '/multimodel':
        get_multimodel(message, mode='multimodel')
    elif msg[0] == '/multimodel_verbose':
        get_multimodel(message, mode='multimodel_verbose')
    elif msg[0] == '/meteogram':
        get_multimodel(message, mode='meteogram')
    else:
        pass


bot.polling(none_stop=True, interval=0)
