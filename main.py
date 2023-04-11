from aiogram import Bot, Dispatcher, executor, types
from decouple import config
from RequestSendler import RequestSendler
from aiogram.dispatcher.filters import ChatTypeFilter

API_TOKEN = config('API_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
   await message.reply("Привет!\nЯ Бот для проектно-образовательного интенсива \"От идеи к прототипу!\"")

@dp.message_handler() 
async def sendMessage(message: types.Message):
    if message.chat.type == 'private':
      
      answer = RequestSendler.SendMessageToServer(message=message.text, userID=message.from_user.id)
      await message.answer(answer)


    elif "@PEIntensivBOT" in message.text:
      answer = RequestSendler.SendMessageToServer(message=message.text, userID=message.from_user.id)
      await message.answer(answer)
       
    

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
