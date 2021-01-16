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

# all available weather maps
weather_modes = {"rains": "APCP",
                 "temp": "TMP2m",
                 "wind": "GUST10m",
                 "rains_sum": "APCPDG",
                 "apcp_phase": "APCP_PHASE",
                 "fog": "FG",
                 "snow": "SNOD",
                 "xrefd": "xREFD",
                 "xrefd_mx": "REFC",
                 "ot": "OT500_1000",
                 "cape_ukr": "CAPE_UKR",
                 "cape_180": "CAPE_180",
                 "tmp925": "TMP925",
                 "tmp850": "TMP850",
                 "tmp700": "TMP700",
                 "tmp500": "TMP500",
                 "tmp300": "TMP300",
                 "k_index": "KIND",
                 "vis": "AVIA_VISIB",
                 "cloud": "HIGH_CL"}

# all available weather prediction models, with synonyms
wrf3 = 'https://meteoinfo.by/maps/wrf3/images-00/'
wrf = wrf3
ukmet = 'https://meteoinfo.by/maps/egrr/'
egrr = ukmet
gfs = 'https://meteoinfo.by/maps/ncep/'
ncep = gfs
gem = 'https://meteoinfo.by/maps/cmc/'
cmc = gem
navgem = 'https://meteoinfo.by/maps/ngps/'
ngps = navgem

alt_models = ('egrr', 'ukmet', 'gfs', 'ncep', 'gem', 'cmc', 'ngps', 'navgem')

# link to avia maps
fact = 'https://meteoinfo.by/maps/fact/'

days = []
for n in range(3):
    day = (datetime.date.today() - datetime.timedelta(days=n)).strftime("%Y%m%d%H")
    days.append(day)
    days.append(day[:-1] + '6')
    days.append(day[:-2] + '12')
    days.append(day[:-2] + '18')
