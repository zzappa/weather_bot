import datetime

# stickers for error messages
stickers = ['CAACAgIAAxkBAAEBwoJf_Ulg-lcGG-e-pDjxCytVeN-W6wAC8wADVp29Cmob68TH-pb-HgQ',
            'CAACAgIAAxkBAAEBwoRf_Ulmdoyt4eGL7jGZEwveO2zJ2AACCQEAAladvQrWZlyD1z-oHR4E',
            'CAACAgIAAxkBAAEBwoZf_UlsfCSz9YJmqIVDNEMiaT_U7gACTQIAAladvQoLpdXvP7GXfx4E'
            'CAACAgIAAxkBAAEBwpRf_Vn-I2DCn85s8_mlC4y6DlbCUwACCwEAAladvQpOseemCPvtSR4E',
            'CAACAgIAAxkBAAEBwpJf_VnxzbcjvW3KZzlYmwXbhSABxgACBQEAAladvQq35P22DkVfdx4E',
            'CAACAgIAAxkBAAEBwpBf_VniIPtKoKewheioB8H9HOnDAQACcgQAAuce7AXKSuGZ_F_atx4E',
            'CAACAgIAAxkBAAEBwo5f_Vnd1SqhOWRjF8uGuzhZzdTCMQACagQAAuce7AW6DxsEpcJEyR4E',
            'CAACAgIAAxkBAAEBwoxf_VnZIyRszXaUx2rhMbwaXity3QACXAQAAuce7AUmmbsbikWzNB4E',
            'CAACAgIAAxkBAAEBwopf_VnV4jGR1H3TEbm6DXuhn_JE5AACQAQAAuce7AXntkQVeFOqGh4E',
            'CAACAgIAAxkBAAEBwohf_VnPmvoUIRCmuoqy_lwYzoJ1GAACIQQAAuce7AWY2vXU1ZNj6x4E']

cold_sticker = 'CAACAgIAAxkBAAEBwoRf_Ulmdoyt4eGL7jGZEwveO2zJ2AACCQEAAladvQrWZlyD1z-oHR4E'
hot_sticker = 'CAACAgIAAxkBAAEBwoxf_VnZIyRszXaUx2rhMbwaXity3QACXAQAAuce7AUmmbsbikWzNB4E'
rains_sticker = 'CAACAgIAAxkBAAEBwoZf_UlsfCSz9YJmqIVDNEMiaT_U7gACTQIAAladvQoLpdXvP7GXfx4E'

temp = 'https://pogoda.by/files/maps/static/fact/RB_TNOW.png'
led = 'https://pogoda.by/files/hydrology/kartaLed.jpg'

# check all https://pogoda.by/observation/satellite
satellite = 'https://pogoda.by/files/satellite/small_031'

rains = 'https://pogoda.by/files/maps/static/fact/RB_PRC_SYN'
winds = 'https://pogoda.by/files/maps/static/fact/AVIA_WIND'
visibility = 'https://pogoda.by/files/maps/static/fact/AVIA_VISIB'
clouds = 'https://pogoda.by/files/maps/static/fact/HIGH_CL'

# all available weather maps
weather_modes = {'rains': rains,
                 'temp':temp,
                 'satellite': satellite,
                 'winds': winds,
                 'led': led,
                 'visibility': visibility,
                 'clouds': clouds}

days = []
for n in range(3):
    day = (datetime.date.today() - datetime.timedelta(days=n)).strftime("%Y%m%d%H")
    days.append(day)
    days.append(day[:-1] + '6')
    days.append(day[:-2] + '12')
    days.append(day[:-2] + '18')

radar_base_url = 'https://pogoda.by/files/radars/static/26850/Radar_26850_MAP_PHEN'
radar_grodno_url = 'https://pogoda.by/files/radars/static/26825/Radar_26825_MAP_PHEN'

meteogram_link = 'https://my.meteoblue.com/visimage/meteogram_web?look=KILOMETER_PER_HOUR%2CCELSIUS%2CMILLIMETER&apikey=5838a18e295d&temperature=C&windspeed=kmh&precipitationamount=mm&winddirection=3char&city=Minsk&iso2=by&lat=53.900002&lon=27.566700&asl=222&tz=Europe%2FMinsk&lang=en&sig=dbcada2a841254b6da8faf27fae14e33'
multimodel_link = 'https://my.meteoblue.com/visimage/meteogram_ensemblemembers_hd?look=KILOMETER_PER_HOUR%2CCELSIUS%2CMILLIMETER&apikey=5838a18e295d&temperature=C&windspeed=kmh&precipitationamount=mm&winddirection=3char&city=Minsk&iso2=by&lat=53.9&lon=27.5667&asl=222&tz=Europe%2FMinsk&fcstlength=168&lang=en&ts=1640862148&sig=c4abe46e04721582cf6aa1d0e2e145c8'
multimodel_verbose_link = 'https://my.meteoblue.com/visimage/meteogram_multiSimple_hd?look=KILOMETER_PER_HOUR%2CCELSIUS%2CMILLIMETER&apikey=5838a18e295d&temperature=C&windspeed=kmh&precipitationamount=mm&winddirection=3char&city=Minsk&iso2=by&lat=53.9&lon=27.5667&asl=222&tz=Europe%2FMinsk&dt=1&fcstlength=72&lang=en&ts=1640862185&sig=c42dcaf2bab6157a001298c9b3975a13'
