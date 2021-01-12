import requests
from PIL import Image
from io import BytesIO
import logging

from constants import (weather_modes,
                       alt_models,
                       wrf3,
                       ukmet,
                       gem,
                       gfs,
                       fact_avia_cloud,
                       fact_avia_visib,
                       today,
                       today_06_utc,
                       today_12_utc,
                       today_18_utc)


def return_img(mode, interval='02', model='wrf3'):
    date = today
    if model.lower() == "avia/cloud":
        link = fact_avia_cloud
    elif model.lower() == "avia/vis":
        link = fact_avia_visib
    elif model.lower() in alt_models:
        if model.lower() in ('gfs', 'ncep'):
            link = gfs
            date = today_06_utc
        elif model.lower() in ('gem', 'cmc'):
            link = gem
        else:
            link = ukmet
    else:
        link = wrf3
    if len(interval) not in (2, 3):
        interval = '24'
    if mode in weather_modes:
        prefix = weather_modes[mode]
        for time in (date, today_06_utc, today_12_utc, today_18_utc):
            try:
                url = f'{link}{prefix}_{time}_{interval}.png'
                logging.warning(url)
                img = requests.get(url)
                i = Image.open(BytesIO(img.content))
                return i
            except Exception:
                pass
        return
