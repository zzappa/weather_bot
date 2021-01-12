import telebot

from constants import weather_modes, alt_models
from actions import return_img

bot = telebot.TeleBot('insert-yout-token')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    msg = message.text.split(' ')
    if msg[0][1:] in weather_modes:
        try:
            if len(msg) == 3:
                i = return_img(msg[0][1:], msg[1], msg[2])
            elif len(msg) == 2:
                i = return_img(msg[0][1:], msg[1])
            else:
                i = return_img(msg[0][1:])
            if i != None:
                bot.send_photo(message.from_user.id, i)
            else:
                bot.send_message(message.from_user.id, "smth went wrong")
        except Exception:
            bot.send_message(message.from_user.id, "smth went wrong")
    else:
        bot.send_message(message.from_user.id, "smth went wrong")


bot.polling(none_stop=True, interval=0)
