### WeatherBot
WeatherBot может показывать различные погодные карты для Беларуси, полученные при моделировании погоды Белгидрометом, 
мультимодельные карты и метеограммы от Meteoblue, и данные с радара, установленного в аэропорту Минска. 
Доступные модели Белгидромета: WRF3, GFS, UKMET и GEM. 
Бот также может показывать прогноз погоды на 3 дня (от сервиса OpenWeather) и фактическую погоду в ~350 городах (Белгидромет).

![](img/weather_bot.png)

### Все доступные комманды
Пример использовани: /cmd xxx model_name, где: 
- cmd - комманда (тип погодной карты)
- xxx - число между 2 и 120 (ч). Для различных моделей и комманд доступны разные временные интервалы.
- model_name - модель ('wrf', 'wrf3'), ('egrr', 'ukmet'), ('gfs', 'ncep'), ('gem', 'cmc') или ('avia', 'fact') (синонимы даны в скобках).
##### Погодные карты WRF3, GEM, UKMET, GFS
- temp - температура воздуха и давление на 2 м
- rains - количество осадков, мм/ч
- wind - ветер, скорость и направление на 10 м
- rains_sum - сумма осадков за 6 ч
- apcp_phase - осадки, фазовое состояние
- fog - туман и осадки
- snow - снежный покров, высота
- xrefd - радиолокационная отражаемость, метеоявления
- xrefd_mx - радиолокационная отражаемость, максимальная
- ot-500-1000 - OT500-1000
- cape_ukr - энергия неустойчивости CAPE
- cape_180 - энергия неустойчивости CAPE180
- tmp925 - высота геопотенциала, ветер и температура на 925 гПа
- tmp850 - высота геопотенциала, ветер и температура на 850 гПа
- tmp700 - высота геопотенциала, ветер и температура на 700 гПа
- tmp500 - высота геопотенциала, ветер и температура на 500 гПа
- tmp300 - высота геопотенциала, ветер и температура на 300 гПа
- k_index - К индекс (вероятность грозы)
##### AVIA комманды
- vis - Карта дальности метеорологической видимости по данным аэропортов, Европа
- cloud - Карта высоты нижней границы облаков по данным метеостанций аэропортов, Европа

#### Получение фактической погоды в разных городах
Для получения фактической погоды, наберите название города на русском языке в любом регистре.

![](img/current_weather.png)

[Список доступных городов.](https://www.pogoda.by/rss2/)

#### Получение карты метеоявлений
Для получения карты метеоявлений с радара, установленного в аэропорту Минска, наберите /radar_minsk, для радара в Гродно - /radar_grodno. 
Анимированные радарные карты доступны по командам /radar_minsk_gif и /radar_grodno_gif.

![](img/radar.png)

Все погодные карты, фактические погодные данные и данные с радара взяты с сайта Белгидромета - [POGODA.BY](https://www.pogoda.by/).

#### Получение мультимодельных данных
Чтобы получить мультимодельные данные на 7 дней, наберите /multimodel. Для более подробного отчёта на 3 дня - /multimodel_verbose. По запросу /meteogram можно получить метеограмму Минска на 5 дней.  
Все данные получены с сайта [Meteoblue](https://www.meteoblue.com/).

![](img/multimodel.png)

#### Получение прогноза погоды на 3 дня
Для получения фактической погоды, наберите /weather <cityname>, например /weather Toronto. Без указания города будет показан прогноз погоды в Минске.  
Данные берутся из [OpenWeatherMap](https://openweathermap.org/).

![](img/forecast.png)
