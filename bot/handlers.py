from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from aiogram.types import InlineQuery, \
    InputTextMessageContent, InlineQueryResultArticle
import loguru

# from bot.queries import create_user, get_all_articles, get_article, get_blog
# from bot.models import User
# from bot.buttons import back_btn, main_btn, article_menu


async def start_handler(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    input_json = {
        "user_id": message.from_user.id,
        "username": message.from_user.username,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
    }
    # user = User(**input_json)
    # create_user(user)
    # await message.answer("Hi!", reply_markup=main_btn("Мой блог"))
