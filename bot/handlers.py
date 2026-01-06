from pyrogram import filters
from bot.client import bot_app

@bot_app.on_message(filters.command("start") & filters.private)
async def start_handler(client, message):
    """Handle /start command"""
    user_name = message.from_user.first_name
    await message.reply_text(
        f"👋 Hello {user_name}!\n\n"
        f"Welcome to the bot. I'm now working correctly!\n\n"
        f"Use /help to see available commands."
    )

@bot_app.on_message(filters.command("help"))
async def help_handler(client, message):
    """Handle /help command"""
    help_text = """
📚 **Available Commands:**

/start - Start the bot
/help - Show this help message
/about - Learn about this bot
/echo [text] - Echo back your message

Just send me any text and I'll respond!
    """
    await message.reply_text(help_text)

@bot_app.on_message(filters.command("about"))
async def about_handler(client, message):
    """Handle /about command"""
    await message.reply_text(
        "🤖 **About This Bot**\n\n"
        "This is a learning bot built with Pyrogram.\n"
        "Framework: Pyrogram\n"
        "Version: 1.0.0\n"
        "Developer: Your Name"
    )

@bot_app.on_message(filters.command("echo"))
async def echo_handler(client, message):
    """Echo back the user's message"""
    # Get text after the command
    text = message.text.split(maxsplit=1)
    
    if len(text) > 1:
        await message.reply_text(f"🔊 Echo: {text[1]}")
    else:
        await message.reply_text("Please provide text to echo. Example: /echo Hello World")

@bot_app.on_message(filters.text & ~filters.command("start") & ~filters.command("help") & ~filters.command("about") & ~filters.command("echo"))
async def text_handler(client, message):
    """Handle any other text message"""
    await message.reply_text(
        f"You said: {message.text}\n\n"
        f"I received your message! Use /help to see what I can do."
    )