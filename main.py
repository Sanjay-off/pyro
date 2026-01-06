import asyncio
from bot.client import bot_app
import bot.handlers 
import logging
logging.basicConfig(level=logging.INFO)

async def main():
    await bot_app.start()
    print("Bot is running")
    await asyncio.Event().wait()

asyncio.run(main())
