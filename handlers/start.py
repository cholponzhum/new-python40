from aiogram import Router,F,types
from aiogram.filters import Command



start_router = Router()


@start_router.message(Command('start'))
async def start_cmd(message:types.Message):
    
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


    await message.answer(f'Hello ,{message.from_user.first_name}',reply_markup=kb)


@start_router.callback_query(F.data=="about_us")
async def about_us(cb:types.CallbackQuery):
    await cb.answer()
    await cb.message.answer("Our website:https://online.geeks.kg/")
