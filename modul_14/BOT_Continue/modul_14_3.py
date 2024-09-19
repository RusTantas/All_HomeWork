'''Цель: подготовить Telegram-бота для взаимодействия с базой данных.

Задача "Витамины для всех!":
Подготовка:
Подготовьте Telegram-бота из последнего домашнего задания 13 моудля сохранив код с ним в файл module_14_3.py.
Если вы не решали новые задания из предыдущего модуля рекомендуется выполнить их.

Дополните ранее написанный код для Telegram-бота:
Создайте и дополните клавиатуры:
В главную (обычную) клавиатуру меню добавьте кнопку "Купить".
Создайте Inline меню из 4 кнопок с надписями "Product1", "Product2", "Product3", "Product4". У всех кнопок назначьте callback_data="product_buying"
Создайте хэндлеры и функции к ним:
Message хэндлер, который реагирует на текст "Купить" и оборачивает функцию get_buying_list(message).
Функция get_buying_list должна выводить надписи 'Название: Product<number> | Описание: описание <number> | Цена: <number * 100>' 4 раза. После каждой надписи выводите картинки к продуктам. В конце выведите ранее созданное Inline меню с надписью "Выберите продукт для покупки:".
Callback хэндлер, который реагирует на текст "product_buying" и оборачивает функцию send_confirm_message(call).
Функция send_confirm_message, присылает сообщение "Вы успешно приобрели продукт!"'''
from gc import callbacks

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, InputFile
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

# Присвоение АПИ и ТОКИНОВ Обязательно
api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage = MemoryStorage())


# Объявляется класс  UserState для расчета колорий, он наследуется для осинхронности, объявляется представителеи класса
class UserState (StatesGroup):
    age= State()
    growth = State()
    weight = State()

# Кнопки посе сообщения
buy = types.InlineKeyboardMarkup(resize_keyboard=True).row(
    types.InlineKeyboardButton('Продукт 1', callback_data='Product#1'),
    types.InlineKeyboardButton('Продукт 2', callback_data='Product#2'),types.InlineKeyboardButton('Продукт 3', callback_data='Product#3'),types.InlineKeyboardButton('Продукт 4', callback_data='Product#4'),
)

# Постоянная кнопки
kb = types.ReplyKeyboardMarkup (
    keyboard = [
        [KeyboardButton(text= 'Информация', callbacks_data= 'Информация'),  types.KeyboardButton(text= 'Расчитать', callbacks_data= 'Расчитать')],
    [types.KeyboardButton(text= 'Купить', callbacks_data= 'Купить')]
], resize_keyboard=True
)

# Хендлер для команды старт
@dp.message_handler(commands='start')
async def start(massage):
    await massage.answer('Привет Я БОТ помогающий твоему здоровью', reply_markup = kb )

# Хендлер для кнопки информация, возвращает картинку
@dp.message_handler(text = 'Информация')
async def infor(massage):
    photo_file = open('КАЧАТЬ ВМЕСТЕ С modul_13_6.jpg', 'rb')
    await massage.answer_photo(photo_file)

# Хендлер кнопки купить, возвращает 4 картинки + текст, можно было засунуть все в одно, но не полусчилось
@dp.message_handler(text = 'Купить')
async def  get_buying_list(massage):
    photo_file_1 = open('Средство 1.jpg', 'rb')
    photo_file_2 = open('Средство 2.jpeg', 'rb')
    photo_file_3 = open('Средство 3.jpg', 'rb')
    photo_file_4 = open('Средство 4.jpg', 'rb')
    await massage.answer('Название: Product 1 | Описание: описание 1 | Цена: 100')
    await massage.answer_photo(photo_file_1)
    await massage.answer('Название: Product 2 | Описание: описание 2 | Цена: 200')
    await massage.answer_photo(photo_file_2)
    await massage.answer('Название: Product 3 | Описание: описание 3 | Цена: 300')
    await massage.answer_photo(photo_file_3)
    await massage.answer('Название: Product 4 | Описание: описание 4 | Цена: 400')
    await massage.answer_photo(photo_file_4)
    await massage.answer('Выберите продукт для покупки', reply_markup = buy )

# Хендлер кнопки расчитать, вызывает машинное состояние, класс
@dp.message_handler(text='Расчитать')
async def set_age(massage):
    await massage.answer('Введите свой возраст')
    await UserState.age.set()
# Хендлер последовательного машинного состояния
@dp.message_handler(state=UserState.age)
async def set_growth(massage, state):
    await state.update_data(age = massage.text)
    await massage.answer('Введите свой рост')
    await UserState.growth.set()

# Хендлер последовательного машинного состояния
@dp.message_handler(state=UserState.growth)
async def set_weight(massage, state):
    await state.update_data(growth = massage.text)
    await massage.answer('Введите свой вес')
    await UserState.weight.set()

# Хендлер последовательного машинного состояния + расчт по колориям (интресное присвоение данных от сообщения от пользователя)
# Было бы неплохо дорабоать по ошибкам по не тем данным
@dp.message_handler(state=UserState.weight)
async def send_calories( message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    formul = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(f"ваша норма колорий {formul}")
    print(formul)
    await state.finish()

# Хендлер инлайн кнопки
@dp.callback_query_handler(text = 'Product#1')
async def butten_resalt_1(call):
    await call.message.answer('Вы купили продукт №1')
    await call.answer()

# Хендлер инлайн кнопки
@dp.callback_query_handler(text = 'Product#2')
async def butten_resalt_2(call):
    await call.message.answer('Вы купили продукт №2')
    await call.answer()

# Хендлер инлайн кнопки
@dp.callback_query_handler(text = 'Product#3')
async def butten_resalt_3(call):
    await call.message.answer('Вы купили продукт №3')
    await call.answer()

# Хендлер инлайн кнопки
@dp.callback_query_handler(text = 'Product#4')
async def butten_resalt_4(call):
    await call.message.answer('Вы купили продукт №4')
    await call.answer()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)