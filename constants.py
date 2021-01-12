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
                 "fact/cloud": "HIGH_CL_"}

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

fact_avia_cloud = 'https://meteoinfo.by/maps/fact/HIGH_CL_'
fact_avia_visib = 'https://meteoinfo.by/maps/fact/AVIA_VISIB_'

today = datetime.date.today().strftime("%Y%m%d%H")
today_06_utc = today[:-1] + '6'
today_12_utc = today[:-2] + '12'
today_18_utc = today[:-2] + '18'