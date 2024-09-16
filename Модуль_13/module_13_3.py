from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

from pyexpat.errors import messages


'''
Цель: написать простейшего телеграм-бота, используя асинхронные функции.

Задача "Он мне ответил!":
Измените функции start и all_messages так, чтобы вместо вывода в консоль строки отправлялись в чате телеграм.
Запустите ваш Telegram-бот и проверьте его на работоспособность.
'''


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage = MemoryStorage())


@dp.message_handler(text = ['Urban', 'ff'])
async def urban_message(massage):
    print(" Urban massage")
    await  massage.answer (" Urban massage!")


@dp.message_handler(commands=['start'])
async def all_message(massage):
    print('Start message')
    await massage.answer ('Start message')


@dp.message_handler()
async def all_message(massage):
    print(" Введите команду /start, чтобы начать общение.")
    await  massage.answer('Введите команду /start, чтобы начать общение')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)