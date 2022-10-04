bot = Bot(token = bot_token)
dp = Dispatcher(bot)

@dp.message_handler(commands = ['start', 'help'])
async def all_commands(msg: types.Message):
    await msg.reply(f'/help\n/see_phonebook\n/add_record Фамилия Имя Телефон\n/find_record Фамилия\n/delete_record Фамилия')

@dp.message_handler(commands = ['see_phonebook'])
async def see_phonebook(msg: types.Message):
    phone_list = wr_rd.read_all_data()
    phone_str = ''
    for i in phone_list:
        phone_str += i
    await msg.reply(phone_str)

@dp.message_handler(commands = ['add_record'])
async def add_record(msg: types.Message):
    mess = msg.text.split()
    fun.new_record_txt(mess[1], mess[2], mess[3])
    await msg.reply('Готово!')

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
