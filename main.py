from highrise_bot import BaseBot, Highrise
import asyncio

class Bot(BaseBot):
    async def on_start(self, session_metadata):
        print("Bot is running!")

    async def on_chat(self, user, message):
        if message == "هلا":
            await self.highrise.chat(f"أهلاً يا {user.username} 🇪🇬")

async def main():
    bot = Bot()
    hr = Highrise(
        bot=bot,
        token="PUT_YOUR_TOKEN_HERE"
    )
    await hr.run()

asyncio.run(main())
