from aiogram import types


def start_keyboard():
    kb = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="our web", url="https://online.geeks.kg/")
            ],

            [    types.InlineKeyboardButton(text="our instagram", url="https://online.geeks.kg/")
            ],
            [
                types.InlineKeyboardButton(text="About us",callback_data="about_us")
            ],
            [
                types.InlineKeyboardButton(text="Donate us",callback_data="donate_us")
            ]
        ]
    )
    return kb