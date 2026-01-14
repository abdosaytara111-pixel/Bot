import os
import asyncio
from highrise import BaseBot, Highrise

class MyBot(BaseBot):
    async def on_start(self, session_metadata):
        print("✅ مبروك! البوت شغال دلوقتي أونلاين على Koyeb")
        print(f"User ID: {session_metadata.user_id}")

    async def on_chat(self, user, message):
        print(f"اللاعب {user.username} قال: {message}")
        if message.lower() == "ping":
            self.highrise.send_chat("Pong! 🏓")

if __name__ == "__main__":
    token = os.environ.get("BOT_TOKEN")
    room_id = os.environ.get("ROOM_ID")
    
    if not token or not room_id:
        print("❌ خطأ: لم يتم العثور على BOT_TOKEN أو ROOM_ID في الإعدادات!")
    else:
        from highrise.__main__ import main
        # السطر ده اللي بيشغل البوت
        main()