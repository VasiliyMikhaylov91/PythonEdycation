from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ContentType, Message
from downloader import tube_title, tube_download


import sys
sys.path.insert(1,'G:\GeekBrains')
from config import MY_BOT_TOKEN

bot = Bot(token=MY_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: Message):
    await message.reply("Привет!\nНапиши ссылку на видео с youtube и я скину его тебе!")


@dp.message_handler(content_types=ContentType.VIDEO)
async def send_weather(message: types.Message):
    title = tube_title(message.text)
    # await bot.send_message(message.from_user.id, title)
    # tube_download(message.text)
    await bot.send_video(message.chat.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp)