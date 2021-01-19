import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup


from bot_init import bot

meteogram_link = 'https://my.meteoblue.com/visimage/meteogram_web?look=KILOMETER_PER_HOUR%2CCELSIUS%2CMILLIMETER&apikey=5838a18e295d&temperature=C&windspeed=kmh&precipitationamount=mm&winddirection=3char&city=Minsk&iso2=by&lat=53.900002&lon=27.566700&asl=222&tz=Europe%2FMinsk&lang=en&sig=dbcada2a841254b6da8faf27fae14e33'
multimodel_link = 'https://www.meteoblue.com/en/weather/forecast/multimodelensemble/minsk_belarus_625144'
multimodel_verbose_link = 'https://www.meteoblue.com/en/weather/forecast/multimodel/minsk_belarus_625144'


def get_image(message, link, txt, soup=True):
    if not soup:
        url = meteogram_link
    else:
        r = requests.get(link)
        soup = BeautifulSoup(r.text, "html5lib")
        links = []
        for img in soup.findAll("a"):
            if 'Minsk' in str(img):
                links.append(img)
        url = "https:" + links[2]['href']
    try:
        r = requests.get(url)
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
        txt = 'Multimodel for Minsk for 3 days.'
        get_image(message, multimodel_verbose_link, txt)
    elif mode == "meteogram":
        txt = 'Meteogram for Minsk for 5 days'
        get_image(message, meteogram_link, txt, soup=False)
