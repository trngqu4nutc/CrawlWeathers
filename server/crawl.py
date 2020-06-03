from bs4 import BeautifulSoup
import requests
import datetime

headers = requests.utils.default_headers()


def getDay():
    url = 'http://www.thoitiethanoi.com'
    req = requests.get(url, headers)

    # lay trang web
    bs = BeautifulSoup(req.content, 'html.parser')
    weatherInfos = bs.find_all(class_='weather-infos')

    d = []

    for i in range(len(weatherInfos)):
        day = weatherInfos[i].find('h3').get_text()
        img = str(weatherInfos[i].find('img'))
        celsius = weatherInfos[i].find(class_='w-celsius').get_text()
        desc = weatherInfos[i].find(class_='w-desc').get_text()
        amplitude = weatherInfos[i].find_all(class_='w-text', limit=3)
        high = amplitude[0].get_text()
        low = amplitude[1].get_text()
        updated = amplitude[2].get_text()
        d.append(
            {'day': day, 'img': img, 'desc': desc, 'celsius': celsius, 'high': high, 'low': low, 'updated': updated})
    # print(d)
    return d


def getTomorow():
    url = 'http://www.thoitiethanoi.com/thoi-tiet-ngay-mai.html'
    req = requests.get(url, headers)

    # lay trang web
    bs = BeautifulSoup(req.content, 'html.parser')
    homeForecast = bs.find_all(class_='home_forecast', limit=4)

    d = []

    for i in range(len(homeForecast)):
        day = homeForecast[i].find(class_='date').find('h3').get_text()
        img = str(homeForecast[i].find('img'))
        celsius = homeForecast[i].find(class_='current_temp').get_text()
        desc = homeForecast[i].find('h4').get_text()
        amplitude = homeForecast[i].find(class_='home_weather_desc').find_all('p')
        high = amplitude[0].get_text()
        low = amplitude[1].get_text()
        updated = homeForecast[i].find(class_='update').get_text()
        d.append(
            {'day': day, 'img': img, 'desc': desc, 'celsius': celsius, 'high': high, 'low': low, 'updated': updated})
    return d


def getDays(url, limit):
    req = requests.get(url, headers)

    # lay trang web
    bs = BeautifulSoup(req.content, 'html.parser')
    forecast = bs.find_all(class_='forecast', limit=limit)

    d = []

    for i in range(len(forecast)):
        day = forecast[i].find('h3').get_text()
        date = forecast[i].find('em').get_text()
        img = str(forecast[i].find('img'))
        desc = forecast[i].find('h4').get_text()
        celsius = forecast[i].find(class_='current_temp').get_text()
        d.append({'day': day, 'date': date, 'img': img, 'desc': desc, 'celsius': celsius})

    return d


def getNow():
    url = 'http://www.thoitiethanoi.com'
    req = requests.get(url, headers)
    date = str(datetime.datetime.now().date())

    # lay trang web
    bs = BeautifulSoup(req.content, 'html.parser')
    weatherInfos = bs.find(class_='weather-infos')

    day = weatherInfos.find('h3').get_text()
    img = str(weatherInfos.find('img'))
    celsius = weatherInfos.find(class_='w-celsius').get_text()
    desc = weatherInfos.find(class_='w-desc').get_text()
    amplitude = weatherInfos.find_all(class_='w-text', limit=3)
    high = amplitude[0].get_text()
    low = amplitude[1].get_text()
    updated = amplitude[2].get_text()
    return [date, meakeTime(day), img, desc, celsius, high, low, updated]


def meakeTime(day):
    time = datetime.datetime.now().time()
    day = day[:10] + 'lúc ' + str(time.hour) + 'h ' + str(time.minute) + 'm'
    return day


# print(getNow())
