from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import sys
sys.path.insert(1,'G:\GeekBrains')
from config import MY_BOT_TOKEN


bot = Bot(token=MY_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

@dp.message_handler(commands=['calc'])
async def process_calc_command(message: types.Message):
    mess = message.text.split()
    def funct(esp_str:str) -> int:
        par_close=esp_str.find(')')
        if par_close != -1:
            par_open = esp_str[:par_close].rfind('(')
            return funct(esp_str[:par_open] + str(funct(esp_str[par_open + 1:par_close])) \
                + (esp_str[par_close + 1:] if par_close != len(esp_str) else '')) 
        plus = esp_str.find('+')
        minus = esp_str.find('-')
        mult = esp_str.find('*') 
        div = esp_str.find('/')
        if (plus == -1) and (minus == -1) and (mult == -1) and (div == -1):
            return float(esp_str)
        if plus != -1:
            return funct(esp_str[:plus]) + funct(esp_str[plus + 1:])
        if minus != -1:
            return funct(esp_str[:minus]) - funct(esp_str[minus + 1:])
        if mult != -1:
            return funct(esp_str[:mult]) * funct(esp_str[mult + 1:])
        return int(funct(esp_str[:div]) / funct(esp_str[div + 1:]))
    res = funct(mess[1])
    await message.reply(res)

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)

if __name__ == '__main__':
    executor.start_polling(dp)