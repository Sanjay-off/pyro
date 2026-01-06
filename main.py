import asyncio
from bot.client import bot_app
import bot.handlers  # This imports and registers all handlers
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

from pyrogram.types import BotCommand

async def main():
    """Main function to start the bot"""
    try:
        # Start the bot
        await bot_app.start()
        logger.info("Bot started successfully!")
        
        # Set bot commands (shows in menu)
        await bot_app.set_bot_commands([
            BotCommand("start", "Start the bot"),
            BotCommand("help", "Show help message"),
            BotCommand("about", "About this bot"),
            BotCommand("echo", "Echo your message")
        ])
        logger.info("Bot commands set successfully!")
        
        # Get bot information
        me = await bot_app.get_me()
        logger.info(f"Bot is running as @{me.username}")
        
        # Keep the bot running
        await asyncio.Event().wait()
        
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        await bot_app.stop()
        logger.info("Bot stopped")

if __name__ == "__main__":
    asyncio.run(main())