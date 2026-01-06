import asyncio
from bot.client import bot_app
import bot.handlers 
import logging
logging.basicConfig(level=logging.INFO)
from pyrogram.types import BotCommand


async def main():
    await bot_app.start()
    await bot_app.set_bot_commands([
        BotCommand("start", "Start the bot"),
        BotCommand("help", "Show help")
    ])
    print("Bot is running")
    await asyncio.Event().wait()

asyncio.run(main())
