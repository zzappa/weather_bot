import telebot
import random

from constants import weather_modes, alt_models, stickers
from cities import cities
from actions import get_weather_map, get_current_weather

bot = telebot.TeleBot('insert-yout-token')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    def _send_error_msg():
        bot.send_sticker(message.chat.id, random.choice(stickers))
        bot.send_message(message.from_user.id, "smth went wrong :(")
    msg = message.text.split(' ')
    if msg[0][1:] in weather_modes:
        try:
            if len(msg) == 3:
                i = get_weather_map(msg[0][1:], msg[1], msg[2])
            elif len(msg) == 2:
                i = get_weather_map(msg[0][1:], msg[1])
            else:
                i = get_weather_map(msg[0][1:])
            if i != None:
                bot.send_photo(message.from_user.id, i)
            else:
                _send_error_msg()
        except Exception:
            _send_error_msg()
    elif msg[0].lower() in cities:
        current_weather = get_current_weather(cities[msg[0].lower()])
        if current_weather:
            bot.send_message(message.from_user.id, current_weather)
        else:
            _send_error_msg()
    else:
        _send_error_msg()


bot.polling(none_stop=True, interval=0)
