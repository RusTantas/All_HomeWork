'''Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать' присылалась Inline-клавиатруа.
Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
С текстом 'Рассчитать норму калорий' и callback_data='calories'
С текстом 'Формулы расчёта' и callback_data='formulas'
Создайте новую функцию main_menu(message), которая:
Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'
Создайте новую функцию get_formulas(call), которая:
Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
Будет присылать сообщение с формулой Миффлина-Сан Жеора.
Измените функцию set_age и декоратор для неё:
Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.
По итогу получится следующий алгоритм:
Вводится команда /start
На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
В ответ на кнопку 'Рассчитать' присылается Inline меню: 'Рассчитать норму калорий' и 'Формулы расчёта'
По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
По Inline кнопке 'Рассчитать норму калорий' начинает работать машина состояний по цепочке.'''


from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, InputFile
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage = MemoryStorage())



class UserState (StatesGroup):
    age= State()
    growth = State()
    weight = State()



button_1 = types.InlineKeyboardMarkup(resize_keyboard=True).row(
    types.InlineKeyboardButton('Расчитать норму колорий', callback_data='button_1_presed'),
    types.InlineKeyboardButton("Формула расчета", callback_data='info'),
)

@dp.message_handler(commands='start')
async def start(massage):
    await massage.answer('Привет! Я БОТ помогающий твоему здоровью ')

@dp.message_handler(text='Раcчитать')
async def add(massage):
    await massage.answer( 'Выбирите опцию', reply_markup = button_1 )


@dp.callback_query_handler(text = 'info')
async def infor(call):
    photo_file = open('Формула расчета.jpg', 'rb')
    await call.message.answer_photo(photo_file)
    await call.answer()

@dp.callback_query_handler(text = 'button_1_presed')
async def butten_resalt(call):
    await call.message.answer('Введите свой возраст')
    await UserState.age.set()
    await call.answer()
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