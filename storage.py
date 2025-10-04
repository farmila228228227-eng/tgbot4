import os, json
from config import DATA_FILE, DEFAULTS

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

data = load_data()

def ensure_chat(chat_id: str):
    if chat_id not in data:
        data[chat_id] = DEFAULTS.copy()
        save_data(data)
    return data[chat_id]
