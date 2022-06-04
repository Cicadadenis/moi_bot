import os
import asyncio
from rich.console import Console
from contextlib import contextmanager, asynccontextmanager
from typing import List, Dict
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
import time
import rich
import rich.progress
from states.states import sessions

console = Console()


class SessionsStorage:
    def __init__(self, directory, api_id, api_hash):
        self.full_sessions: Dict[str, TelegramClient] = {}

        self.initialize = True
        path = 'polzovateli'
        us = sessions.ses
        print()
        for file in rich.progress.track(os.listdir('sessions')):
            if file.endswith(".session"):
                session_path = os.path.join("sessions", file)

                with open(session_path) as fileobj:
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

                        self.full_sessions[session_path] = session
                except:
                    pass

                

        if self.initialize:
            try:
                rich.print()
                with console.status("Инициализация..."):
                    asyncio.get_event_loop().run_until_complete(
                        asyncio.wait([
                            self.check_session(session, path)
                            for path, session in self.full_sessions.items()
                        ])
                    )
            except:
                pass
    async def check_session(self, session, path):
        rich.print()
        #console.log(f"Инициализация сеанса {path}")

        try:
            await session.connect()
        except Exception as err:
            console.log(f"Session {path} returned error. {err}. Удаление.")
            del self.full_sessions[path]
            os.remove(path)
            os.system("cls")
            return

        if not await session.is_user_authorized():
            console.log(f"Инициализация {path} мертв. Удаление его")
            del self.full_sessions[path]
            os.remove(path)
            return
        
        console.log(f"Инициализация {path}")

    def get_session_path(self, session: TelegramClient) -> str:
        for path, client in self.full_sessions.items():
            if client == session:
                return path

    @property
    def sessions(self) -> List[TelegramClient]:
        return list(self.full_sessions.values())

    @contextmanager
    def initialize_session(self, session):
        if not self.initialize:
            session.connect()

        yield

        if not self.initialize:
            session.disconnect()

    @asynccontextmanager
    async def ainitialize_session(self, session):
        if not self.initialize:
            await session.connect()
            time.sleep(3)

        yield

        if not self.initialize:
            await session.disconnect()
            time.sleep(3)
    def __len__(self):
        return len(self.sessions)
        
