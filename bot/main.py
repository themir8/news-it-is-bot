import pathlib
import os

import dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.files import PickleStorage

from config.logger import logger_init
from .handlers import start_handler

# Load dotenv
dotenv.load_dotenv()

# Configure logging.
# 4-levels for logging: INFO, DEBUG, WARNING, ERROR
logger_init("INFO")


async def main():
    """Main function"""

    # Initialize bot and dispatcher
    bot = Bot(token=os.getenv("API_TOKEN"))
    try:
        storage = PickleStorage(pathlib.Path("db"))
        dp = Dispatcher(bot, storage=storage)
        # start_handler register
        dp.register_message_handler(
            start_handler, commands={"start"}, state="*")
        # text_handler register
        # dp.register_message_handler(
        #     text_handler, content_types="text")
        await dp.start_polling()
    finally:
        await bot.close()
