from aiogram import Router, F
from aiogram.types import Message
from aiogram.exceptions import TelegramForbiddenError
from filters import check_banned, check_link
from storage import data, save_data, ensure_chat

router = Router()

async def punish(message: Message, action: str, reason: str, cfg: dict):
    try:
        await message.delete()
    except TelegramForbiddenError:
        pass

    user = message.from_user.mention_html()
    if action == "warn":
        await message.chat.send_message(cfg["warn_message"].format(user=user, reason=reason, time=""))
    elif action == "mute":
        await message.chat.restrict(
            user_id=message.from_user.id,
            permissions={"can_send_messages": False},
            until_date=cfg["mute_seconds_words"]
        )
        await message.chat.send_message(cfg["mute_message"].format(user=user, reason=reason, time=f"{cfg['mute_seconds_words']}s"))
    elif action == "ban":
        await message.chat.ban(user_id=message.from_user.id)
        await message.chat.send_message(cfg["ban_message"].format(user=user, reason=reason, time=""))

@router.message(F.text)
async def moderation_handler(message: Message):
    chat_id = str(message.chat.id)
    cfg = ensure_chat(chat_id)

    if not cfg["enabled"]:
        return

    text = message.text or ""
    bad = check_banned(text, cfg["banned_words"])
    if bad:
        return await punish(message, cfg["action_words"], bad, cfg)

    link = check_link(text, cfg["allowed_links"])
    if link:
        return await punish(message, cfg["action_links"], link, cfg)
