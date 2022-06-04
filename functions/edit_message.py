import asyncio
import os, time
import random
from rich.prompt import Prompt, Confirm
from rich.console import Console
from multiprocessing import Process
from telethon import events, types
import os 
import webbrowser
from functions.function import Function
from tkinter import * 
from tkinter import filedialog, Tk, messagebox

console = Console()

class ReportFunc(Function):
    """Изменить Текст Спам Сообшения"""
    async def execute(self):
        def logo():
            console.print("[blink blue]      _             __         ___       __[/]", justify="center")
            console.print("[blink blue]  ____(_)______ ____/ /__ _____/ _ )___  / /_[/]", justify="center")
            console.print("[blink yellow] / __/ / __/ _ `/ _  / _ `/___/ _  / _ \/ __/[/]", justify="center")
            console.print("[blink yellow]\__/_/\__/\_,_/\_,_/\_,_/   /____/\___/\__/[/]", justify="center")
            console.print("[blink blue]----------Telegram-Bot-Cicada3301-----------[/]", justify="center")

        root=Tk()
        root.geometry('498x550')
        root.wm_title('Добавление Текста Для спама')
        root.iconbitmap('core\py\ccc.ico')
        root.resizable(False, False)
        lb = Label(root, text="Для Рандомизации Текста \nПеред Следующим Сообщениям Нужно Поставить Символ $\nПример: \n\ntext1 $text2 $text3", bg='silver')
        lb.pack(padx=30)
        def retrieve_input():
            inputValue=textBox.get("1.0","end-1c")
            with open("message.txt", "w", encoding="utf-8") as f:
                f.write(inputValue)
            root.destroy()
            os.system("cls")
            logo()
            console.print("[italic blue]\n\n\n\nТекст Успешнно Изменнен[/]", justify="center")
            time.sleep(3)
        textBox=Text(root, height=15, width=30)
        textBox.pack(pady=50)
        buttonCommit=Button(root, height=1, width=10, text="Добавить", 
                            command=lambda: retrieve_input())
        buttonCommit.pack()
        root.mainloop()                           