import requests
import sys
sys.path.insert(1,'G:\GeekBrains')
from config import YA_TOKEN

# from city_coord import get_coord


# Получение словаря со сводкой погоды из сервиса Yandex по координатам ширины и долготы
def get_weather(coordinates:list, token = YA_TOKEN)->dict:
    # coord = get_coord(city)
    rec = f'https://api.weather.yandex.ru/v2/forecast?lat={coordinates[0]}&lon={coordinates[1]}&extra=true'
    print(rec)
    r = requests.get(rec,headers= {'X-Yandex-API-Key': token})
    data = r.json()
    return data
