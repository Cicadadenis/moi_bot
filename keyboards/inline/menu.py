from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import *

# =========================================================
# ========================MAIN MENU========================
from utils.db_api.db_commands import select_user_accounts, select_user



async def main_menu(user_id):
    user = await select_user(user_id)
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[

            [
                InlineKeyboardButton(text="🗳 Добавить Акаунты", callback_data="adddd")
            ],

            [
                InlineKeyboardButton(text="🔲 Загрузки", callback_data="ceker")
            ],
            [
                InlineKeyboardButton(text="🔄 Изменения", callback_data="sms")
            ],

            [
                InlineKeyboardButton(text="🧬 Конвертеры", callback_data="broadcast")
            ],

            [
                InlineKeyboardButton(text="🔧 Работа С Акаунтами", callback_data="use")
            ],
            [
                InlineKeyboardButton(text="📩 Спамеры", callback_data="fdel")
            ],

            [
                InlineKeyboardButton(text="🔍 Поиск Чатов", callback_data="paussa")
            ],
            #[
            #    InlineKeyboardButton(text=f"{'✅' if user[6] == 1 else '⛔️'}Выходить после спам атаки",
             #                        callback_data="leave")
            #],

            #[
            #    InlineKeyboardButton(text="📝Изменить фото", callback_data=f"ed`photo`{chat_id}"),
            #    InlineKeyboardButton(text="🗑Удалить", callback_data=f"ed`del`{chat_id}")
            #],
#
            #[
            #    InlineKeyboardButton(text="🔕Рассылка выключена" if is_on == 0 else "🔔Рассылка включена",
            #                         callback_data=f"ed`turn`{chat_id}")
            #],

 

        ]
    )
    return keyboard


repppo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Жестокое обращение с ребенком", callback_data="rep1")
        ],
        [
            InlineKeyboardButton(text="Авторские права", callback_data="rep2")
        ],

        [
            InlineKeyboardButton(text="Поддельный канал/аккаунт", callback_data="rep3")
        ],

        [
            InlineKeyboardButton(text="Порнография", callback_data="rep4")
        ],
        [
            InlineKeyboardButton(text="Спам", callback_data="rep5")
        ],

        [
            InlineKeyboardButton(text="Насилие", callback_data="rep6")
        ],

        [
            InlineKeyboardButton(text="Другой", callback_data="rep7")
        ],
        
        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]

    ]
)

spamer = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Спам По Списку", callback_data="spam_fo_spis")
        ],
        [
            InlineKeyboardButton(text="Спам По Списку Текстом И Картинкой", callback_data="spam_imag")
        ],

        [
            InlineKeyboardButton(text="Флуд в личку", callback_data="floodls")
        ],

        [
            InlineKeyboardButton(text="Флуд в чат", callback_data="floodchat")
        ],
        [
            InlineKeyboardButton(text="Флуд на комментарии к каналу", callback_data="floodcomm")
        ],

        [
            InlineKeyboardButton(text="Запустить Report", callback_data="report")
        ],
        
        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]

    ]
)


maka = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Очистить все диалоги", callback_data="clean_dialog")
        ],
        [
            InlineKeyboardButton(text="Парсер Групп", callback_data="parser_groop")
        ],

        [
            InlineKeyboardButton(text="Присоединяйтесь к голосовому чату", callback_data="add_voice")
        ],

        [
            InlineKeyboardButton(text="Присоединяйтесь к чату", callback_data="add_to_chanel")
        ],
        [
            InlineKeyboardButton(text="Проверить На Спам", callback_data="look_spam")
        ],

        [
            InlineKeyboardButton(text="Установить 2fa пароль", callback_data="pass2fa")
        ],
        
        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]

    ]
)

konver = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Конвертер в Sessions из URL", callback_data="ses_is_url")
        ],


        [
            InlineKeyboardButton(text="Конвертер С Формата Tdata", callback_data="tdata")
        ],
        
        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]

    ]
)

izmenen = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Изменить биографию", callback_data="bio")
        ],
        [
            InlineKeyboardButton(text="Изменить имена", callback_data="rename")
        ],

        [
            InlineKeyboardButton(text="Изменить фото профиля", callback_data="refoto")
        ],
        
        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]

    ]
)


ydal = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Удалить Фото", callback_data="fottodell")
        ]
    ]
)

zagruzki = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Загрузить Users Для Report", callback_data="spisreport")
        ],
        [
            InlineKeyboardButton(text="Загрузить Свой Список Для Спама", callback_data="svspis")
        ],

        [
            InlineKeyboardButton(text="Загрузить Текст Для Спама", callback_data="textspam")
        ],

        [
            InlineKeyboardButton(text="Загрузить Список Прокси", callback_data="prox")
        ],

        [
            InlineKeyboardButton(text="Загрузить Фото Для Спама", callback_data="ffoto")
        ],

        [
            InlineKeyboardButton(text="Посмотреть Фото Из Списка", callback_data="lookfoto")
        ],
        
        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]

    ]
)


goo = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💣 Начать 💣", callback_data="back_to_main_menu")
        ]
    ]
)


akiy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✔️ Добавить по номеру", callback_data="add_account")
        ],

        [
            InlineKeyboardButton(text="✔️ Загрузить sessions", callback_data="ad_sesion")
        ],
        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]
    ]
)



