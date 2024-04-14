from aiogram import Router,F,types
from aiogram.filters import Command


kafe_router =Router()

@kafe_router.message(Command('kafe'))
async def kafe(message:types.Message):
    kb =types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Европейская кухня'),
                types.KeyboardButton(text='Восточная кухня'),
            ],
            [
                types.KeyboardButton(text='Китайская кухня'),
                types.KeyboardButton(text='Турецкая кухня'),
            ]

        ],
        resize_keyboard=True
    )
    await message.answer('Выберите меню', reply_markup=kb)


@kafe_router.message(F.text.lower()=='европейская кухня')
async def show_evrope(message:types.Message):
    print(message.text)
    await message.answer('блюда от шеф повара для вас!')


@kafe_router.message(F.text.lower()=='Восточная кухня')
async def show_vostoc(message:types.Message):
    print(message.text)
    await message.answer('блюда Востока  для вас!')


@kafe_router.message(F.text.lower()=='Китайская кухня')
async def show_china(message:types.Message):
    print(message.text)
    await message.answer('блюда Китая  для вас!')

@kafe_router.message(F.text.lower()=='Турецкая кухня')
async def show_china(message:types.Message):
    print(message.text)
    await message.answer('блюда Турции для вас!')