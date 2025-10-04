from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from storage import data, save_data, ensure_chat
from utils import is_admin

router = Router()

def main_menu(chat_id):
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🚫 Список слов", callback_data=f"words:{chat_id}")],
        [InlineKeyboardButton(text="🌐 Белый список ссылок", callback_data=f"links:{chat_id}")],
        [InlineKeyboardButton(text="⚡ Статус: Вкл/Выкл", callback_data=f"toggle:{chat_id}")],
    ])

@router.message(F.text == "/panel")
async def open_panel(message: Message):
    chat_id = str(message.chat.id)
    if not await is_admin(message.bot, message.chat.id, message.from_user.id):
        return await message.answer("🚫 Нет доступа")
    ensure_chat(chat_id)
    await message.answer("⚙️ Панель управления:", reply_markup=main_menu(chat_id))

@router.callback_query(F.data.startswith("toggle"))
async def toggle_filter(callback: CallbackQuery):
    chat_id = callback.data.split(":")[1]
    cfg = ensure_chat(chat_id)
    cfg["enabled"] = not cfg["enabled"]
    save_data(data)
    await callback.message.edit_text(
        f"⚙️ Панель управления:\n\nФильтр: {'✅ ВКЛ' if cfg['enabled'] else '❌ ВЫКЛ'}",
        reply_markup=main_menu(chat_id)
    )
    await callback.answer("Изменено!")
