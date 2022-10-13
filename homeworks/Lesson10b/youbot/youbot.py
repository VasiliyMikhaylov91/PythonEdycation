from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import Message
from downloader import tube_download
import os

import sys
sys.path.insert(1,'G:\GeekBrains')
from config import MY_BOT_TOKEN

bot = Bot(token=MY_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: Message):
    await message.reply("Привет!\nНапиши ссылку на видео с youtube и я скину его тебе!")


@dp.message_handler()
async def send_video(message: types.Message):
    await bot.send_video(message.chat.id, open('homeworks\Lesson10b\youbot\ '.replace(' ','')\
        + await tube_download(message.text)), 'rb')

if __name__ == '__main__':
    executor.start_polling(dp)