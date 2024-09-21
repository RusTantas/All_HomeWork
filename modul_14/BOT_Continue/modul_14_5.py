'''Задача "Продуктовая база":
Подготовка:
Для решения этой задачи вам понадобится код из предыдущей задачи. Дополните его, следуя пунктам задачи ниже.

Дополните ранее написанный код для Telegram-бота:
Создайте файл crud_functions.py и напишите там следующие функции:
initiate_db, которая создаёт таблицу Products, если она ещё не создана при помощи SQL запроса. Эта таблица должна содержать следующие поля:
id - целое число, первичный ключ
title(название продукта) - текст (не пустой)
description(описание) - тест
price(цена) - целое число (не пустой)
get_all_products, которая возвращает все записи из таблицы Products, полученные при помощи SQL запроса.

Изменения в Telegram-бот:
В самом начале запускайте ранее написанную функцию get_all_products.
Измените функцию get_buying_list в модуле с Telegram-ботом, используя вместо обычной нумерации продуктов функцию get_all_products. Полученные записи используйте в выводимой надписи: "Название: <title> | Описание: <description> | Цена: <price>"
Перед запуском бота пополните вашу таблицу Products 4 или более записями для последующего вывода в чате Telegram-бота."'''
import sqlite3
from gc import callbacks
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, InputFile
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from crud_functions import *
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

# Присвоение АПИ и ТОКИНОВ Обязательно
api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage = MemoryStorage())
#подключаем базу данных
initiate_db()
db = get_all_products()


# Объявляется класс  UserState для расчета колорий, он наследуется для осинхронности, объявляется представителеи класса
class UserState (StatesGroup):
    age= State()
    growth = State()
    weight = State()

class UserRegistration (StatesGroup):
    user_name= State()
    user_email = State()
    user_age = State()
    user_balans = State()



# Кнопки посе сообщения
buy = types.InlineKeyboardMarkup(resize_keyboard=True).row(
    types.InlineKeyboardButton('Продукт 1', callback_data='Product#1'),
    types.InlineKeyboardButton('Продукт 2', callback_data='Product#2'),types.InlineKeyboardButton('Продукт 3', callback_data='Product#3'),types.InlineKeyboardButton('Продукт 4', callback_data='Product#4'),
)

# Постоянная кнопки
kb = types.ReplyKeyboardMarkup (
    keyboard = [
        [KeyboardButton(text= 'Информация', callbacks_data= 'Информация'),  types.KeyboardButton(text= 'Расчитать', callbacks_data= 'Расчитать')],
    [types.KeyboardButton(text= 'Купить', callbacks_data= 'Купить'), types.KeyboardButton(text= 'Регистрация', callbacks_data= 'Регистрация')]
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

    await massage.answer(f'Название: {db[0][1]} | Описание: {db[0][2]} | Цена: {db[0][3]} ')
    await massage.answer_photo(photo_file_1)
    await massage.answer(f'Название: {db[1][1]} | Описание: {db[1][2]} | Цена: {db[1][3]} ')
    await massage.answer_photo(photo_file_2)
    await massage.answer(f'Название: {db[2][1]} | Описание: {db[2][2]} | Цена: {db[2][3]} ')
    await massage.answer_photo(photo_file_3)
    await massage.answer(f'Название: {db[3][1]} | Описание: {db[3][2]} | Цена: {db[3][3]} ')
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



#  Хендлер кнопки регистрации, вызывает машинное состояние, класс
@dp.message_handler(text='Регистрация')
async def set_user_name(massage):
    await massage.answer('Введите имя пользователя(только латинские алфавит)')
    await UserRegistration.user_name.set()
# Хендлер последовательного машинного состояния
@dp.message_handler(state=UserRegistration.user_name)
async def set_user_email(massage, state):
    await state.update_data(user_name = massage.text)
    await massage.answer('Введите свой email')
    await UserRegistration.user_email.set()
# Хендлер последовательного машинного состояния
@dp.message_handler(state=UserRegistration.user_email)
async def set_user_age(massage, state):
    await state.update_data(user_email = massage.text)
    await massage.answer('Введите свой возраст')
    await UserRegistration.user_age.set()

# Хендлер последовательного машинного состояния + перевод в БД
# Было бы неплохо дорабоать по ошибкам по не тем данным
@dp.message_handler(state=UserRegistration.user_age)
async def user_registration( message, state):
    await state.update_data(user_age = message.text)
    await state.update_data(user_balans=1000)
    data = await state.get_data()
    if add_user(data['user_name'], data['user_email'], int(data['user_age']), int(data['user_balans'])) == True:
        user = data['user_name']
        await message.answer(f'Регистарция {user} прошла успешна', reply_markup = kb)
    else:
         await message.answer('Пользователь с таким именим уже существует прошу изменить "имя пользователя"', reply_markup = kb)
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