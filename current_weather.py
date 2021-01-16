import requests
import re
import html
import logging

from cities import url


def get_current_weather(city):
    try:
        link = url + city
        logging.warning(link)
        r = requests.get(link)
        date = re.findall('<pubDate>.*<\/pubDate>', r.text)
        desc = re.findall('<description>.*<\/description>', r.text)
        date = date[0].lstrip('<pubDate>').rstrip('</pubDate>')
        desc = html.unescape(desc[1]).lstrip('<description><![CDATA[').rstrip(']]></description>').replace('| ', '\n')
        weather = date + '\n' + desc
        logging.warning(weather)
    except Exception:
        weather = None
    return weather