userrs = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📋 Посмотреть список", callback_data="spisok_us")
#            InlineKeyboardButton(text="📥 Загрузить список", callback_data="usse")
        ],

        [
            InlineKeyboardButton(text="➕ Добавить в список", callback_data="adusse"),
            InlineKeyboardButton(text="➖ Очистить список", callback_data="rmusse")
        ],

        [
            InlineKeyboardButton(text="➕ Фаил с username ", callback_data="fuser") 
        ],

        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]
    ]
)
# ========================PERSONAL ACCOUNT========================
# MAIN PERSONAL ACCOUNT MENU
personal_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📥Пополнить баланс📥", callback_data="deposit")
        ],
        [
            InlineKeyboardButton(text="📖Все заказы", callback_data="my_orders"),
            InlineKeyboardButton(text="📖Статус заказа", callback_data="show_order_status")
        ],
        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]
    ]
)

code_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1️⃣", callback_data="code_number:1"),
            InlineKeyboardButton(text="2️⃣", callback_data="code_number:2"),
            InlineKeyboardButton(text="3️⃣", callback_data="code_number:3"),
        ],
        [
            
            InlineKeyboardButton(text="4️⃣", callback_data="code_number:4"),
            InlineKeyboardButton(text="5️⃣", callback_data="code_number:5"),
            InlineKeyboardButton(text="6️⃣", callback_data="code_number:6")
        ],
        [
            
            InlineKeyboardButton(text="7️⃣", callback_data="code_number:7"),
            InlineKeyboardButton(text="8️⃣", callback_data="code_number:8"),
            InlineKeyboardButton(text="9️⃣", callback_data="code_number:9")
        ],
        [
            InlineKeyboardButton(text="0️⃣", callback_data="code_number:0")
            
        ],
        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]
    ]
)

start_spam_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💬 В чат", callback_data="spam:chat"),
            InlineKeyboardButton(text="💌 В лс", callback_data="spam:user")
        ],
        [
            InlineKeyboardButton(text="🤖В бота", callback_data="spam:bot")
        ],
        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]
    ]
)
ssttop = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⛔️Остановить", callback_data="stop_spam")
        ]
    ]
)
proxy_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✔️Добавить", callback_data="add_proxy"),
            InlineKeyboardButton(text="❗️Удалить", callback_data="del_proxy")
        ],
        [
            InlineKeyboardButton(text="🔙Назад", callback_data="back_to_main_menu")
        ]
    ]
)

accept_spam_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🚀Запустить атаку", callback_data="accept_spam"),
        ],
        [
            InlineKeyboardButton(text="✖️Отмена", callback_data="back_to_main_menu")
        ]
    ]
)

# =========================================================
# ========================ADMIN MENU========================
# MAIN ADMIN MENU
admin_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📮Рассылка", callback_data="broadcast")
        ],
        [
            InlineKeyboardButton(text="✅Выдать доступ", callback_data="give_time"),
            InlineKeyboardButton(text="⛔️Забрать доступ", callback_data="take_time")
        ],
        [
            InlineKeyboardButton(text="🔙В главное меню", callback_data="back_to_main_menu")
        ]
    ]
)

# BACK TO ADMIN MENU BUTTON
back_admin = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️Назад", callback_data="back_admin")
        ]
    ]
)

# DELETE BROADCAST MESSAGE
broadcast_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="❇️Понял❇️", callback_data="delete_this_message")
            #"delete_this_message")
        ]
    ]
)

# BROADCAST CONFIRM MENU
choose_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅Да", callback_data="yes")
        ],
       # [
        #    InlineKeyboardButton(text="❌Нет", callback_data="xxx")
        #]
    ]
)

# ========================BACK TO MAIN MENU BUTTON========================
back_to_main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️Назад", callback_data="back_to_main_menu")
        ]
    ]
)


# ========================CHATS MENU========================
# ALL USER CHATS
async def accounts_menu(user_id):
    accs = await select_user_accounts(user_id)
    keyboard = InlineKeyboardMarkup(row_width=2)
    for acc in accs:
        keyboard.insert(InlineKeyboardButton(text=acc[1], callback_data=f"accounts:{acc[1]}"))
    keyboard.add(InlineKeyboardButton(text="➕ Добавить аккаунт", callback_data="add_account"))
    keyboard.add(InlineKeyboardButton(text="🔙Назад", callback_data=f"back_to_main_menu"))
    return keyboard


# INSIDE CHAT
def in_chat_menu(is_on, chat_id, number):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="📝Изменить текст🔰", callback_data=f"ed`text`{chat_id}"),
                InlineKeyboardButton(text="📝Изменить задержку", callback_data=f"ed`delay`{chat_id}")
            ],
            [
                InlineKeyboardButton(text="📝Изменить фото", callback_data=f"ed`photo`{chat_id}"),
                InlineKeyboardButton(text="🗑Удалить", callback_data=f"ed`del`{chat_id}")
            ],
            [
                InlineKeyboardButton(text="🔕Рассылка выключена" if is_on == 0 else "🔔Рассылка включена",
                                     callback_data=f"ed`turn`{chat_id}")
            ],
            [
                InlineKeyboardButton(text="⬅️Назад", callback_data=f"accounts:{number}")
            ]
        ]
    )
    return keyboard
