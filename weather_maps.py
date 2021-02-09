import logging
from io import BytesIO

import requests
from PIL import Image

from constants import (weather_modes,
                       alt_models,
                       wrf3,
                       ukmet,
                       gem,
                       gfs,
                       fact,
                       days)


def get_weather_map(mode, interval='02', model='wrf3'):
    link = _get_link(model)
    if len(interval) not in (2, 3):
        interval = '24'
    if mode in weather_modes:
        prefix = weather_modes[mode]
        for day in days:
            try:
                url = f'{link}{prefix}_{day}_{interval}.png'
                logging.warning(url)
                logging.warning((mode, interval, model))
                img = requests.get(url)
                i = Image.open(BytesIO(img.content))
                return i
            except Exception:
                pass
        return


def _get_link(model='wrf3'):
    if model.lower() in ("avia", "fact"):
        link = fact
    elif model.lower() in alt_models:
        if model.lower() in ('gfs', 'ncep'):
            link = gfs
        elif model.lower() in ('gem', 'cmc'):
            link = gem
        else:
            link = ukmet
    else:
        link = wrf3
    return link
