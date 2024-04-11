import asyncio
import aiogram
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv
from os import getenv
import logging

import os 
import random

from config import TOKEN

bot = Bot(token =TOKEN)
dp = Dispatcher()



@dp.message(Command('start'))
async def start_cmd(message:types.Message):
    await message.answer(f'Hello ,{message.from_user.first_name}')


@dp.message(Command('myinfo'))
async def myinfo(message:types.Message):
    await message.answer(f'Hello \nYour ID:{message.from_user.id})\nName: {message.from_user.first_name}')




@dp.message(Command('picture'))
async def send_picture(message:types.Message):
    photo = types.FSInputFile('images/' + random.choice(os.listdir('images')), 'rb')
    await message.answer_photo(photo=photo)



async def main():
    await dp.start_polling(bot)

if __name__ =='__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:   
        print('Exit')