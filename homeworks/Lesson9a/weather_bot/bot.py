from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import sys
sys.path.insert(1,'G:\GeekBrains')
from config import  MY_BOT_TOKEN
from translation import distionary, dict_wind

from coord_weather import get_weather
from city_coord import get_coord

bot = Bot(token=MY_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши название города и я там тебе сводку погоды")

@dp.message_handler()
async def send_weather(message: types.Message):
    dict_weather = get_weather(get_coord(message.text))
    await bot.send_message(message.from_user.id,\
                        f'Погода в городе {dict_weather["geo_object"]["locality"]["name"]}'+'\n'+\
                        f'Температура воздуха: {str(dict_weather["fact"]["temp"])} °C'+'\n'+\
                        f'Ощущается как: {str(dict_weather["fact"]["feels_like"])} °C'+'\n'+\
                        f'{distionary[dict_weather["fact"]["condition"].replace("-","")]}'+'\n'+\
                        f'Ветер: {dict_wind[dict_weather["fact"]["wind_dir"]]} {str(dict_weather["fact"]["wind_speed"])} м/c'+'\n'+\
                        f'Атмосферное давление: {str(dict_weather["fact"]["pressure_mm"])} мм.рт.ст'+'\n'+\
                        f'Влажность воздуха: {str(dict_weather["fact"]["humidity"])}%')
if __name__ == '__main__':
    executor.start_polling(dp)