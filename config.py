import os

OWNER_ID = 7322925570   # твой Telegram ID
BOT_TOKEN = os.getenv("BOT_TOKEN")
DATA_FILE = "data.json"

DEFAULTS = {
    "banned_words": [],
    "allowed_links": [],
    "enabled": True,
    "mode": "admins",
    "bot_admins": [],
    "warn_message": "🚫 {user} написал {reason} и получил предупреждение.",
    "mute_message": "🚫 {user} написал {reason} и получил мут на {time}.",
    "ban_message": "🚫 {user} написал {reason} и был заблокирован.",
    "action_words": "warn",
    "action_links": "mute",
    "mute_seconds_words": 300,
    "mute_seconds_links": 600
}
