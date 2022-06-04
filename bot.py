from aiogram.utils import executor
import asyncio, os
import requests
from data import config
from loader import scheduler, dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from handlers.users.admin import on_startup2
token = config.TOKEN
wait_for = 6
async def on_startup(dispatcher):
    await on_startup_notify(dispatcher)
    MethodGetMe = (f'''https://api.telegram.org/bot{token}/GetMe''')
    response = requests.post(MethodGetMe)
    tttm = response.json()
    tk = tttm['ok']
    if tk == True:
        id_us = (tttm['result']['id'])
        first_name = (tttm['result']['first_name'])
        username = (tttm['result']['username'])
  

        print(f"""
                    ---------------------------------
                    🆔 Bot id: {id_us}
                    ---------------------------------
                    👤 Имя Бота: {first_name}
                    ---------------------------------
                    🗣 username: {username}
                    ---------------------------------
                    🌐 https://t.me/{username}
                    ---------------------------------
                    ******* Suport: @Satanasat ******
        """)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.create_task(on_startup2(10))
    executor.start_polling(dp, on_startup=on_startup)
    scheduler.start()