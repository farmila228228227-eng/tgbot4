import re

LINK_REGEX = re.compile(r"(https?://|t\.me/|telegram\.me|www\.)", re.IGNORECASE)

def check_banned(text, banned_words):
    for w in banned_words:
        if re.search(rf"\b{re.escape(w)}\b", text, re.IGNORECASE):
            return w
    return None

def check_link(text, allowed_links):
    if not text: return None
    if LINK_REGEX.search(text):
        for domain in allowed_links:
            if domain.lower() in text.lower():
                return None
        return "link"
    return None
