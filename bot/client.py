from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

bot_app = Client(
    "bot_session",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN
)
