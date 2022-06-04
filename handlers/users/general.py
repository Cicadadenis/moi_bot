from datetime import datetime
from email import message
import os
import time
from aiogram import types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from proxy_checking import ProxyChecker
from telethon import TelegramClient
from aiogram.dispatcher.filters.state import State, StatesGroup
from data.config import ADMINS, api_id, api_hash
from filters import IsNotSubscribed
from keyboards.inline.menu import admin_menu, main_menu, back_to_main_menu, goo
from loader import dp, bot
from modules.settings import Settings
from modules.sessions_storage import SessionsStorage
from modules.functions_storage import FunctionsStorage
from telethon.sessions import StringSession
from states.states import sessions
from utils.db_api.db_commands import *
from datetime import datetime
from datetime import datetime, date, time
from utils.other_utils import get_user_date, send_message_to_chat
class test(StatesGroup):
    tt = State()
first_date = date.today()
second_date   =  date(2022, 6, 29)
delta = second_date - first_date





@dp.callback_query_handler(IsNotSubscribed())
async def answer_call(call: CallbackQuery):
    await call.answer("❗️У вас нету подписки, чтобы пользоваться ботом")


# ========================DELETE BROADCAST MESSAGE========================
# WITH STATE
@dp.callback_query_handler(text="delete_this_message", state="*")
async def del_broadcast_msg(call: CallbackQuery):
    await call.message.delete()
    await bot_start(call.message)


# ========================SHOW MAIN MENU========================
# /start WITHOUT STATE


@dp.message_handler(CommandStart(), state="*")
async def bot_start(message: types.Message):
    if delta == "0":
        await message.answer("<b>Срок Trial Version Истек !</b>")
        time.sleep(10)
        exit(1)
    if not await select_user(message.chat.id):
        await add_user(message.chat.id)
        polz = message.chat.id
        path = 'polzovateli'
        await message.answer("<b>❗️У вас нету подписки, чтобы пользоваться ботом</b>\n"
                             f"Trial Version Осталось {delta.days} Дней")
        os.mkdir(f"{path}/{polz}")
        os.mkdir(f"{path}/{polz}/sessions")
        time.sleep(0.5)
        os.mkdir(f"{path}/{polz}/sessions/spamblock")
        time.sleep(0.5)
        os.mkdir(f"{path}/{polz}/tdata_to_sessions")
        time.sleep(0.5)
        os.mkdir(f"{path}/{polz}/media")
        open(f"{path}/{polz}/message.txt", "w")
        open(f"{path}/{polz}/ussers.txt", "w")
        open(f"{path}/{polz}/report.txt", "w")
        open(f"{path}/{polz}/proxy.txt", "w")
    stat, user = await select_statistic(), await select_user(message.chat.id)
    #result_date = await get_user_date(message.chat.id)
    proxy = await select_user_proxy(message.chat.id)
    if not await select_user(message.chat.id):
        await add_user(message.chat.id)
        polz = message.chat.id
        path = 'polzovateli'
        os.mkdir(f"{path}/{polz}")
        os.mkdir(f"{path}/{polz}/sessions")
        time.sleep(0.5)
        os.mkdir(f"{path}/{polz}/tdata_to_sessions")
        time.sleep(0.5)
        os.mkdir(f"{path}/{polz}/sessions/spamblock")
        time.sleep(0.5)
        os.mkdir(f"{path}/{polz}/media")
        open(f"{path}/{polz}/message.txt", "w")
        open(f"{path}/{polz}/ussers.txt", "w")
        open(f"{path}/{polz}/report.txt", "w")
        open(f"{path}/{polz}/proxy.txt", "w")

    stat, user = await select_statistic(), await select_user(message.chat.id)
    #result_date = await get_user_date(message.chat.id)
    proxy = await select_user_proxy(message.chat.id)


    
    await message.answer(
        "<b>👋 Привет, данный бот создан для удобного авто~постинга во все чаты телеграмма!\n\n"
        "♻️ Отправлять любому юзеру своё сообщение от добавленного аккаунта!\n"
        "♻️ Добавлять хоть 100 чатов (и настраивать их одновременно)\n"
        "♻️Включать / отключать рассылки.\n"
        "♻️Менять все параметры, задержки / текст / фото / и другие!\n\n"
        "🚀Удачного использования!</b>",
        reply_markup=goo)
    
