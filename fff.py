
import asyncio
import os
import random
from random import randint
from telethon import TelegramClient, Button, events 
from datetime import datetime, timedelta

from telethon.tl.functions.messages import ImportChatInviteRequest

from telethon.tl.functions.channels import JoinChannelRequest
import json
from typing import Any
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
#from convert_tdata import convert_tdata
import time
from telethon.sync import TelegramClient
from telethon import connection

# для корректного переноса времени сообщений в json
from datetime import date, datetime

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.messages import GetHistoryRequest

import os, sys
import configparser
import csv
import time
import random


import rarfile
import shutil
import re
import requests
from datetime import datetime
import time

import os
from telethon.sync import TelegramClient
from telethon import functions, types
from datetime import datetime, timedelta

ch = "https://t.me/s_a_t_a_n_a_6_6"

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
acaunt = file_list[5]
cli = open(f"sessions/79361101321.session", "r", encoding="utf-8").read()
client = TelegramClient(StringSession(cli), api_id, api_hash)
client.connect()
print("1")

channel_username = "SpamBot"
gg = client.send_message(channel_username, "/start")
kk = gg.peer_id.user_id

print(kk)

posts = client.get_messages(
    gg.peer_id.user_id
)



for x in posts:
    print(x.message)
    input()