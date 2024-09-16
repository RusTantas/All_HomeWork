'''Задача "Меньше текста, больше кликов":
Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах тела для расчёта калорий выдавались по нажатию кнопки.
Измените massage_handler для функции set_age. Теперь этот хэндлер будет реагировать на текст 'Рассчитать', а не на 'Calories'.
Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом: 'Рассчитать' и 'Информация'. Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства при помощи параметра resize_keyboard.
Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.
В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками. При нажатии на кнопку с надписью 'Рассчитать' срабатывает функция set_age с которой начинается работа машины состояний для age, growth и weight.

Пример результата выполнения программы:
Клавиатура по команде /start:'''



from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton
import asyncio


api = "7189711436:AAGD8lqGigz_RHl67cZWhVO65PfGTMzQPtU"
bot = Bot(token=api)
dp = Dispatcher(bot, storage = MemoryStorage())



class UserState (StatesGroup):
    age= State()
    growth = State()
    weight = State()
#keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
kb = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
button = KeyboardButton(text= 'Информация')
button_2 = KeyboardButton(text= 'Расчитать')
kb.add(button, button_2)


@dp.message_handler(commands='start')
async def start(massage):
    await massage.answer('Привет', reply_markup = kb )

@dp.message_handler(text='Информация')
async def inform(massage):
    await massage.answer('Информация о боте')

@dp.message_handler(text='Расчитать')
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