@dp.callback_query_handler(text="back_to_main_menu", state="*")
async def support(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await state.finish()
    path = 'polzovateli'
    us = call.message.chat.id
    sms = open(f"{path}/{us}/message.txt", "r", encoding="utf-8").read()
    sessionnss = []

    for file in os.listdir(f"{path}/{us}/sessions"):
        if file.endswith(".session"):
            session_path = os.path.join("sessions", file)
            sessionnss.append(session_path)
    file_list = len(sessionnss)
    users = len(open(f"{path}/{us}/ussers.txt", "r", encoding="utf-8").readlines())
    mes = len(open(f"{path}/{us}/message.txt", "r", encoding="utf-8").read())
    izo = len(os.listdir(f"{path}/{us}/media"))
    if mes >= 1:
        sms = "есть"
    else:
        sms = "нет"
    ban = len(os.listdir(f"{path}/{us}/sessions/spamblock"))
    report = len(open(f"{path}/{us}/report.txt", "r", encoding="utf-8").readlines())
    user = await select_user(call.message.chat.id)
    stat, proxy = await select_statistic(), await select_user_proxy(call.message.chat.id)
    #result_date = await get_user_date(call.message.chat.id)

    pp = await call.message.answer(
            f"Trial Version Осталось {delta.days} Дней\n\n"
            f"👤    <b>Акаунтов для спама:</b>   {file_list}\n"
            f"✍️    <b>Акаунтов В Бане:</b> {ban}\n"
            f"✍️    <b>Сообщение Для Спама:</b> {sms}\n"
            f"🏞    <b>Изображений Для Спама:</b> {izo} шт\n"
            f"👩‍👩‍👧‍👧    <b>Участников На Снос:</b> {report}\n"
            f"👩‍👩‍👧‍👧    <b>Участников для спама:</b> {users}", reply_markup=await main_menu(call.message.chat.id))


@dp.callback_query_handler(text="posst")
async def posst(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    #await call.message.delete(pp.message_id)
    sms = open('sms.txt', 'r', encoding="utf-8").read()
    ft = open("foto.txt", "r").read()
    if ft == "+++":
        path = f'pics/broadcast/cicada.jpg'
        with open(path, 'rb') as f:
            photo = f.read()
        await call.message.answer_photo(photo=photo, caption=f"{sms}", reply_markup=back_to_main_menu)
    if ft == "---":
        await call.message.answer(sms, reply_markup=back_to_main_menu)
# BACK FROM ANY HANDLER TO MAIN MENU WITH STATE
@dp.callback_query_handler(text="admin", state="*")
async def support(call: CallbackQuery, state: FSMContext):
    

    await state.finish()
    if str(call.from_user.id) in ADMINS:
        await call.message.edit_text("Админ-меню", reply_markup=admin_menu)


# ========================INFO BUTTON========================
@dp.callback_query_handler(text="inf")
async def support(call: CallbackQuery):
    await call.message.edit_text(
        "<b>👋 Привет, данный бот создан для удобного авто~постинга во все чаты телеграмма!\n\n"
        "♻️ Отправлять любому юзеру своё сообщение от добавленного аккаунта!\n"
        "♻️ Добавлять хоть 100 чатов (и настраивать их одновременно)\n"
        "♻️Включать / отключать рассылки.\n"
        "♻️Менять все параметры, задержки / текст / фото / и другие!\n\n"
        "🚀Удачного использования!</b>",
        reply_markup=back_to_main_menu)
