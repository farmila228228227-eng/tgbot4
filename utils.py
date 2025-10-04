from aiogram import Bot
from config import OWNER_ID

async def is_admin(bot: Bot, chat_id: int, user_id: int):
    if user_id == OWNER_ID:
        return True
    try:
        member = await bot.get_chat_member(chat_id, user_id)
        return member.is_chat_admin()
    except:
        return False
