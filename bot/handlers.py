from pyrogram import filters
# from bot.client import bot_app

# @bot_app.on_message(filters.command("start"))
# async def start_handler(client, message):
#     await message.reply_text(
#         "Welcome! Bot started and responding."
#     )
from bot.client import bot_app

@bot_app.on_message(filters.text)
async def handle_text(client, message):
    if message.text and message.text.lower().startswith("/start"):
        await message.reply_text("Start matched raw text")
