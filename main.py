from aiogram import Bot, Dispatcher, executor, types

from api_key import API_TOKEN_KEY
API_TOKEN = API_TOKEN_KEY

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ Бот для проектно-образовательного интенсива \"От идеи к прототипу!\"")

@dp.message_handler() 
async def echo(message: types.Message): 
   await message.answer(message.text)