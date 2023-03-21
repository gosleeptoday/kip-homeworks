import aiogram
import config as cfg
from aiogram import types
from aiogram.dispatcher.filters import Text

bot = aiogram.Bot(token = cfg.TOKEN)
dp = aiogram.Dispatcher(bot)

print('старт')

@dp.message_handler(commands=['start'])
async def first_start(message: aiogram.types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*cfg.buttons)
    await message.answer("Привет, используйте /schedule, что бы посмореть распиание", reply_markup=keyboard)

@dp.message_handler(commands=['schedule'])
async def sched(message: aiogram.types.Message):
    await message.answer("Используйте кнопки для управления ботом.")
    print(message.text)

@dp.message_handler(Text(equals='Четная неделя'))
async def chet(message: aiogram.types.Message):
    await message.answer(cfg.chet)

@dp.message_handler(Text(equals='Нечетная неделя'))
async def chet(message: aiogram.types.Message):
    await message.answer(cfg.nechet)

if __name__ == '__main__':
    aiogram.executor.start_polling(dp)