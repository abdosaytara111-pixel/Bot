from highrise import BaseBot, Highrise
import asyncio, os

class Bot(BaseBot):
    async def on_start(self, session_metadata):
        print("Bot connected successfully!")

    async def on_chat(self, user, message):
        if message == "هلا":
            await self.highrise.chat(f"أهلاً يا {user.username} 🇪🇬")

async def main():
    bot = Bot()
    hr = Highrise(
        bot=bot,
        token=os.getenv("BOT_TOKEN"),
        room_id=os.getenv("ROOM_ID")
    )
    await hr.run()

asyncio.run(main())
