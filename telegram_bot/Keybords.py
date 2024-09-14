
from turtledemo.penrose import start
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Стоймость"),
            KeyboardButton(text="О нас"),
        ]

    ], resize_keyboard=True
)

katalog_kb = InlineKeyboardMarkup (
    inline_keyboard=[
        [InlineKeyboardButton(text="Средняя игра", callback_data="medium")],
        [InlineKeyboardButton(text="Большая игра", callback_data="big")],
        [InlineKeyboardButton(text="Очень большая игра", callback_data="mega")],
        [InlineKeyboardButton(text="Другие предложения", callback_data="other")]
    ], resize_keyboard=True
)

buy_kb = InlineKeyboardMarkup (
    inline_keyboard=[
        [InlineKeyboardButton(text="Купить!", url='https://www.mosigra.ru/')],
    ], resize_keyboard=True
)