import datetime

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
                 "fact/vis": "AVIA_VISIB",
                 "fact/cloud": "HIGH_CL"}

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

fact = 'https://meteoinfo.by/maps/fact/'

days = []
for n in range(3):
    day = (datetime.date.today() - datetime.timedelta(days=n)).strftime("%Y%m%d%H")
    days.append(day)
    days.append(day[:-1] + '6')
    days.append(day[:-2] + '12')
    days.append(day[:-2] + '18')
