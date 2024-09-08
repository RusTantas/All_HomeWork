
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage = MemoryStorage())

class UserState (StatesGroup):
    age= State()
    growth = State()
    weight = State()

@dp.message_handler(text ='Calories')
async def set_age(massage):
    await massage.answer('Введите свой возраст')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(massage, state):
    await state.update_data(age = massage.text)
    await massage.answer('Введите свой рост')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(massage, state):
    await state.update_data(growth = massage.text)
    await massage.answer('Введите свой вес')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories( message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    formul = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f"ваша норма колорий {formul}")
    print(formul)
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
