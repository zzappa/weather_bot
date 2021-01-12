# code to recreate cities dict
# r = requests.get('https://www.pogoda.by/rss2/')
# soup = BeautifulSoup(r.text, 'html.parser')
# all = []
# for a in soup.find_all('a'):
#     all.append(a)
#
# all2 = [str(a) for a in all if '<a href="/rss2/cityrss.php?q' in str(a)]
# all2 = [a.split('погода ') for a in all2]
# all2 = [a[-1].rstrip('</a>').split('Индекс ВМО: ')[-1].replace('">', ' ').replace() for a in all2]
# cities = {a.split(' ')[1]: a.split(' ')[0].lower() for a in all2}

url = 'https://www.pogoda.by/rss2/cityrss.php?q='
cities = {'айнажи': '26229',
          'александров': '27428',
          'алуксне': '26346',
          'анапа': '37001',
          'анна': '34238',
          'аньяланкоски': '2830',
          'арад': '15200',
          'артёмовск': '34510',
          'аскания-нова': '33915',
          'бакэу': '15150',
          'барановичи': '26941',
          'бараолт': '15215',
          'бауска': '26429',
          'бежецк': '27217',
          'белая': '33464',
          'белгород': '34214',
          'белополье': '33446',
          'белосток': '12295',
          'белый': '26585',
          'бельско-бяла': '12600',
          'бельцы': '33745',
          'бережаны': '33409',
          'березино': '26853',
          'березинский-заповедник': '26959',
          'биржай': '26531',
          'бобринец': '33717',
          'бобруйск': '26961',
          'богодухов': '34302',
          'богучар': '34336',
          'бологое': '26298',
          'борисов': '26759',
          'ботошаны': '15020',
          'брагин': '33124',
          'брашов': '15300',
          'брест': '33008',
          'броды': '33297',
          'брянск': '26898',
          'буй': '27242',
          'быково': '27527',
          'быстрица': '15085',
          'валга': '26247',
          'валуйки': '34321',
          'варшава': '12375',
          'василевичи': '33038',
          'васлуи': '15154',
          'велиж': '26578',
          'великие': '26477',
          'верхнедвинск': '26554',
          'верхний-волочек': '26393',
          'весёлый': '33495',
          'вилейка': '26745',
          'вилсанди': '26214',
          'вильнюс': '26730',
          'винница': '33562',
          'виртсу': '26128',
          'витебск': '26666',
          'владимир': '27532',
          'владимир-волынский': '33177',
          'влодава': '12497',
          'вознесенск': '33777',
          'волгоград': '34560',
          'волковыск': '26923',
          'вологда': '27037',
          'воложин': '26748',
          'волоколамск': '27502',
          'воронеж': '34123',
          'вроцлав': '12424',
          'выборг': '22892',
          'выру': '26249',
          'высокое': '33001',
          'вязьма': '26695',
          'вяйке-маарья': '26141',
          'гагарин': '27507',
          'гадяч': '33376',
          'гайсин': '33577',
          'ганцевичи': '26947',
          'гдов': '26157',
          'геническ': '33910',
          'гигант': '34740',
          'гожув': '12300',
          'гомель': '33041',
          'горки': '26774',
          'гродно': '26825',
          'губиниха': '34407',
          'гулбене': '26348',
          'гусь-хрустальный': '27539',
          'дарабани': '15000',
          'даугавпилс': '26544',
          'дебрецен': '12882',
          'деллис': '60396',
          'днепропетровск': '34504',
          'дно': '26268',
          'добеле': '26424',
          'докшицы': '26657',
          'дрогичин': '33011',
          'дрогобыч': '33398',
          'дружба': '33058',
          'езерище': '26566',
          'ейск': '34727',
          'елгава': '26425',
          'елец': '27928',
          'ершов': '34186',
          'жешув': '12580',
          'житковичи': '33027',
          'житомир': '33325',
          'жлобин': '26966',
          'жуковка': '26894',
          'закопане': '12625',
          'заметчино': '27857',
          'замосць': '12595',
          'запорожье': '34601',
          'звенигородка': '33586',
          'зелена-гура': '12400',
          'зилани': '26436',
          'знаменка': '33609',
          'зосена': '26339',
          'ивано-франковск': '33526',
          'иваново': '27347',
          'ивацевичи': '26938',
          'измаил': '33889',
          'изюм': '34415',
          'инеу': '15033',
          'калач': '34247',
          'калининград': '26702',
          'калиш': '12435',
          'калуга': '27703',
          'каменец-подольский': '33548',
          'каменица': '11993',
          'каменск': '34535',
          'каспровы': '12650',
          'катовице': '12560',
          'каунас': '26629',
          'кашин': '27316',
          'кашира': '27627',
          'кельце': '12570',
          'кентшин': '12185',
          'киев': '33345',
          'кингисепп': '26059',
          'кирилловка': '34609',
          'кировоград': '33711',
          'кирсанов': '27957',
          'кихну': '26226',
          'кишинёв': '33815',
          'клайпеда': '26509',
          'кличев': '26864',
          'клуж-напока': '15120',
          'кобеляки': '33621',
          'ковель': '33173',
          'козенице': '12488',
          'козьмодемьянск': '27479',
          'койсовска': '11958',
          'колка': '26313',
          'коло': '12345',
          'коломия': '33651',
          'комиссаровка': '33723',
          'комрат': '33883',
          'конотоп': '33261',
          'константиновск': '34644',
          'кострома': '27333',
          'костюковичи': '26887',
          'кошице': '11968',
          'кременец': '33299',
          'кривой': '33791',
          'кумлинге': '2790',
          'кунда': '26045',
          'курск': '34009',
          'куусику': '26134',
          'лаукува': '26518',
          'леба': '12120',
          'лельчицы': '33105',
          'лемборк': '12125',
          'лепель': '26659',
          'лесек': '11918',
          'лешно': '12690',
          'ливны': '34013',
          'лида': '26832',
          'лиепая': '26406',
          'липецк': '27930',
          'лиски': '34231',
          'лодзь': '12465',
          'лозовая': '34409',
          'лубны': '33377',
          'лукоянов': '27665',
          'луцк': '33187',
          'лынтупы': '26645',
          'львов': '33393',
          'любань': '26078',
          'любашевка': '33761',
          'любешов': '33075',
          'люблин': '12495',
          'марьина-горка': '26855',
          'мадона': '26447',
          'мариуполь': '34712',
          'мерсрагс': '26324',
          'миколайки': '12280',
          'миллерово': '34438',
          'милхостов': '11978',
          'минск': '26850',
          'мироновка': '33466',
          'мичуринск': '27935',
          'мишкольц': '12772',
          'млава': '12270',
          'могилев': '26862',
          'могилев-подольский': '33663',
          'можайск': '27509',
          'мозырь': '33036',
          'моршанск': '27848',
          'москва': '27612',
          'мстиславль': '26779',
          'мурманск': '22113',
          'нижний-новгород': '27459',
          'нарва': '26058',
          'нарочь': '26649',
          'нежин': '33246',
          'николаев': '33788',
          'николаевское': '26167',
          'новая': '33869',
          'новгород': '26179',
          'новоград-волынский': '33312',
          'новогрудок': '26836',
          'новый': '12660',
          'нолинск': '27393',
          'одесса': '33837',
          'окна': '15015',
          'октябрь': '26950',
          'олевск': '33203',
          'ольштын': '12272',
          'ополе': '12530',
          'орадя': '15080',
          'орша': '26763',
          'орёл': '27906',
          'осташков': '26389',
          'остроленка': '12285',
          'охона': '27108',
          'ошмяны': '26736',
          'павилоста': '26403',
          'пакри': '26029',
          'пенза': '27962',
          'пинск': '33019',
          'познань': '12330',
          'полесская': '33015',
          'полоцк': '26653',
          'поныри': '34003',
          'попрад': '11952',
          'порвоон': '2991',
          'прилуки': '33362',
          'приморско-ахтарск': '34824',
          'пришиб': '34607',
          'пружаны': '26929',
          'псков': '26258',
          'пушкинские': '26359',
          'пшемысль': '12695',
          'пярну': '26231',
          'рава-русская': '33287',
          'резекне': '26446',
          'рига': '26422',
          'ристна': '26115',
          'ровно': '33301',
          'роман': '15111',
          'ромны': '33268',
          'рославль': '26882',
          'ростов': '27329',
          'руйиена': '26238',
          'руссаро': '2982',
          'рухну': '26227',
          'рыбинск': '27225',
          'рязань': '27730',
          'салдус': '26416',
          'самохваловичи': '26843',
          'сандомир': '12585',
          'санкт-петербург': '26063',
          'сарны': '33088',
          'сасово': '27745',
          'сату-маре': '15010',
          'сафоново': '26686',
          'сацуэны': '15042',
          'свермово': '11938',
          'светловодск': '33614',
          'свиноуйсьце': '12200',
          'свитязь': '33067',
          'сегед': '12982',
          'седльце': '12385',
          'селятин': '33657',
          'семёновка': '33049',
          'сенно': '26668',
          'сигету': '15004',
          'скривери': '26435',
          'скулте': '26326',
          'славгород': '26878',
          'слуцк': '26951',
          'смоленск': '26781',
          'советск': '26614',
          'спас-деменск': '26795',
          'старая': '26275',
          'старый': '34116',
          'столбцы': '26846',
          'стропков': '11976',
          'сувалки': '12195',
          'сулеюв': '12469',
          'сумы': '33275',
          'сухиничи': '27707',
          'сырве': '26218',
          'таганрог': '34720',
          'таллин': '26038',
          'тамбов': '27947',
          'таммисаари': '2757',
          'тарнув': '12575',
          'тарту': '26242',
          'тверь': '27402',
          'тельшай': '26515',
          'тересполь': '12399',
          'тернополь': '33415',
          'тетерев': '33228',
          'тихвин': '26094',
          'тихорецк': '34838',
          'топлица': '15107',
          'торопец': '26479',
          'торунь': '12250',
          'тотьма': '27051',
          'трубчевск': '26997',
          'тула': '27719',
          'турку': '2773',
          'тюри': '26135',
          'ужгород': '33631',
          'умань': '33587',
          'устка': '12115',
          'утена': '26633',
          'уто': '2981',
          'ханко': '2750',
          'харьков': '34300',
          'хел': '12135',
          'хельтерма-порт': '26124',
          'херсон': '33902',
          'хмельницкий': '33429',
          'хойнице': '12235',
          'холм': '26378',
          'хурбаново': '11858',
          'ченстохова': '12550',
          'череповец': '27113',
          'чернигов': '33135',
          'чернобыль': '33231',
          'черновцы': '33658',
          'черняховск': '26711',
          'чертков': '33536',
          'чечерск': '26974',
          'чигирин': '33605',
          'чопок': '11916',
          'шарковщина': '26643',
          'шауляй': '26524',
          'шепетовка': '33317',
          'штрбске': '11933',
          'щецин': '12205',
          'щецинек': '12215',
          'щучин': '26834',
          'юрьевец': '27355',
          'яготин': '33356'}
