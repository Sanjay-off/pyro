import asyncio
from bot.client import bot_app
import bot.handlers  # This imports and registers all handlers BEFORE bot starts
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
        # Handlers are already registered via the import above
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
        logger.info(f"Bot @{me.username} is now running!")
        logger.info(f"Bot ID: {me.id}")
        
        # Keep the bot running and listening for updates
        await asyncio.Event().wait()
        
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        await bot_app.stop()
        logger.info("Bot stopped")

if __name__ == "__main__":
    asyncio.run(main())