from aiogram import Bot, Dispatcher, types

TOKEN ='6547676391:AAEdkV6D8zyyjElWEx4pUO1oDZPYsN-djjU'


bot = Bot(token =TOKEN)
dp = Dispatcher()


async def set_my_menu():
    await bot.set_my_commands([
        types.BotCommand(command="start",description="beginner"),
        types.BotCommand(command="picture",description="Show"),
        types.BotCommand(command="shop",description="shop"),

    ])
