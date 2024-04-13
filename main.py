import asyncio
from aiogram import Bot
import logging


from config import bot,dp,set_my_menu
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.myinfo import myinfo_router
from handlers.shop import shop_router
from handlers.echo import echo_router


async def main():
    await set_my_menu()
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(myinfo_router)
    dp.include_router(shop_router)
    dp.include_router(echo_router)

    await dp.start_polling(bot)

if __name__ =='__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:   
        print('Exit')