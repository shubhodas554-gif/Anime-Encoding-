from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

class AutoAnimeBot(Client):
    def __init__(self):
        super().__init__(
            "AnimeXMafiaBot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            sleep_threshold=5,
        )
        self.queue = []
        self.status = type("Status", (), {"text": ""})()
        self.UPLOADS_CHANNEL_ID = None
        self.INDEX_CHANNEL_ID = None
        self.schedule = None
