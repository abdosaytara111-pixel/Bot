from highrise_bot import BaseBot, Highrise
import asyncio
import os

from modules.welcome import WelcomeSystem
from modules.commands import CommandSystem

class MyBot(BaseBot):
    def __init__(self):
        self.welcome = WelcomeSystem(self)
        self.commands = CommandSystem(self)

    async def on_start(self, session_metadata):
        print("🚀 Bot started!")

    async def on_chat(self, user, message):
        await self.commands.handle(user, message)

    async def on_user_join(self, user):
        await self.welcome.send(user)

async def main():
    bot = MyBot()
    hr = Highrise(
        bot=bot,
        token=os.getenv("BOT_TOKEN"),
        room_id=os.getenv("ROOM_ID")   # 👈 هنا
    )
    await hr.run()

asyncio.run(main())
