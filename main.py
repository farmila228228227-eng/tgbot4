import asyncio
from aiogram import Bot, Dispatcher
import moderation, panel
from config import BOT_TOKEN

bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()

dp.include_router(moderation.router)
dp.include_router(panel.router)

async def main():
    print("🚀 Бот запущен")
    await dp.start_polling(bot)

if __name__ == "__main__":
    if not BOT_TOKEN:
        raise RuntimeError("❌ BOT_TOKEN не найден. Добавь его в Replit Secrets.")
    asyncio.run(main())
