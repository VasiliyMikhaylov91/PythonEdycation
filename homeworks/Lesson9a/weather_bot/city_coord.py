import requests
import sys
sys.path.insert(1,'G:\GeekBrains')
from config import OW_TOKEN_cord

# Получение координат города из сервиса OpenWeather
def get_coord(city, token = OW_TOKEN_cord):
    r = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={token}')
    data = r.json()
    try:
        return [data[-1]['lat'],data[-1]['lon']]
    except:
        return None

