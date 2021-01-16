import logging

import pyowm

from bot_init import bot, owm_token
from constants import cold_sticker, hot_sticker, rains_sticker


def get_forecast(message):
    owm = pyowm.OWM(owm_token)
    mgr = owm.weather_manager()
    default_city = 'Minsk'
    msg = message.text.lstrip('/weather ')
    logging.warning(msg)
    try:
        try:
            place = msg
            observation = mgr.weather_at_place(msg)
            forecast = mgr.forecast_at_place(msg, '3h')
        except Exception:
            place = default_city
            observation = mgr.weather_at_place(place)
            forecast = mgr.forecast_at_place(place, '3h')
        temp = observation.weather.temperature('celsius')['temp']
        feels_like = observation.weather.temperature('celsius')['feels_like']
        logging.warning(feels_like)
        curr_status = observation.weather.status
        my_fc_temps = []
        my_fc_statuses = []
        for wth in forecast.forecast:
            my_fc_temps.append(wth.temperature('celsius'))
            my_fc_statuses.append(wth.status)
        else:
            forecast = "The current temperature in {} is {} C, " \
                       "and it feels like {}. Current conditions - {}.\n\n" \
                       "In 3h it will be {} C, feels like {}, and {}.\n" \
                       "In 6h it will be {} C, feels like {}, and {}.\n" \
                       "Toworrow it will be {} C, feels like {}, and {}.\n" \
                       "In 2 days it will be {} C, feels like {}, and {}.\n" \
                       "In 3 days it will be {} C, feels like {}, and {}.\n".format(place, temp, feels_like,
                                                                                    curr_status,
                                                                                    my_fc_temps[1]['temp'],
                                                                                    my_fc_temps[1]['feels_like'],
                                                                                    my_fc_statuses[1],
                                                                                    my_fc_temps[2]['temp'],
                                                                                    my_fc_temps[2]['feels_like'],
                                                                                    my_fc_statuses[2],
                                                                                    my_fc_temps[8]['temp'],
                                                                                    my_fc_temps[8]['feels_like'],
                                                                                    my_fc_statuses[8],
                                                                                    my_fc_temps[16]['temp'],
                                                                                    my_fc_temps[16]['feels_like'],
                                                                                    my_fc_statuses[16],
                                                                                    my_fc_temps[24]['temp'],
                                                                                    my_fc_temps[24]['feels_like'],
                                                                                    my_fc_statuses[24])
        if feels_like <= -15:
            bot.send_sticker(message.from_user.id, cold_sticker)
        elif feels_like >= 27:
            bot.send_sticker(message.from_user.id, hot_sticker)
        elif "rain" or "snow" in str(curr_status).lower():
            bot.send_sticker(message.from_user.id, rains_sticker)
        bot.reply_to(message, forecast)
    except pyowm.commons.exceptions.UnauthorizedError:
        bot.reply_to(message, 'Sorry, try again')
