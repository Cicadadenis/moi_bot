import asyncio
import os
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.sync import TelegramClient
from states.states import AddAccount, DelAcc, AddProxy, DelProxy, SpamChat, SpamUser, SpamBot
import random
from random import randint
from telethon import TelegramClient, Button, events
from datetime import datetime, timedelta
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery, Message
from telethon.tl.functions.messages import ImportChatInviteRequest
from aiogram.utils.exceptions import Unauthorized
from telethon.tl.functions.channels import JoinChannelRequest
import json
from typing import Any, NoReturn
from telethon import TelegramClient, Button, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import os, time
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.users import GetUsersRequest
from telethon.tl.types import ChannelParticipantsSearch
import asyncio
import datetime, sys
from datetime import datetime, date, time
from telethon import utils
from telethon.tl.types import InputPeerUser
import os
from loguru import logger
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from convert_tdata import *
import time
from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime
from modules.settings import Settings
from modules.sessions_storage import SessionsStorage
from modules.functions_storage import FunctionsStorage
# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.account import UpdateProfileRequest
# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from telethon.errors.rpcerrorlist import FloodWaitError
from keyboards.inline.menu import back_admin, admin_menu, choose_menu, zagruzki
from loader import dp, bot
from states.states import BroadcastState, GiveTime, TakeTime
from keyboards.inline.menu import back_to_main_menu,  api_hash, api_id, code_menu, \
    main_menu, proxy_menu, start_spam_menu, accept_spam_menu, ssttop, repppo, akiy
from utils.db_api.db_commands import select_all_users, del_user, update_date
from calendar import c
from telethon.utils import get_input_peer
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import PeerUser, PeerChat, PeerChannel, InputPeerUser, InputPeerChat, InputPeerChannel
from telethon.tl.functions.messages import GetDialogsRequest
from email import message
import random
import sys, os
from rich.console import Console
from modules.settings import Settings
from telethon import functions, types
from modules.sessions_storage import SessionsStorage
from modules.functions_storage import FunctionsStorage
from telethon.sessions import StringSession
from telethon.tl.custom import Button
from datetime import datetime
from telethon.tl.functions.channels import JoinChannelRequest, InviteToChannelRequest
from telethon.errors import PeerFloodError, UserPrivacyRestrictedError
from telethon.tl.functions.channels import GetParticipantsRequest
from rich.prompt import Prompt
from rich.console import Console
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.channels import LeaveChannelRequest

from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.channels import InviteToChannelRequest
import asyncio
from keyboards.inline.menu import back_to_main_menu,  api_hash, api_id, code_menu, \
    main_menu, proxy_menu, start_spam_menu, accept_spam_menu, zagruzki, izmenen, konver, maka, spamer
import socks
from utils.db_api.db_commands import select_all_users, del_user, update_date
from telethon.tl.functions.channels import JoinChannelRequest
from telethon import TelegramClient
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.types import InputChannel
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from aiogram.dispatcher import FSMContext
from telethon.tl.functions.messages import AddChatUserRequest
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import os, sys
import configparser
import csv
import time
import random

from lib2to3.pgen2 import token
import rarfile
import shutil
import re
import requests
from datetime import datetime
import time
from aiogram import Dispatcher, executor
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram import Bot, types, executor
from aiogram.utils.markdown import hbold, hlink
import time
from threading import Timer
import os
from telethon.sync import TelegramClient
from telethon import functions, types
from datetime import datetime, timedelta


class akasil(StatesGroup):
    sms_text = State()
    search = State()
    urlses = State()
    parser = State()
    add_chat = State()
    pass2fa = State()
    spam_fo_spis = State()
    spam_imag = State()
    sp_spi = State()

class sms5(StatesGroup):
    sms_text = State()
    bio = State()



class sms4(StatesGroup):
    sms_text = State()
    spam = State()
    textspam = State()
    proxy = State()
    foto = State()
    tdata = State()

class sms3(StatesGroup):
    sms_text = State()

class sms2(StatesGroup):
    sms_text = State()

class post(StatesGroup):
    text = State()

class tima(StatesGroup):
    timeout = State()



