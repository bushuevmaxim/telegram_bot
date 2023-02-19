from aiogram import Bot, Dispatcher, executor, types
from decouple import config

API_TOKEN = config('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ Бот для проектно-образовательного интенсива \"От идеи к прототипу!\"")

@dp.message_handler() 
async def echo(message: types.Message): 
   await message.answer(message.text)

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)