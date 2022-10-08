import requests
import sys
sys.path.insert(1,'G:\GeekBrains')
from config import YA_TOKEN

from city_coord import get_coord


# Получение словаря со сводкой погоды из сервиса Yandex по координатам ширины и долготы
def get_weather(city:str, token = YA_TOKEN)->dict:
    coord = get_coord(city)
    r = requests.get(f'https://api.weather.yandex.ru/v2/forecast?lat={str(coord[0])}&lot={str(coord[1])}'+\
        f'&[lang="ru-RU"]&[limit=1]&[hours="false"]&[extra="true"]', headers= {'X-Yandex-API-Key': token})
    data = r.json()
    return data