@dp.callback_query_handler(text="paussa")
async def paus(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Введи Критерии Для Поиска </b>")
    await akasil.search.set()

@dp.message_handler(state=akasil.search)
async def receive_com(message: Message, state):
    search = message.text
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    api_hash = "b826075fd7ea762e6b9f853146d47995"
    api_id = 1325339
    session = TelegramClient(
                        StringSession("1ApWapzMBu8CmjHE47x8rCF3a7P6l9_mdPEmlFJd25VbEpnAqSSj5FdCwZ_13sbmNNqzWc6Qljztsy2AYLWKrS7391Lmut2t5pxUGe4tKyEsYdEhTjOMdySe1S97DwSxa7igieFUKTCW21C8nPxRXkPz4Cez5XGuSrUfgefkfcuzJolvKkVQd6BCza8ll_-Onk8bI8FgNngFg5_Mr329Lgd8ZGcZzKl87KeUEXrxjKFsJtLBCK2k7VU1LdMHnHDrt97kaNu9vfNQsBNAlDtpU16wc8HNsigj64AnuYelktnzqJaSOA3ZT2uEU7e7fxoDR3JNrWtOjY-4JbHD2MGB_WUWtoTuK-ms="),
                        api_id,
                        api_hash,
                        device_model="Redmi Note 10",
                        lang_code="en",
                        system_lang_code="en"
                    )
    await session.connect()

    result =   await session(functions.contacts.SearchRequest(
        q=search,
        limit=100
    ))


    for x in  result.chats:
        ress = (
            f"\n\n➖➖➖➖➖➖➖➖➖➖\n"
            f"<b>Название:   {x.title}</b>\n"
            f"➖➖➖➖➖➖➖➖➖➖➖\n"
            f"<b>Адрес:</b>  http://t.me/{x.username}\n"
            f"➖➖➖➖➖➖➖➖➖➖➖\n"
            f"<b>Пользователей:</b>  {x.participants_count}\n"
            f"➖➖➖➖➖➖➖➖➖➖➖\n"
        )
        await message.answer(ress)
    await state.finish()
    await message.answer(f"<b>Найдено {len(result.chats)} Чатов</b>", reply_markup=back_to_main_menu)


@dp.callback_query_handler(text="use")
async def use(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Меню Работы С Акаунтами:</b>", reply_markup=maka)


@dp.callback_query_handler(text="floodcomm")
async def floodcomm(call: CallbackQuery):
    await call.answer("Скоро Будет Доступно !!!!")


@dp.callback_query_handler(text="floodchat")
async def floodchat(call: CallbackQuery):
    await call.answer("Скоро Будет Доступно !!!!")


@dp.callback_query_handler(text="floodls")
async def floodls(call: CallbackQuery):
    await call.answer("Скоро Будет Доступно !!!!")


@dp.callback_query_handler(text="add_voice")
async def add_to_chanel(call: CallbackQuery):
    await call.answer("Скоро Будет Доступно !!!!")


@dp.callback_query_handler(text="9")
async def dds(call: CallbackQuery):
    await call.answer("Скоро Будет Доступно !!!!")

@dp.callback_query_handler(text="ad_sesion")
async def ad_sesion(call: CallbackQuery):
    await call.message.answer("<b>Отправь мне файлы sesions</b>")
    @dp.message_handler(content_types=['document'])
    async def uss(message: Message):
        path = 'polzovateli'
        us = message.chat.id
        bbbb =  message.document.file_name #.download(destination="ussers.txt")

        fast = bbbb.split(".")
        try:
            if fast[1] == 'session':
                time.sleep(2)
                await message.document.download(destination=f"{path}/{us}/sessions/{bbbb}")
                await message.answer(f"<b>Акаунт <code>{fast[0]}</code> добавлен</b>", reply_markup=back_to_main_menu)
            else:
                await message.answer(f"<b>Фаил <code>{fast}</code> поврежден либо неверного формата</b>", reply_markup=back_to_main_menu)
        except:
            await message.answer("<b>‼️ Фаил недобустимого формата ‼️</b>", reply_markup=back_to_main_menu)


@dp.callback_query_handler(text="rep")
async def rep(call: CallbackQuery):
    msms = await call.message.answer("<b>Запуск Reporter</b>")
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    tt = open('time.txt', 'r')
    ti = int(tt.read())
    tt.close()
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581"
    file_list = os.listdir('sessions')
    xx = len(file_list)
    ss = open('ussers.txt', 'r').readlines()
    z = len(ss)
    count = int(z)
    i = 1
    s = 0
    c = 0
    o = 0
    msm = 0
    a = 5
    while i <= xx:
        try:
            acaunt = file_list[i]
            try:
                npn  = int(open(f"check/{acaunt}.txt", "r").read())
            except:
                i = i + 1
                continue
            print(npn)
            if npn <= 0:
                i = i + 1
                continue
            sto = open('stop.txt', 'r').read()
            if sto == 'stop':
                with open('stop.txt', 'w') as f:
                    f.write("start")
                await call.message.answer("Рассылка остановлена", reply_markup=back_to_main_menu)
                break
            if a == count:
                await client.disconnect()
                i = i + 1
                a = 0
            mm = 0
            file_list = os.listdir('sessions')
            acaunt = file_list[i]
            cli = open(f"sessions/{acaunt}").read()
            aka = acaunt.split(".")[0]
            client = TelegramClient(StringSession(cli), api_id, api_hash)
            await client.connect()
            ss = open('ussers.txt', 'r').readlines()
            username = ss[a][:-1]
            message_id = "8"
            rsn = types.InputReportReasonPornography()
            msg = "some messages"
            async def rep(username, message_id, rsn, msg):
                print("y")
                a = await client(functions.messages.ReportRequest(
                    peer='@'+username,
                    id=[int(message_id)],
                    reason=rsn,
                    message = msg
                ))
                print(a)

            msm = msm + 1
            await msms.edit_text(
                f"<b>   Всего отправленно жалоб {msm}</b>\n\n"
                f"💬    <b>Жалоба С Акаунта: \n<code>{aka}</code> \nна</b> <code>{username}</code> Отправленна! +1 \n\n", reply_markup=ssttop)
            o = o + 1

            mm = mm + 1
            time.sleep(ti)
            a = a + 1
            await client.disconnect()
        except:
            i = i + 1
    await call.message.answer("<b>Report Завершил работу над списком !</b>", reply_markup=back_to_main_menu)

@dp.callback_query_handler(text="adddd", state="*")
async def adddd(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Выбери способ добавления: </b>", reply_markup=akiy
    )

@dp.callback_query_handler(text="bio", state="*")
async def rename(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Введи Новую Биографию:</b>")
    await sms5.bio.set()


@dp.message_handler(state=sms5.bio)
async def bio(message: Message, state):
    path = 'polzovateli'
    us = message.chat.id   
    bio = message.text
    await state.finish()
    biograf =  await message.answer("Изменение Биографии Профиля")
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    for file in os.listdir(f"{path}/{us}/sessions"):
        if file.endswith(".session"):
            session_path = os.path.join("sessions", file)
            
            with open(f"{path}/{us}/{session_path}") as fileobj:
                 auth_key = fileobj.read()
            try:
                session = TelegramClient(
                    StringSession(auth_key),
                    api_id,
                    api_hash,
                    device_model="Redmi Note 10",
                    lang_code="en",
                    system_lang_code="en"
                )
                await session.connect()
                me = await session.get_me()
                print(me.about)
            except:
                pass

            try:
                await session(
                    UpdateProfileRequest(about=bio)
                )
                await biograf.edit_text("<b>Биография Измененна</b>")
            except:
                await biograf.edit_text("<b>Биография НЕ Измененна</b>")
                pass
    await biograf.edit_text("<b>Биография Изменена На Всех Акаунтах</b>", reply_markup=back_to_main_menu)



@dp.callback_query_handler(text="rep1", state="*")
async def rep1(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    msgs = await call.message.answer("Запуск Reporta Жестокое обращение с ребенком")
    path = 'polzovateli'
    us = call.message.chat.id    
    a = open(f"{path}/{us}/report.txt", 'r', encoding='utf-8').readlines()
    baza = []
    for x in a:
        d = x.split("\n")
        for s in d:
            if s >= '0':
                baza.append(s)
    for z in baza:
        for file in os.listdir(f"{path}/{us}/sessions"):
            if file.endswith(".session"):
                session_path = os.path.join("sessions", file)

                with open(f"{path}/{us}/{session_path}") as fileobj:
                        auth_key = fileobj.read()
                #try:
                session = TelegramClient(
                    StringSession(auth_key),
                    api_id,
                    api_hash,
                    device_model="Redmi Note 10",
                    lang_code="en",
                    system_lang_code="en"
                )
                await session.connect()
            
                f = random.randint(1,458)
                iidd = [int(f)]
                me = await session.get_me()
                try:
                    v = await session.get_input_entity(z) 
                    t = v
                    uss = int(v.user_id) 
                    asa = await session.get_input_entity(PeerUser(uss))
                    await msgs.edit_text(f"<b>Жалоба Отправленна С Акаунта {me.first_name}</b>\n"
                                            f"<b>На Пользователя {z}</b>")
                    
                #except:
                #    vvv = await session.get_input_entity(x)
                #    ttt = vvv
                #    usus = int(vv.channel_id)  
                #    asa = await session.get_input_entity(PeerChannel(usus))
                #    await msgs.edit_text(f"<b>Жалоба Отправленна С Акаунта {akka}</b>\n"
                #                            f"<b>На Пользователя {x}</b>")  
                except:
                    await msgs.edit_text(f"<b>Пользователь {z} Мертв</b>")  
                    
    await msgs.edit_text(f"<b>Жалобы Отправленны</b>", reply_markup=back_to_main_menu)

@dp.callback_query_handler(text="refoto", state="*")
async def rename(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    msgs = await call.message.answer("Изменение Фото Профиля")
    path2 = 'polzovateli'
    us = call.message.chat.id    
    path = os.path.join(os.getcwd(), "assets", "photos")
    photos = os.listdir(path)
    for file in os.listdir(f"{path2}/{us}/sessions"):
        if file.endswith(".session"):
            session_path = os.path.join("sessions", file)
            
            with open(f"{path2}/{us}/{session_path}") as fileobj:
                 auth_key = fileobj.read()
            try:
                session = TelegramClient(
                    StringSession(auth_key),
                    api_id,
                    api_hash,
                    device_model="Redmi Note 10",
                    lang_code="en",
                    system_lang_code="en"
                )
                await session.connect()
                photo = os.path.join(
                    path, random.choice(photos)
                )
            except:
                pass
            try:
                await session(functions.photos.UploadProfilePhotoRequest(
                    file=await session.upload_file(photo),
                ))
                await msgs.edit_text("<b>Фото Измененно</b>")
            except:

                pass
    await msgs.edit_text("<b>Фото Измененно На Всех Акаунтах</b>", reply_markup=back_to_main_menu)

@dp.callback_query_handler(text="rename", state="*")
async def rename(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    msgs = await call.message.answer("Изменение Имени Профиля")
    path = 'polzovateli'
    us = call.message.chat.id    
    for file in os.listdir(f"{path}/{us}/sessions"):
        if file.endswith(".session"):
            session_path = os.path.join("sessions", file)
            
            with open(f"{path}/{us}/{session_path}") as fileobj:
                 auth_key = fileobj.read()
            try:
                session = TelegramClient(
                    StringSession(auth_key),
                    api_id,
                    api_hash,
                    device_model="Redmi Note 10",
                    lang_code="en",
                    system_lang_code="en"
                )
                await session.connect()
                me = await session.get_me()
                print(me.first_name)
            except:
                pass
            with open("assets/names.txt", "r", encoding="utf-8") as file:
                names = file.read().strip().splitlines()
            name = random.choice(names).split()
            first_name = name[0]
            print(first_name)
            last_name = name[1]
            try:
                await session(
                    UpdateProfileRequest(
                        first_name=first_name,
                        last_name=last_name
                    )
                )
                await msgs.edit_text("<b>Имя Измененно</b>")
            except:
                await msgs.edit_text("<b>Имя НЕ Измененно</b>")
                pass
    await msgs.edit_text("<b>Имя Измененно На Всех Акаунтах</b>", reply_markup=back_to_main_menu)


@dp.callback_query_handler(text="add_silka", state="*")
async def add_silka(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer(
        f"<b>Для загрузки акаунтов по ссылке</b>\n"
        f"<b>Нужны акаунты только с этого ресурса:</b>\n"
        f"<b>https://ydeda.pro/</b>")
    await akasil.sms_text.set()




@dp.message_handler(state=akasil.sms_text)
async def receive_com(message: Message, state):
    ww = message.text
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    API_HASH = "bd4bbac77f54cd096ede52dd2e8e2e50"
    API_ID = 17463049
    sessions = []
    await message.answer("<b>Идет Обработка и подвязка акаунтов ожидайте...</b>")
    baza = []
    dir_name = "temp_aka"
    print("".join(map(str, ww)))
    url_pattern = r'https://[\S]+'
    u = re.findall(url_pattern, ww)
    s = len(u)

    await message.answer(f"<b>Подготавливаю {s} Акаунтов</b>")
    for x in u:

        os.system(f"wget {x} ")
        time.sleep(4)
        z = x.split("/")[-1]
        print(z)
        nn = z.split("-")[0]
        rarobj = rarfile.RarFile(z)
        rarobj.extractall(dir_name)
        for tdata in os.listdir("temp_aka"):
            print(tdata)
            auth_key = convert_tdata(f"temp_aka/{nn}/tdata")[0]
#            except Exception as err:
 #               logger.error(err)
  #          else:
   #             logger.success(f"{tdata} успешно конвертировано")

            sessions.append(StringSession(auth_key))

            logger.info("Проверка аккаунтов")
            j = 0
            for session in sessions:
 #               await messag.answer(f"<b>Подключаю Акаунт {nn}</b>")
                j = j + 1
                client = TelegramClient(
                    session,
                    api_hash=API_HASH,
                    api_id=API_ID
                )



                await client.connect()
                auth_key = client.session.save()
                with open(f"sessions/{tdata}.session", "w") as file:
                    file.write(auth_key)
                    await client.disconnect()
                    logger.success(f"{tdata} — сохранён.")
                with open(f"check/{tdata}.session.txt", "w") as f:
                    f.write("10")
        zzz = os.listdir("temp_aka")
        nn = len(zzz)
        os.system(f"rm -r temp_aka/* ")

    await message.answer(f"<b>Готово ! Акаунты добавленны +{s} шт !</b>", reply_markup=back_to_main_menu)
#
    await state.finish()
    sessions.clear()

@dp.callback_query_handler(text="sms", state="*")
async def sms(call: CallbackQuery, state: FSMContext):
    path = 'polzovateli'
    us = call.message.chat.id
    sessionnss = []
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
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
    if file_list <= 1:
        await call.message.answer('<b>У Тебя Нет Акаунтов</b>',
                         reply_markup=back_to_main_menu)
    else:
        await call.message.answer(
            f"<b>Меню Изменения:</b>",
                                     reply_markup=izmenen)
        await sms2.sms_text.set()
    #await call.message.answer('💬     <b>Текст успешно сохранен</b> !',
     #                     reply_markup=back_to_main_menu)
#
    @dp.message_handler(state=sms2.sms_text)
    async def sms_spam(message: Message,  state: FSMContext):
        data = await state.get_data()
        sms = message.text
        with open('sms.txt', 'w', encoding="utf-8") as f:
            f.write(sms)
        await message.answer('💬     <b>Текст успешно сохранен</b> !',
                            reply_markup=back_to_main_menu)


@dp.callback_query_handler(text="give_time")
async def edit_commission(call: CallbackQuery, state: FSMContext):
    msg_to_edit = await call.message.edit_text("<b>🆔    Введите ID человека:</b>",
                                               reply_markup=back_admin)
    await GiveTime.GT1.set()
    await state.update_data(msg_to_edit=msg_to_edit)


@dp.message_handler(state=GiveTime.GT1)
async def receive_com(message: Message, state: FSMContext):
    data = await state.get_data()
    msg_to_edit = data.get("msg_to_edit")
    user_id = message.text
    await message.delete()
    await GiveTime.next()
    await state.update_data(user_id=user_id)
    await msg_to_edit.edit_text("<b>⏰  Введите время в часах которое выдать человеку:</b>", reply_markup=back_admin)


@dp.message_handler(state=GiveTime.GT2)
async def receive_com(message: Message, state: FSMContext):
    data = await state.get_data()
    msg_to_edit, user_id = data.get("msg_to_edit"), data.get("user_id")
    try:
        hours = int(message.text)
        await message.delete()
        date_when_expires = datetime.now() + timedelta(hours=hours)
        date_to_db = str(date_when_expires).split(".")[0].replace("-", " ").split(":")
        date_to_db = " ".join(date_to_db[:-1])
        await update_date(user_id, date_to_db)
        await state.finish()
        await msg_to_edit.edit_text("<b>Доступ выдан.</b>", reply_markup=back_admin)
    except ValueError:
        await msg_to_edit.edit_text("<b>    ⏰Не верный формат, попробуйте еще раз.</b>")


@dp.callback_query_handler(text="take_time")
async def edit_commission(call: CallbackQuery, state: FSMContext):
    msg_to_edit = await call.message.edit_text("<b>🆔    Введите ID человека:</b>",
                                               reply_markup=back_admin)
    await TakeTime.T1.set()
    await state.update_data(msg_to_edit=msg_to_edit)


@dp.message_handler(state=TakeTime.T1)
async def receive_com(message: Message, state: FSMContext):
    data = await state.get_data()
    msg_to_edit = data.get("msg_to_edit")
    user_id = message.text
    await message.delete()
    await update_date(user_id, None)
    await state.finish()
    await msg_to_edit.edit_text("<b>У юзера больше нет доступа.</b>", reply_markup=back_admin)


# ========================BROADCAST========================
# ASK FOR PHOTO AND TEXT
@dp.callback_query_handler(text="broadcast")
async def broadcast2(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Меню Контертации</b>", reply_markup=konver)



# RECEIVE PHOTO OR TEXT
@dp.message_handler(content_types=['photo'], state=BroadcastState.BS1)
async def broadcast4(message: Message, state: FSMContext):
    await message.delete()
    easy_chars = 'abcdefghijklnopqrstuvwxyz1234567890'
    name = 'cicada'
    photo_name = name + ".jpg"
    await message.photo[-1].download(f"pics/broadcast/{photo_name}")
    await state.update_data(photo=photo_name, text=message.caption)
    with open("foto.txt", "w") as f:
        f.write("+++")
    await asyncio.sleep(2)
    await message.answer("🏞    <b>Фото успешно загруженно</b>", reply_markup=back_to_main_menu)



@dp.callback_query_handler(text="fdel")
async def fdel(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Меню Спама:</b>", reply_markup=spamer)

@dp.callback_query_handler(text="hahah")
async def broadcast_text_post(call: CallbackQuery):
    try:
        kart = os.listdir("pics/broadcast")
        if kart[0] == 'cicada.jpg':
            path = f'pics/broadcast/cicada.jpg'
            with open(path, 'rb') as f:
                photo = f.read()
            ssm = open('sms.txt', 'r', encoding="utf-8").read()
            zz = ssm.split('|')
            sms = random.choice(zz)
            await call.message.answer_photo(photo=photo, caption=f"{ssm}\n\n"
                                                            f"<b>Все правильно? Отправляем?</b>",
                                    reply_markup=choose_menu)
    except:
        ssm = open('sms.txt', 'r', encoding="utf-8").read()
        zz = ssm.split('|')
        sms = random.choice(zz)
        await call.message.answer(ssm + "\n\n<b>Все правильно? Отправляем?</b>", reply_markup=choose_menu)

from telethon import TelegramClient, sync

@dp.callback_query_handler(text="invait")
async def gru(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Выбери куда добавлять пользователей</b>", reply_markup=inv)


@dp.callback_query_handler(text="ses_is_url", state="*")
async def canal(call: CallbackQuery, state: FSMContext):
    path = 'polzovateli'
    us = call.message.chat.id
    await call.message.answer("<b>'Конвертер в Sessions из URL Сылок\n\nВведи URL Адресса</b>")
    await akasil.urlses.set()


@dp.message_handler(state=akasil.urlses)
async def urlses(message: Message, state: FSMContext):
    url = message.text
    path = 'polzovateli'
    baza = []
    dd = url.split("\n")
    us = message.chat.id
    
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    dit_temp = f"{path}/{us}/tdata_to_sessions"
    for x in dd:
        baza.append(x)
    for tdata in os.listdir(f"{path}/{us}/tdata_to_sessions"):
        shutil.rmtree(f"{path}/{us}/tdata_to_sessions/{tdata}")
    fg = len(baza)
    sw = int(100/fg)
    ssw = int(100/fg)
    ms = await message.answer(
        f"<b>Выполняеться Скачивание {fg} Акаунтов</b>")
        
    for x in baza:
        y = x.split("/")[-1]
        z = x.split("/")[-1]
        nn = z.split("-")[0]
        os.system(f"curl -O {x}")
        await ms.edit_text(f"<b>Выполняеться Скачивание {fg} Акаунтов</b>\n\n"
                           f"<b>Выполненно {sw}%</b>")
        sw = sw + ssw
        rarobj = rarfile.RarFile(f"{y}")
        rarobj.extractall(dit_temp)
        time.sleep(3)
        os.system(f"del  {y}")
    ff = len(os.listdir(f"{path}/{us}/tdata_to_sessions"))
    msd = await message.answer(f"<b>Выполняеться Конвертация {ff} Акаунтов</b>")
    sessions = []
    API_HASH = "bd4bbac77f54cd096ede52dd2e8e2e50"
    API_ID = 17463049
    gg = int(100/ff)
    ggg = int(100/ff)
    for tdata in os.listdir(f"{path}/{us}/tdata_to_sessions"):
            
            auth_key = convert_tdata(f"{path}/{us}/tdata_to_sessions/{tdata}/tdata")[0]

            client =  TelegramClient(
                StringSession(auth_key),
                api_hash=API_HASH,
                api_id=API_ID
            )



            await client.connect()
            await msd.edit_text(f"<b>Выполненно {gg}%</b>")
            gg = gg + ggg
            auth_key =   client.session.save()
            with open(f"{path}/{us}/sessions/{tdata}.session", "w") as file:
                file.write(auth_key)
                await client.disconnect()



    await message.answer(f"<b>Сконвертированно: {len(baza)} шт</b>", reply_markup=back_to_main_menu)

@dp.callback_query_handler(text="lookfoto", state="*")
async def canal(call: CallbackQuery, state: FSMContext):
    path = 'polzovateli'
    us = call.message.chat.id
    fil = os.listdir(f"{path}/{us}/media/")
    
    for file in fil:
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton(text="Удалить Фото", callback_data=file))
        with open(f"{path}/{us}/media/{file}", "rb") as f:
            x = f.read()
        await bot.send_photo(chat_id=us, photo=x, reply_markup=keyboard)
    await call.message.answer("<b>Вернуться Не Удаляя Фото</>", reply_markup=back_to_main_menu)
    @dp.callback_query_handler(lambda c: c.data)
    async def poc_callback_but(c:CallbackQuery):
        ydal = c.data
        path = 'polzovateli'
        us = call.message.chat.id
        os.remove(f"{path}/{us}/media/{ydal}")
        await call.message.answer("<b>Фото Успешно Удаленно</b>", reply_markup=back_to_main_menu)


@dp.callback_query_handler(text="look_spam", state="*")
async def look_spam(call: CallbackQuery, state: FSMContext):
    path = 'polzovateli'
    us = call.message.chat.id
    sessionnss = []
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
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
    if file_list <= 1:
        await call.message.answer('<b>У Тебя Нет Акаунтов</b>',
                         reply_markup=back_to_main_menu)
    else:
        msg = await call.message.answer("<b>Запущен Процесс Проверка На Спам</b>")
        for file in os.listdir(f"{path}/{us}/sessions"):
            if file.endswith(".session"):
                session_path = os.path.join("sessions", file)
                aka = session_path.split("/")[1]
                akka = aka.split(".")[0]

                with open(f"{path}/{us}/{session_path}") as fileobj:
                        auth_key = fileobj.read()
                try:
                    session = TelegramClient(
                        StringSession(auth_key),
                        api_id,
                        api_hash,
                        device_model="Redmi Note 10",
                        lang_code="en",
                        system_lang_code="en"
                    )
                    await session.connect()
                    await session.send_message("SpamBot", "/start")
                    time.sleep(0.5)
                    messages = await session.get_messages("SpamBot", limit=1)
                    text = messages[0].message
                    if text != "Good news, no limits are currently applied to your account. You’re free as a bird!":
                        if "sending spam" in text:
                            await msg.edit_text("<b>Это вечное ограничение</b>")

                        else:
                            result = re.findall(r"\d+\s\w+\s\d{4}", text)
                            if len(result) == 0:
                                await msg.edit_text(f"<b>{text}</b>")

                            date = result[0]
                            await msg.edit_text(f"<b>{date}</b>")

                    else:
                        await msg.edit_text(f"<b>Аккаунт {akka} без блокировки спама</b>")

                except:
                    pass

        await msg.edit_text(f"<b>Проверка Завершена</b>", reply_markup=back_to_main_menu)


@dp.callback_query_handler(text="pass2fa", state="*")
async def pass2fa(call: CallbackQuery, state: FSMContext):
    path = 'polzovateli'
    us = call.message.chat.id
    sessionnss = []
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
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
    if file_list <= 1:
        await call.message.answer('<b>У Тебя Нет Акаунтов</b>',
                         reply_markup=back_to_main_menu)
    else:
        await call.message.answer("<b>Укажи Какой Установить Пароль </b>")
        await akasil.pass2fa.set()

@dp.message_handler(state=akasil.pass2fa)
async def pass2fa(message: Message, state: FSMContext):
    password = message.text
    path = 'polzovateli'
    us = message.chat.id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    msg = await message.answer(f"<b>Установка Облачного Пароля</b>")
    for file in os.listdir(f"{path}/{us}/sessions"):
        if file.endswith(".session"):
            session_path = os.path.join("sessions", file)
            aka = session_path.split("/")[1]
            akka = aka.split(".")[0]

            with open(f"{path}/{us}/{session_path}") as fileobj:
                    auth_key = fileobj.read()
            try:
                session = TelegramClient(
                    StringSession(auth_key),
                    api_id,
                    api_hash,
                    device_model="Redmi Note 10",
                    lang_code="en",
                    system_lang_code="en"
                )
                await session.connect()
                session.edit_2fa(new_password=password)
                await msg.edit_text(f"Пароль Успешно Применен Для Акаунта {akka}")
            except:
                await msg.edit_text(f"Не Удалось Установить Пароль Для Акаунта {akka}")
    await msg.edit_text(f"Пароль Успешно Применен Для Акаунтов", reply_markup=back_to_main_menu)


@dp.callback_query_handler(text="report", state="*")
async def report(call: CallbackQuery, state: FSMContext):
    path = 'polzovateli'
    us = call.message.chat.id
    sessionnss = []
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
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
    if users <= 0:
        await call.message.answer('<b>У Тебя Нет Списка Users</b>',
                         reply_markup=back_to_main_menu)
    if file_list <= 1:
        await call.message.answer('<b>У Тебя Нет Акаунтов</b>',
                         reply_markup=back_to_main_menu)
    if report <= 0:
        await call.message.answer('<b>У Тебя Нет Списка Report</b>',
                         reply_markup=back_to_main_menu)
    else:
        await call.message.answer("<b>Какой Тип Reporta Использовать ?</b>", reply_markup=repppo)
        await akasil.report.set()



@dp.callback_query_handler(text="spam_imag", state="*")
async def spam_imag(call: CallbackQuery, state: FSMContext):
    path = 'polzovateli'
    us = call.message.chat.id
    sessionnss = []
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
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
    if file_list <= 1:
        await call.message.answer('<b>У Тебя Нет Акаунтов</b>',
                         reply_markup=back_to_main_menu)
    if users <= 1:
        await call.message.answer('<b>У Тебя Нет Пользователей Для Спама</b>',
                         reply_markup=back_to_main_menu)
    if mes <= 0:
        await call.message.answer('<b>У Тебя Нет Текста Для Спама</b>',
                         reply_markup=back_to_main_menu)
    if izo <= 0:
        await call.message.answer('<b>У Тебя Нет Изображения Для Спама</b>',
                         reply_markup=back_to_main_menu)
    else:
        await call.message.answer("<b>Укажи Время Задержки Между отправками СМС</b>")
        await akasil.spam_imag.set()



@dp.message_handler(state=akasil.spam_imag)
async def spam_imag(message: Message, state: FSMContext):
    pauza = int(message.text)
    path = 'polzovateli'
    us = message.chat.id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    ff = len(os.listdir(f"{path}/{us}/sessions"))
    gg = int(100/ff)
    ggg = int(100/ff)
    msg = await message.answer(f"<b>Начат процесс Cпама По Списку </b>")
    fil = random.choice(os.listdir(f"{path}/{us}/media"))
    a = open(f"{path}/{us}/ussers.txt", 'r', encoding='utf-8').readlines()
    meees = open(f"{path}/{us}/message.txt", "r", encoding="utf-8").read()
    text = meees.split("$")
    baza = []
    for z in a:
        d = z.split("\n")
        for s in d:
            if s >= '0':
                baza.append(s)
    c = 0
    o = 0
    try:
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton(text="Остановить", callback_data="ssstop"))
        for file in os.listdir(f"{path}/{us}/sessions"):
            if file.endswith(".session"):
                session_path = os.path.join("sessions", file)
                aka = session_path.split("/")[1]
                akka = aka.split(".")[0]
                with open(f"{path}/{us}/{session_path}") as fileobj:
                        auth_key = fileobj.read()
                try:
                    session = TelegramClient(
                        StringSession(auth_key),
                        api_id,
                        api_hash,
                        device_model="Redmi Note 10",
                        lang_code="en",
                        system_lang_code="en"
                    )
                    await session.connect()
                except:
                    pass
                z = 0
                i = 0
                for z in baza:

                    if i == 35:
                        break
                    #try:
                    me = await session.get_me()
                    try:
                        v = await session.get_input_entity(z)     
                    except:
                        continue
                    usu = int(v.user_id)         
                    asa = await session.get_input_entity(PeerUser(usu))
                    mes = random.choice(text)
                    i = i + 1  
                    with open(f"{path}/{us}/media/{fil}", "rb") as f:
                        ph = f.read()
                        await session.send_file(
                                usu,
                                ph,
                                caption=mes,
                                parse_mode="html"
                            )
                    baza.remove(z) 
                    o = o + 1
                    mom = len(baza)
                    await msg.edit_text(                                
                                    f"✉️    <b>Рассылка с Акаунта:</b>    \n\n    <b>⚜️ {akka} 💠 </b>\n\n"
                                    f"<b>На пользователя 🗣 {z} ✅</b>\n\n"
                                    f"🛑    <b>Пауза между смс:</b>   <b>{pauza} сек</b>\n"
                                    f"<b>❌     Недоставленно:  {c}</b>\n"
                                    f"<b>✅     Доставленно:    {o}</b>\n\n"
                                    f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>", reply_markup=keyboard)
                
                    time.sleep(pauza)
                    open(f"{path}/{us}/ussers.txt", "w")
                    for x in baza:
                        with open(f"{path}/{us}/ussers.txt", "a", encoding="utf-8") as f:
                            f.write(f"{x}\n")
 
                await msg.edit_text(f"✉️    <b>💠 Рассылка Спама Завершена 💠</b>\n\n"
                                    f"<b>❌     Недоставленно:  {c}</b>\n"
                                    f"<b>✅     Доставленно:    {o}</b>\n\n", reply_markup=back_to_main_menu)
                break    
            
    except:
        await msg.edit_text(f"✉️    <b>💠 Рассылка Спама Завершена 💠</b>\n\n"
                            f"<b>❌     Недоставленно:  {c}</b>\n"
                            f"<b>✅     Доставленно:    {o}</b>\n\n", reply_markup=back_to_main_menu)





@dp.callback_query_handler(text="sp_spi", state="*")
async def sp_spi(call: CallbackQuery, state: FSMContext):
    path = 'polzovateli'
    us = call.message.chat.id
    sessionnss = []
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    for file in os.listdir(f"{path}/{us}/sessions"):
        if file.endswith(".session"):
            session_path = os.path.join("sessions", file)
            sessionnss.append(session_path)
    file_list = len(sessionnss)
    users = len(open(f"{path}/{us}/ussers.txt", "r", encoding="utf-8").readlines())
    mes = len(open(f"{path}/{us}/message.txt", "r", encoding="utf-8").read())
    if file_list <= 0:
        await call.message.answer('<b>У Тебя Нет Акаунтов</b>',
                         reply_markup=back_to_main_menu)
    if users <= 0:
        await call.message.answer('<b>У Тебя Нет Пользователей Для Спама</b>',
                         reply_markup=back_to_main_menu)
    if mes <= 0:
        await call.message.answer('<b>У Тебя Нет Текста Для Спама</b>',
                         reply_markup=back_to_main_menu)
    else:
        await call.message.answer("<b>Укажи Время Задержки Между отправками СМС</b>")
        await akasil.sp_spi.set()




@dp.message_handler(state=akasil.sp_spi)
async def sp_spi(message: Message, state: FSMContext):
    pauza = int(message.text)
    path = 'polzovateli'
    us = message.chat.id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    ff = len(os.listdir(f"{path}/{us}/sessions"))
    gg = int(100/ff)
    ggg = int(100/ff)
    msg = await message.answer(f"<b>Начат процесс Cпама По Списку </b>")
    a = open(f"{path}/{us}/ussers.txt", 'r', encoding='utf-8').readlines()
    meees = open(f"{path}/{us}/message.txt", "r", encoding="utf-8").read()
    text = meees.split("$")
    baza = []
    for zx in a:
        d = zx.split("\n")
        for s in d:
            if s >= '0':
                baza.append(s)

    ses = []
    for file in os.listdir(f"{path}/{us}/sessions"):
        if file.endswith(".session"):
            session_path = os.path.join("sessions", file)
            akaaka = session_path[9:]
            aka = akaaka.split(".")[0]
            akka = aka.split(".")[0]
            with open(f"{path}/{us}/{session_path}") as fileobj:
                    auth_key = fileobj.read()
                    ses.append(auth_key)
    c = 0
    h = 0
    for tg in ses:
        session = TelegramClient(
            StringSession(tg),
            api_id,
            api_hash,
            device_model="Redmi Note 10",
            lang_code="en",
            system_lang_code="en"
        )
        await session.connect()


        i = 0
        for x in baza:
            if i == 35:
                break
            
            me = await session.get_me()         
            v = await session.get_input_entity(x)          
            usu = int(v.user_id)         
            asa = await session.get_input_entity(PeerUser(usu))
            mes = random.choice(text)
            i = i + 1  
            try:
                await session.send_message(usu, mes, parse_mode="html")
                print(x)


                mom = len(baza)
                await msg.edit_text(                                
                            f"✉️    <b>Рассылка с Акаунта:</b>    \n\n    <b>⚜️ {me.first_name} 💠 </b>\n\n"
                            f"<b>На пользователя 🗣 {x} ✅</b>\n\n"
                            f"🛑    <b>Пауза между смс:</b>   <b>{pauza} сек</b>\n"
                            f"<b>❌     Недоставленно:  {c}</b>\n"
                            f"<b>✅     Доставленно:    {h}</b>\n\n"
                            f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>")
                h = h + 1
                baza.remove(x)
                time.sleep(pauza)
                open(f"{path}/{us}/ussers.txt", "w")
                for z in baza:
                    with open(f"{path}/{us}/ussers.txt", "a", encoding="utf-8") as f:
                        f.write(f"{z}\n")
                
            except:
                c = c + 1
                mom = len(baza)
                await msg.edit_text(                                
                            f"✉️    <b>Рассылка с Акаунта:</b>    \n\n    <b>⚜️ {me.first_name} 💠 </b>\n\n"
                            f"<b>На пользователя 🗣 {x} ✅</b>\n\n"
                            f"🛑    <b>Пауза между смс:</b>   <b>{pauza} сек</b>\n"
                            f"<b>❌     Недоставленно:  {c}</b>\n"
                            f"<b>✅     Доставленно:    {h}</b>\n\n"
                            f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>")
    await msg.edit_text(f"✉️    <b>💠 Рассылка Спама Завершена 💠</b>\n\n"
                        f"<b>❌     Недоставленно:  {c}</b>\n"
                        f"<b>✅     Доставленно:    {h}</b>\n\n")
    
                    
       


# ===============ADD/CHANGE ACCOUNT===========
@dp.callback_query_handler(text="add_account")
async def show_all_chats(call: CallbackQuery, state: FSMContext):
    msg_to_edit = await call.message.edit_text("<b>Напишите номер аккаунта. В формате +380xxxxxxxxx</b>",
                                               reply_markup=back_to_main_menu)
    await AddAccount.A1.set()
    await state.update_data(msg_to_edit=msg_to_edit)


@dp.message_handler(state=AddAccount.A1)
async def receive_number(message: Message, state: FSMContext):
    path = 'polzovateli'
    us = message.chat.id
    data = await state.get_data()
    msg_to_edit = data.get("msg_to_edit")
    number = message.text
    await message.delete()
    if os.path.exists(f"{path}/{us}/temp/{number}.session"):
        os.remove(f"{path}/{us}/temp/{number}.session")
        await update_session(number, None)
    client = TelegramClient(f"{path}/{us}/temp/{number}", api_id, api_hash)
    await client.connect()
    sent = await client.send_code_request(phone=number)
    await client.disconnect()
    await msg_to_edit.edit_text(f"<b>Вы указали <code>{number}</code>\n"
                                f"Укажите первую цифру кода:</b>",
                                reply_markup=code_menu)
    await AddAccount.next()
    await state.update_data(number=number, sent=sent, code_hash=sent.phone_code_hash)


@dp.callback_query_handler(text_startswith="code_number:", state=AddAccount.A2)
async def receive_code(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg_to_edit = data.get("msg_to_edit")
    num_1 = call.data.split(":")[1]
    await msg_to_edit.edit_text(f"<b>Код будет выстраиваться тут: <code>{num_1}</code></b>", reply_markup=code_menu)
    await AddAccount.next()
    await state.update_data(num_1=num_1)


@dp.callback_query_handler(text_startswith="code_number:", state=AddAccount.A3)
async def receive_code(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg_to_edit, num_1 = data.get("msg_to_edit"), data.get("num_1")
    num_2 = call.data.split(":")[1]
    code = num_1 + num_2
    await msg_to_edit.edit_text(f"<b>Код будет выстраиваться тут: <code>{code}</code></b>", reply_markup=code_menu)
    await AddAccount.next()
    await state.update_data(num_2=num_2)


@dp.callback_query_handler(text_startswith="code_number:", state=AddAccount.A4)
async def receive_code(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg_to_edit, num_1, num_2 = data.get("msg_to_edit"), data.get("num_1"), data.get("num_2")
    num_3 = call.data.split(":")[1]
    code = num_1 + num_2 + num_3
    await msg_to_edit.edit_text(f"<b>Код будет выстраиваться тут: <code>{code}</code></b>", reply_markup=code_menu)
    await AddAccount.next()
    await state.update_data(num_3=num_3)


@dp.callback_query_handler(text_startswith="code_number:", state=AddAccount.A5)
async def receive_code(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg_to_edit, num_1, num_2, num_3 = data.get("msg_to_edit"), data.get("num_1"), data.get("num_2"), data.get("num_3")
    num_4 = call.data.split(":")[1]
    code = num_1 + num_2 + num_3 + num_4
    await msg_to_edit.edit_text(f"<b>Код будет выстраиваться тут: <code>{code}</code></b>", reply_markup=code_menu)
    await AddAccount.next()
    await state.update_data(num_4=num_4)


@dp.callback_query_handler(state=AddAccount.A6)
async def receive_code(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    msg_to_edit, num_1, num_2, num_3 = data.get("msg_to_edit"), data.get("num_1"), data.get("num_2"), data.get("num_3")
    number, num_4, sent, code_hash = data.get("number"), data.get("num_4"), data.get("sent"), data.get("code_hash")
    num_5 = call.data.split(":")[1]
    code = num_1 + num_2 + num_3 + num_4 + num_5
    try:
        client = TelegramClient(f"{path}/{us}/sessions/{number}", api_id, api_hash)
        await client.connect()
        await client.sign_in(phone=number, code=code, phone_code_hash=code_hash)
        string = StringSession.save(client.session)
        with open(f"{path}/{us}/sessions/{number}.session", "w") as file:
            file.write(string)
        await client.disconnect()
        await update_session(call.from_user.id, call.from_user.id)
        await add_acc(call.from_user.id, number)
        await msg_to_edit.edit_text(f"<b>Готово, аккаунт добавлен</b>", reply_markup=back_to_main_menu)
        await update_acc_count()
        await state.finish()
        os.remove(f"{path}/{us}/temp/{number}")
    except Exception as e:
        print(e)
        await msg_to_edit.edit_text("Не верный код, или стоит облачный пароль, убери его и Попробуй заново.", reply_markup=back_to_main_menu)
        await client.disconnect()
        os.remove(f"{path}/{us}/temp/{number}")
        await state.finish()




@dp.callback_query_handler(text="add_to_chanel", state="*")
async def add_to_chanel(call: CallbackQuery, state: FSMContext):
    path = 'polzovateli'
    us = call.message.chat.id
    sessionnss = []
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
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
    if file_list <= 1:
        await call.message.answer('<b>У Тебя Нет Акаунтов</b>',
                         reply_markup=back_to_main_menu)
                        
    else:
        await call.message.answer("<b>Укажи Ссылку На Чат  Куда Вступить  Акаунтам</b>", reply_markup=back_to_main_menu)
        await akasil.add_chat.set()



@dp.message_handler(state=akasil.add_chat)
async def add_to_chanel(message: Message, state: FSMContext):
    invite = message.text
    path = 'polzovateli'
    us = message.chat.id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    ff = len(os.listdir(f"{path}/{us}/sessions"))
    gg = int(100/ff)
    ggg = int(100/ff)
    msg = await message.answer(f"<b>Начат процесс Вступления В Чат {ff}-и Акаунтам</b>")
    try:
        for file in os.listdir(f"{path}/{us}/sessions"):
            if file.endswith(".session"):
                session_path = os.path.join("sessions", file)

                with open(f"{path}/{us}/{session_path}") as fileobj:
                     auth_key = fileobj.read()
                try:
                    session = TelegramClient(
                        StringSession(auth_key),
                        api_id,
                        api_hash,
                        device_model="Redmi Note 10",
                        lang_code="en",
                        system_lang_code="en"
                    )
                    await session.connect()
                    await session(JoinChannelRequest(invite))
                    await msg.edit_text(f"<b>Выполнено {gg}%</b>")
                    gg = gg + ggg
                except:
                    pass
        await msg.edit_text(f"<b>процесс Вступления В Чат {ff}-и Акаунтав Успешно Завершен</b>", reply_markup=back_to_main_menu)
    except:
        await msg.edit_text("<b>Ссылка не Пренадлежит Группе Либо Чату, Или Указана Не Верно</b>", reply_markup=back_to_main_menu)

@dp.callback_query_handler(text="parser_groop", state="*")
async def parser_groop(call: CallbackQuery, state: FSMContext):
    path = 'polzovateli'
    us = call.message.chat.id
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Укажи Ссылку На Группу От Куда Парсить Пользователей</b>")
    await akasil.parser.set()

@dp.message_handler(state=akasil.parser)
async def parser(message: Message, state: FSMContext):
    invite = message.text
    path = 'polzovateli'
    us = message.chat.id
    baza = []
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    for file in os.listdir(f"{path}/{us}/sessions"):
        if file.endswith(".session"):
            session_path = os.path.join("sessions", file)
            baza.append(session_path)
    ses = random.choice(baza)
    with open(f"{path}/{us}/{ses}") as fileobj:
            auth_key = fileobj.read()
    # try:
    session = TelegramClient(
        StringSession(auth_key),
        api_id,
        api_hash,
        device_model="Redmi Note 10",
        lang_code="en",
        system_lang_code="en"
    )
    await session.connect()
    chats = []
    last_date = None
    chunk_size = 200
    groups=[]
    offset_user = 0
    limit_user = 300
    all_participants = [] 
    filter_user = ChannelParticipantsSearch('')
    await session(JoinChannelRequest(invite))
    open(f"{path}/{us}/ussers.txt", "w")
    msg = await message.answer(f"<b>Запущен Процесс Парсинга с Группы {invite}</b>")
    try:
        participants = await session(GetParticipantsRequest(invite,
            filter_user, offset_user, limit_user, hash=0))
        all_participants.extend(participants.users)

        offset_user += len(participants.users)
        all_users_details = [] 
        for participant in all_participants:
            dd = participant.status

           
            if  not participant.username == None:

                if participant.username not in all_users_details:
                    all_users_details.append(participant.username)
        
        for x in all_users_details:
            ss = x
            if not ss[-3:] == "bot":
                if not ss[-3:] == "Bot":
                    await msg.edit_text(
                            "<b>Спарсен 🗣 {} ✅ пользователь</b>"
                            .format(x)
                        )
                    with open(f"{path}/{us}/ussers.txt", "a") as f:
                        f.write(str(f"{x}\n"))
        
        await session(LeaveChannelRequest(invite))

        zx = len(open(f"{path}/{us}/ussers.txt", "r").readlines())
        await msg.edit_text(f"<b>Парсинг окончен Спарсено {zx} Пользователей</b>", reply_markup=back_to_main_menu)
    except:
        await message.answer("<b>Ссылка не Пренадлежит Группе Либо Указана Не Верно</b>", reply_markup=back_to_main_menu)





@dp.callback_query_handler(text="clean_dialog", state="*")
async def clean_dialog(call: CallbackQuery, state: FSMContext):
    path = 'polzovateli'
    us = call.message.chat.id
    sessionnss = []
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
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
    if file_list <= 1:
        await call.message.answer('<b>У Тебя Нет Акаунтов</b>',
                         reply_markup=back_to_main_menu)

    else:
        ff = len(os.listdir(f"{path}/{us}/sessions"))
        ggg = int(100/ff)
        gg = int(100/ff)
        msg = await call.message.answer("<b>Очистка Диалогов Запущенна</b>")
        for file in os.listdir(f"{path}/{us}/sessions"):
            if file.endswith(".session"):
                session_path = os.path.join("sessions", file)

                with open(f"{path}/{us}/{session_path}") as fileobj:
                     auth_key = fileobj.read()

                session = TelegramClient(
                    StringSession(auth_key),
                    api_id,
                    api_hash,
                    device_model="Redmi Note 10",
                    lang_code="en",
                    system_lang_code="en"
                )
                await session.connect()

                async for dialog in session.iter_dialogs():
                    if not isinstance(dialog.entity, types.Channel):
                        await session(functions.messages.DeleteHistoryRequest(
                            peer=dialog.entity,
                            max_id=0,
                            just_clear=True,
                            revoke=True
                        ))
                        await msg.edit_text(f"<b>Очистка Выполнена на {gg}%</b>")
                        gg = gg + ggg
                    else:
                        await session(
                            functions.channels.LeaveChannelRequest(dialog.id)
                        )

        await msg.edit_text(f"<b>Очистка Выполнена Успешно</b>", reply_markup=back_to_main_menu)




@dp.callback_query_handler(text="tdata", state="*")
async def tdata(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Отправь Папку Акаунта В Rar Архиве</b>\n"
                              f"<b>Порядок архива должен быть таким \n"
                              f"иначе конвертация небудет выполнена</b>\n\n"
                              f"|-Rar Архив\n"
                              f"|--Имя папки Акаунта\n"
                              f"|----tdata", reply_markup=back_to_main_menu)
    await sms4.tdata.set()

@dp.message_handler(content_types=['document'], state=sms4.tdata)
async def broadcast4(message: Message, state: FSMContext):
    path = 'polzovateli'
    us = message.chat.id
    dit_temp = f"{path}/{us}/tdata_to_sessions"
    for tdata in os.listdir(f"{path}/{us}/tdata_to_sessions"):
        shutil.rmtree(f"{path}/{us}/tdata_to_sessions/{tdata}")
    ss = message.document.file_name
    await message.document.download(f"{path}/{us}/{ss}")
    rarobj = rarfile.RarFile(f"{path}/{us}/{ss}")
    rarobj.extractall(dit_temp)
    time.sleep(3)
    os.remove(f"{path}/{us}/{ss}")
    ff = len(os.listdir(f"{path}/{us}/tdata_to_sessions"))
    msd = await message.answer(f"<b>Выполняеться Конвертация {ff} Акаунтов</b>")
    sessions = []
    API_HASH = "bd4bbac77f54cd096ede52dd2e8e2e50"
    API_ID = 17463049
    gg = int(100/ff)
    ggg = int(100/ff)
    for tdata in os.listdir(f"{path}/{us}/tdata_to_sessions"):
            try:
                auth_key = convert_tdata(f"{path}/{us}/tdata_to_sessions/{tdata}/tdata")[0]

                client =  TelegramClient(
                    StringSession(auth_key),
                    api_hash=API_HASH,
                    api_id=API_ID
                )



                await client.connect()
                await msd.edit_text(f"<b>Выполненно {gg}%</b>")
                gg = gg + ggg
                auth_key =   client.session.save()
                with open(f"{path}/{us}/sessions/{tdata}.session", "w") as file:
                    file.write(auth_key)
                    await client.disconnect()
            except:
                await msd.edit_text(f"<b>Акаунт Поврежден Либо Мертв</b>")


    await message.answer(f"<b>Сконвертированно: {ff} шт</b>", reply_markup=back_to_main_menu)







@dp.callback_query_handler(text="ffoto", state="*")
async def canal(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Отправь Фото Для Спама</b>", reply_markup=back_to_main_menu)
    await sms4.foto.set()

@dp.message_handler(content_types=['photo'], state=sms4.foto)
async def broadcast4(message: Message, state: FSMContext):
    path = 'polzovateli'
    us = message.chat.id
    ss = await message.photo[-1].get_file()
    rr = ss.file_path
    photo_name = rr.split("/")[1]
    easy_chars = 'abcdefghijklnopqrstuvwxyz1234567890'
    #name = 'cicada'
    #photo_name = name + ".jpg"
    await message.photo[-1].download(f"{path}/{us}/media/{photo_name}")
    await message.answer("<b>Фото успешно загруженно</b>", reply_markup=back_to_main_menu)


@dp.callback_query_handler(text="spisreport", state="*")
async def canal(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Введи Users Для Report</b>", reply_markup=back_to_main_menu)
    await sms4.sms_text.set()


@dp.message_handler(state=sms4.sms_text)
async def cann(message: Message, state: FSMContext):
    report = message.text
    path = 'polzovateli'
    us = message.chat.id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    usus = report.split("\n")
    await state.finish()
    print(usus)
    baza = []
    for x in usus:
        if x >= '0':
            baza.append(x)
    open(f"{path}/{us}/report.txt", "w")
    for x in baza:
        with open(f"{path}/{us}/report.txt", "a", encoding="utf-8") as f:
                    f.write(f"{x}\n")
    users = len(open(f"{path}/{us}/report.txt", "r", encoding="utf-8").readlines())
    await message.answer(f"<b>Добавленно {users} Пользователей</b>", reply_markup=back_to_main_menu)
#
#    ti = open('time.txt', 'r').read()
#    api_id = 16746278
#    api_hash = "ca3a465d4b961e137addeb2e4f9b6581"
#    file_list = os.listdir('sessions')
#    xx = len(file_list)
#    ss = open('ussers.txt', 'r').readlines()
#    z = len(ss)
#    if z <= 1:
#        await message.answer("Добать получателей список пуст !")
#
#    count = int(z)
#    i = 0
#    d = 0
#    s = 0
#    c = 0
#    o = 0
#    ss = os.listdir('sessions')
#    mom = len(ss)
#    a = 0
#    v = 0
#    while i <= xx:
#        try:
#            acaunt = file_list[i]
#            try:
#                npn  = int(open(f"check/{acaunt}.txt", "r").read())
#            except:
#                i = i + 1
#                continue
#            print(npn)
#            if npn <= 0:
#                i = i + 1
#                continue
#            if mom <= 0:
#                break
#            if v == z:
#                break
#            mm = 0
#            file_list = os.listdir('sessions')
#            akk = acaunt.split(".")[0]
#            cli = open(f"sessions/{acaunt}").read()
#            client = TelegramClient(StringSession(cli), api_id, api_hash)
#            await client.connect()
#            result = await client(functions.users.GetFullUserRequest(id="me"))
#            nam = result.user.first_name
#            lnam = result.user.last_name
#            if mm <= 20:
#
#                try:
#                    await client(JoinChannelRequest(channel))
#                    o = o + 1
#                    mom = mom - 1
#                    await msms.edit_text(
#                        f"<b>Добавленно в Группу: {o}</b>\n"
#                        f"<b>Добавлен пользователь {akk} в группу ✅</b>\n\n"
#                        f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>", reply_markup=ssttop)
#                    ti2 = open('time.txt', 'r')
#                    ti = int(ti2.read())
#                    ti2.close()
#                    time.sleep(ti)
#                    msm = msm + 1
#                    mm = mm + 1
#                    v = v + 1
#
#
#                    d = d + 1
#                except:
#
#                    mom = mom - 1
#                    await msms.edit_text(
#                        f"<b>Добавленно в Группу: {o}</b>\n"
#                        f"<b>Не Добавлен {akk} в группу ❌</b>\n\n"
#                        f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>", reply_markup=ssttop)
#                    ti2 = open('time.txt', 'r')
#                    ti = int(ti2.read())
#                    ti2.close()
#                    time.sleep(ti/2)
#                    d = d + 1
#                    v = v + 1
#        except:
#            i = i + 1
#    await message.answer("<b>Инвайт завершил работу</b>", reply_markup=back_to_main_menu)
#    await state.finish()


@dp.callback_query_handler(text="ppr", state="*")
async def gru(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Введи ссылку группы в таком формате: http://t.me/username/</b>", reply_markup=back_to_main_menu)
    await sms5.sms_text.set()



@dp.message_handler(state=sms3.sms_text)
async def gruuu(message: Message, state: FSMContext):
    channel = message.text
    msms = await message.answer("<b>Начинаю Инвайт Группы</b>")
    await message.delete()
    ti = open('time.txt', 'r').read()
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581"
    file_list = os.listdir('sessions')
    xx = len(file_list)
    ss = open('ussers.txt', 'r').readlines()
    z = len(ss)
    if z <= 1:
        await message.answer("Добать получателей список пуст !")

    count = int(z)
    i = 1
    d = 0
    ss = open('ussers.txt', 'r').readlines()
    mom = len(ss)
    c = 0
    o = 0
    msm = 0
    a = 0
    v = 0
    while i <= xx:
        try:
            if mom <= 0:
                break
            if d == 15:
                i = i + 1
            if v == z:
                break
            mm = 0
            file_list = os.listdir('sessions')
            acaunt = file_list[i]
            try:
                npn  = int(open(f"chec/{acaunt}.txt", "r").read())
            except:
                i = i + 1
                continue
            print(npn)
            if npn <= 0:
                i = i + 1
                continue
            cli = open(f"sessions/{acaunt}").read()
            client = TelegramClient(StringSession(cli), api_id, api_hash)
            await client.connect()
            await client(JoinChannelRequest(channel))

            if mm <= 20:
                ss = open('ussers.txt', 'r').readlines()
                user = ss[a][:-1]
                akk = acaunt.split(".")[0]
                #await client(functions.channels.InviteToChannelRequest(channel=channel, users = [user]))
                try:
                    await client(InviteToChannelRequest(channel=channel, users = [user]))
                    o = o + 1
                    mom = mom - 1
                    await msms.edit_text(
                        f"<b>Добавленно в Группу: {o}</b>\n"
                        f"<b>Добавлен пользователь {user} в группу ✅</b>\n\n"
                        f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>", reply_markup=ssttop)
                    ti2 = open('time.txt', 'r')
                    ti = int(ti2.read())
                    ti2.close()
                    time.sleep(ti)
                    mm = mm + 1
                    v = v + 1
                    a = a + 1
                    d = d + 1

                except:
                    mom = mom - 1
                    await msms.edit_text(
                        f"<b>Добавленно в Группу: {o}</b>\n"
                        f"<b>Не Добавлен {user} в группу ❌</b>\n\n"
                        f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>", reply_markup=ssttop)
                    ti2 = open('time.txt', 'r')
                    ti = int(ti2.read())
                    ti2.close()
                    time.sleep(ti/2)
               #     except:
               #     time.sleep(ti/2)
               #     await message.answer(f"<b>Не вышло добавить пользователь {user} в группу ❌</b>")
               #     d = d + 1
                    a = a + 1
               #     v = v + 1
        except:
          ##  print("ne policilos")
            i = i + 1

    await message.answer("<b>Инвайт завершил работу</b>", reply_markup=back_to_main_menu)
    await state.finish()
ban = []
@dp.callback_query_handler(text="svspis", state="*")
async def canal(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Введи Users Для Спама</b>", reply_markup=back_to_main_menu)
    await sms4.spam.set()

@dp.callback_query_handler(text="textspam", state="*")
async def textspam(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Введи Сообщения Для Спама,</b>\n"
                             f"<b>Для использования Рандомных Смс Используй Символ $</b>\n"
                             f"<b>Пример Ввода:</b>\n\n"
                             f"     <code>text1 $text2 $text3</code>", reply_markup=back_to_main_menu)
    await sms4.textspam.set()



@dp.message_handler(state=sms4.textspam)
async def textspam(message: Message, state: FSMContext):
    text = message.text
    path = 'polzovateli'
    us = message.chat.id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    await state.finish()

    with open(f"{path}/{us}/message.txt", "w", encoding="utf-8") as f:
                    f.write(f"{text}")

    await message.answer(f"<b>Текст Для Спама Успешно Добавлен </b>", reply_markup=back_to_main_menu)


@dp.message_handler(state=sms4.spam)
async def svoispisok(message: Message, state: FSMContext):
    spisok = message.text
    path = 'polzovateli'
    us = message.chat.id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    usus = spisok.split("\n")
    await state.finish()
    print(usus)
    baza = []
    for x in usus:
        if x >= '0':
            baza.append(x)
    open(f"{path}/{us}/ussers.txt", "w")
    for x in baza:
        with open(f"{path}/{us}/ussers.txt", "a", encoding="utf-8") as f:
                    f.write(f"{x}\n")
    users = len(open(f"{path}/{us}/ussers.txt", "r", encoding="utf-8").readlines())
    await message.answer(f"<b>Добавленно {users} Пользователей</b>", reply_markup=back_to_main_menu)



@dp.callback_query_handler(text="prox", state="*")
async def canal(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Введи Proxy В Таком формате:</b>\n"
                              f"<b>ip:port:login:pass</b>", reply_markup=back_to_main_menu)
    await sms4.proxy.set()




@dp.message_handler(state=sms4.proxy)
async def svoispisok(message: Message, state: FSMContext):
    spisok = message.text
    path = 'polzovateli'
    us = message.chat.id
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    usus = report.split("\n")
    await state.finish()
    print(usus)
    baza = []
    for x in usus:
        if x >= '0':
            baza.append(x)
    open(f"{path}/{us}/proxy.txt", "w")
    for x in baza:
        with open(f"{path}/{us}/proxy.txt", "a", encoding="utf-8") as f:
                    f.write(f"{x}\n")
    users = len(open(f"{path}/{us}/proxy .txt", "r", encoding="utf-8").readlines())
    await message.answer(f"<b>Добавленно {users} шт</b>", reply_markup=back_to_main_menu)


from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.channels import LeaveChannelRequest
@dp.message_handler(state=sms5.sms_text)
async def gruuu(message: Message, state: FSMContext):
    ch = message.text
    await message.answer("<b>Начинаю парсинг.....</b>")
    ti = open('time.txt', 'r').read()
    api_id = 16746278
    api_hash = "ca3a465d4b961e137addeb2e4f9b6581"
    file_list = os.listdir('sessions')
    xx = len(file_list)
    ss = open('ussers.txt', 'r').readlines()
    z = len(ss)
    file_list = os.listdir('sessions')
    sht = len(file_list)
    xaka = random.randint(0, sht)
    acaunt = file_list[3]
    cli = open(f"sessions/{acaunt}").read()
    client = TelegramClient(StringSession(cli), api_id, api_hash)
    await client.connect()

    await client(JoinChannelRequest(ch))
    chats = []
    last_date = None
    chunk_size = 200
    groups=[]
    offset_user = 0
    limit_user = 1000

    all_participants = []   # список всех участников канала
    filter_user = ChannelParticipantsSearch('')

    participants = await client(GetParticipantsRequest(ch,
        filter_user, offset_user, limit_user, hash=0))

    all_participants.extend(participants.users)
    offset_user += len(participants.users) # len(participants.users)
    await message.answer("<b>Идет сохранения списка.....</b>")
    all_users_details = []   # список словарей с интересующими параметрами участников канала
    for participant in all_participants:
        dd = participant.status

        if  not participant.username == None:
            all_users_details.append(participant.username)


    for x in all_users_details:
        ss = x
        if not ss[-3:] == "bot":
            with open("ussers.txt", "a") as f:
                f.write(str(f"{x}\n"))
    zx = len(open('ussers.txt', 'r').readlines())
    await client(LeaveChannelRequest(ch))
    await message.answer(
        f"<b>Список сохранен</b>\n"
        f"<b>Получено {zx} пользователей</b>", reply_markup=back_to_main_menu)

async def sending_check(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        nv2 = (datetime.now().strftime("%d %B, %Y"))
        nv = (datetime.now().strftime("%H:%M:%S"))
        print(nv2)
        if nv[:7] == "12:00:0":
            print(nv2)
            #with open(f"{username}.db", "rb") as doc:
                #await bot.send_document(692916588,
                                       ## doc,
                                       # caption=f"📦 BACKUP\n"
                                        #        f"🕜 {tt}")

            time.sleep(2)
vv = int('6')
async def on_startup2(vv):
    while True:
        await asyncio.sleep(vv)
        nv2 = (datetime.now().strftime("%d %b %Y, %H:%M"))
        nv = (datetime.now().strftime("%H:%M:%S"))
        off_spam = open("spam/spam.txt", "r", encoding="utf-8").readlines()


        for x in off_spam:
            offs = x.split()
            voz = offs[0]
            vz = voz.split("'")
            wernyt = vz[1]
            pr = f"{offs[2]} {offs[3]} {offs[4]} {offs[5]}"
            if pr == nv2:
                shutil.move(f"spam/{wernyt}", f"sessions/{wernyt}")
                with open("spam/spam.txt", "w", encoding="utf-8") as f:
                    f.writelines(off_spam[1:])

       # if nv[:7] == "12:00:0":
       #     print(nv2)
       #     time.sleep(5)

"""
    @dp.callback_query_handler(text="stop_spam")
    async def st(call: CallbackQuery):
        with open("stop.txt", "w") as f:
            f.write("1")

    tmr = Timer(1.0, start_clock)
    tmr.start()
    """


@dp.callback_query_handler(text="stop_spam")
async def st(call: CallbackQuery):
    await call.answer("Ожидай выполняеться Остановка !!!")
    with open("stop.txt", "w") as f:
        f.write("1")

# START BROADCAST
@dp.callback_query_handler(text="go_start")
async def broadcast_text_post(call: CallbackQuery):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    ft = open("foto.txt", "r").read()
    if ft == "+++":
        ded = await call.message.answer("<b>Спам Рассылка Запущенна !</b>")
        api_id = 16746278
        api_hash = "ca3a465d4b961e137addeb2e4f9b6581"
        file_list = os.listdir('sessions')
        xx = len(file_list)
        ss = open('ussers.txt', 'r').readlines()
        mom = len(ss)
        open("otcet.txt", "w", encoding="utf-8")
        with open("stop.txt", "w") as f:
            f.write("0")
        i = 0
        p = 0
        t = 0
        c = 0
        o = 0
        propusk = 0

        while xx >= i:
            acaunt = file_list[i]
            try:
                npn  = int(open(f"check/{acaunt}.txt", "r").read())
            except:
                i = i + 1
                continue
            print(npn)
            if npn <= 0:
                i = i + 1
                continue
            akk = acaunt.split(".")[0]
            ti = int(open('time.txt', 'r').read())
            sto = int(open('stop.txt', 'r').read())
            if sto == 1:
                await call.message.answer("stop", reply_markup=back_to_main_menu)
                break
            try:
                cli = open(f"sessions/{acaunt}").read()
                client = TelegramClient(StringSession(cli), api_id, api_hash)
                await client.connect()
            except:
                client = TelegramClient(f"sessions/{acaunt}", api_id, api_hash)
                await client.connect()

            fff = open("pics/broadcast/cicada.jpg", 'rb').read()
            ssm = open('sms.txt', 'r', encoding="UTF-8").read()
            zz = ssm.split('|')
            sms = random.choice(zz)
            try:
                file_list2 = open('ussers.txt', 'r').readlines()
            except:
                await call.message.answer("Рассылка завершена", reply_markup=back_to_main_menu)


            if propusk == 3:
                #await client.disconnect()
                i = i + 1
                t = t - 9
                propusk = 0
            if mom <= 0:
                break

            if p >= 3:
                ban.append(acaunt)
                #await client.disconnect()
                i = i + 1
                p = p - 40
            if len(file_list2) >= p:
                try:
                    with open("ussers.txt", "r") as z:
                        lines = z.readlines()
                        far = lines[0][:-1]

                    with open("ussers.txt", "w") as f:
                        f.writelines(lines[1:])
                    xxw = await client.get_entity(far)
                    await client.send_file(xxw, file=fff, caption=ssm)
                    with open("ussers.txt", "w") as f:
                        f.writelines(lines[1:])
                    p = p + 1
                    propusk = 0
                    t = t + 1
                    o = o + 1
                    result = await client(functions.users.GetFullUserRequest(id="me"))
                    nam = result.user.first_name
                    lnam = result.user.last_name
                    await ded.edit_text(
                                f"✉️    <b>Рассылка с Акаунта:</b>    \n\n    <b>⚜️ {akk} 💠 {nam} {lnam} ⚜️</b>\n\n"
                                f"<b>На пользователя 🗣 {far} ✅</b>\n\n"
                                f"🛑    <b>Пауза между смс:</b>   <b>{ti} сек</b>\n"
                                f"<b>❌     Недоставленно:  {c}</b>\n"
                                f"<b>✅     Доставленно:    {o}</b>\n\n"
                                f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>", reply_markup=ssttop)
                    mom = mom - 1


                    time.sleep(ti)
                except:
                    p = p + 1
                    t = t + 1
                    c = c + 1
                    result = await client(functions.users.GetFullUserRequest(id="me"))
                    nam = result.user.first_name
                    lnam = result.user.last_name

                    await ded.edit_text(
                                f"✉️    <b>Рассылка с Акаунта:</b>    \n\n    <b>⚜️ {akk} 💠 {nam} {lnam} ⚜️</b>\n\n"
                                f"<b>На пользователя 🗣 {far} ❌</b>\n\n"
                                f"🛑    <b>Пауза между смс:</b>   <b>{ti} сек</b>\n"
                                f"<b>❌     Недоставленно:  {c}</b>\n"
                                f"<b>✅     Доставленно:    {o}</b>\n\n"
                                f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>", reply_markup=ssttop)
                    with open("ussers.txt", "w") as f:
                        f.writelines(lines[1:])
                    time.sleep(ti/2)
                    propusk = propusk + 1
                    mom = mom - 1
                    await client.disconnect()
            else:
                await client.disconnect()
                i = i + 1
                mom = mom - 1
        sto = int(open('stop.txt', 'r').read())
        if sto == 1:
            await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
            await call.message.answer("Рассылка остановлена", reply_markup=back_to_main_menu)
        else:
            await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
            await call.message.answer("✅ <b>Рассылка Завершена</b> ✅", reply_markup=back_to_main_menu)


    if ft == "---":
        ded = await call.message.answer("<b>Спам Рассылка Запущенна !</b>")
        api_id = 16746278
        api_hash = "ca3a465d4b961e137addeb2e4f9b6581"
        file_list = os.listdir('sessions')
        xx = len(file_list)
        ss = open('ussers.txt', 'r').readlines()
        mom = len(ss)
        open("otcet.txt", "w", encoding="utf-8")
        with open("stop.txt", "w") as f:
            f.write("0")
        i = 0
        p = 0
        t = 0
        c = 0
        o = 0
        propusk = 0

        while xx >= i:
            acaunt = file_list[i]
            akk = acaunt.split(".")[0]
            ti = int(open('time.txt', 'r').read())
            sto = int(open('stop.txt', 'r').read())
            if sto == 1:

                break
            try:
                cli = open(f"sessions/{acaunt}").read()
                client = TelegramClient(StringSession(cli), api_id, api_hash)
                await client.connect()
            except:
                client = TelegramClient(f"sessions/{acaunt}", api_id, api_hash)
                await client.connect()

           
            ssm = open('sms.txt', 'r', encoding="UTF-8").read()
            zz = ssm.split('|')
            sms = random.choice(zz)
            try:
                file_list2 = open('ussers.txt', 'r').readlines()
            except:
                await call.message.answer("Рассылка завершена", reply_markup=back_to_main_menu)


            if propusk == 3:
                #await client.disconnect()
                i = i + 1
                t = t - 9
                propusk = 0
            if mom <= 0:
                break

            if p >= 3:
                ban.append(acaunt)
                #await client.disconnect()
                i = i + 1
                p = p - 40
            if len(file_list2) >= p:
                try:
                    with open("ussers.txt", "r") as z:
                        lines = z.readlines()
                        far = lines[0][:-1]
                    xxw = await client.get_entity(far)
                    await client.send_message(far, ssm)
                    with open("ussers.txt", "w") as f:
                        f.writelines(lines[1:])
                    p = p + 1
                    propusk = 0
                    t = t + 1
                    o = o + 1
                    result = await client(functions.users.GetFullUserRequest(id="me"))
                    nam = result.user.first_name
                    lnam = result.user.last_name
                    await ded.edit_text(
                                f"✉️    <b>Рассылка с Акаунта:</b>    \n\n    <b>⚜️ {akk} 💠 {nam} {lnam} ⚜️</b>\n\n"
                                f"<b>На пользователя 🗣 {far} ✅</b>\n\n"
                                f"🛑    <b>Пауза между смс:</b>   <b>{ti} сек</b>\n"
                                f"<b>❌     Недоставленно:  {c}</b>\n"
                                f"<b>✅     Доставленно:    {o}</b>\n\n"
                                f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>", reply_markup=ssttop)
                    mom = mom - 1

                    time.sleep(ti)
                except:
                    p = p + 1
                    t = t + 1
                    c = c + 1
                    result = await client(functions.users.GetFullUserRequest(id="me"))
                    nam = result.user.first_name
                    lnam = result.user.last_name

                    await ded.edit_text(
                                f"✉️    <b>Рассылка с Акаунта:</b>    \n\n    <b>⚜️ {akk} 💠 {nam} {lnam} ⚜️</b>\n\n"
                                f"<b>На пользователя 🗣 {far} ❌</b>\n\n"
                                f"🛑    <b>Пауза между смс:</b>   <b>{ti} сек</b>\n"
                                f"<b>❌     Недоставленно:  {c}</b>\n"
                                f"<b>✅     Доставленно:    {o}</b>\n\n"
                                f"<b>‼️ Осталось 👩‍👩‍👧‍👧 {mom}</b>", reply_markup=ssttop)
                    with open("ussers.txt", "w") as f:
                        f.writelines(lines[1:])
                    time.sleep(ti/2)
                    propusk = propusk + 1
                    mom = mom - 1
                    await client.disconnect()
            else:
                await client.disconnect()
                i = i + 1
                mom = mom - 1
        sto = int(open('stop.txt', 'r').read())
        if sto == 1:
            await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
            await call.message.answer("Рассылка остановлена", reply_markup=back_to_main_menu)
        else:
            await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
            await call.message.answer("✅ <b>Рассылка Завершена</b> ✅", reply_markup=back_to_main_menu)






@dp.callback_query_handler(text="ceker")
async def broadcast_text_post(call: CallbackQuery, state: FSMContext):
    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    await call.message.answer("<b>Меню Загрузки</b>", reply_markup=zagruzki)
    #api_id = 16746278
    #api_hash = "ca3a465d4b961e137addeb2e4f9b6581"
    #file_list = os.listdir('sessions')
    #xx = len(file_list)
    #with open("stop.txt", "w") as f:
    #    f.write("0")
    #xox = len(file_list)
    #i = 0
    #s = 0
    #sp = 0
    #tit = 0
    #r = 1
    #ydalen = []
    #pr = 1
    #while i <= xx:
    #    try:
    #        sto = int(open('stop.txt', 'r').read())
    #        if sto == 1:
#
    #            break
    #        mm = 0
    #        file_list = os.listdir('sessions')
    #        acaunt = file_list[i]
#
    #        cli = open(f"sessions/{acaunt}").read()
    #        client = TelegramClient(StringSession(cli), api_id, api_hash)
    #        await client.connect()
#
    #        channel_username = "SpamBot"
    #        gg = await client.send_message(channel_username, "/start")
    #        kk = gg.peer_id.user_id
    #        posts = await client.get_messages(
    #                gg.peer_id.user_id
    #                )
#
    #        for x in posts:
    #            fff = x.message
    #            with open(f"check\\{acaunt}.txt", "w") as m:
    #                m.write("10")
    #            if fff == 'Good news, no limits are currently applied to your account. You’re free as a bird!':
    #                await call.message.edit_text(
    #                    f"✅    <b>Рабочих акаунтов доступно: {r}</b>\n"
    #                    f"❌    <b>В Спаме:  {sp}</b>\n"
    #                    f"❌❌❌   <b>Мертвые:  {tit}</b>\n"
    #                    f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
    #                    f"<b>Акаунт \n💠 {acaunt.split('.')[0]}💠 </b> ✅\n"
    #                    f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
    #                    f"<b>SpamBot:  {fff[10:20]}</b>\n"
    #                    f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
    #                    f"<b>Проверенно {pr} Из {xx}</b>\n\n"
    #                    f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
    #                    f"<b>Осталось проверить {xox}</b>", reply_markup=ssttop)
    #                pr = pr + 1
    #                i = i + 1
    #                xox = xox - 1
    #                r = r + 1
    #                time.sleep(2)
    #                await client.disconnect()
#
    #            if not fff == 'Good news, no limits are currently applied to your account. You’re free as a bird!':
    #                with open("spam.txt", "w", encoding="utf-8") as f:
    #                        f.write(str(fff))
    #                ssppam = open("spam.txt", "r", encoding="utf-8").readlines()
    #                spm = ssppam[1].split("until")
    #                await call.message.edit_text(
    #                        f"✅    <b>Рабочих акаунтов доступно: {r}</b>\n"
    #                        f"❌    <b>В Спаме:  {sp}</b>\n"
    #                        f"❌❌❌   <b>Мертвые:  {tit}</b>\n"
    #                        f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
    #                        f"<b>Акаунт \n💠 {acaunt.split('.')[0]}💠 </b> ❌\n"
    #                        f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
    #                        f"<b>SpamBot:  {spm[1][:-1]}</b>\n"
    #                        f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
    #                        f"<b>Проверенно {pr} Из {xx}</b>\n\n"
    #                        f"➖➖➖➖➖➖➖➖➖➖➖➖\n"
    #                        f"<b>Осталось проверить {xox}</b>", reply_markup=ssttop)
#
    #                with open("spam/spam.txt", "a") as ff:
    #                    ff.write(str(f"{[acaunt, spm[1][:-1]]}\n"))
    #                shutil.move(f"sessions/{acaunt}", f"spam/{acaunt}")
    #                sp = sp + 1
    #                time.sleep(2)
    #                await client.disconnect()
    #                i = i + 1
    #                xox = xox - 1
    #                pr = pr + 1
#
    #    except:
    #        time.sleep(2)
    #        ydalen.append(acaunt)
    #        tit = len(ydalen)
    #        await client.disconnect()
    #        i = i + 1
    #        xox = xox - 1
    #        pr = pr + 1
    #if sto == 1:
    #    await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)
    #    await call.message.answer("Проверка остановлена", reply_markup=back_to_main_menu)
    #else:
    #    keyboard = InlineKeyboardMarkup()
    #    for x in ydalen:
    #        keyboard.add(InlineKeyboardButton(text=x.split('.')[0], callback_data=x))
    #    keyboard.add(InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu"))
#
    #    await call.message.answer(
    #                            f"🔍    <b>Проверка Завершена</b> !\n\n"
    #                            f"✅    <b>Рабочих акаунтов доступно: {r}</b>\n"
    #                            f"❌    <b>В Спаме:  {sp}</b>\n"
    #                            f"❌❌❌   <b>Мертвые:  {tit}</b>\n")
    #    await call.message.answer('<b>Какой Акаунт Удалить ?</b>\n\n', reply_markup=keyboard)
    #    @dp.callback_query_handler(lambda c: c.data)
    #    async def poc_callback_but(c:CallbackQuery):
    #        ydal = c.data
    #        os.remove(f"sessions/{ydal}")
    #        await call.message.answer(f'<b>✅ Акаунт {ydal.split(".")[0]} Удален ✅</b>', reply_markup=back_to_main_menu)
#
@dp.callback_query_handler(text="xxx")
async def exitt(call: CallbackQuery):
    await call.message.edit_text("<b>меню</b>", reply_markup=back_to_main_menu)
@dp.callback_query_handler(lambda c: c.data)
async def poc_callback_but(c:CallbackQuery):
    stop = c.data
    if stop == "ssstop":
        await call.message.answer("<b>Рассылка Остановленна</b>", reply_markup=back_to_main_menu)
    else:
        pass
