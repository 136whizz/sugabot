from telethon import TelegramClient
import logging
import time

openai_key = "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"
api_id = "18200930"
api_hash = "8e0c2f2528850bbd44405cb2b617a4e2"
bot_token = "6019079009:AAFQGxSjiTEbr1ypfY0E3WgzNqx0LwKktPY"

bot = TelegramClient("harrypbot", api_id, api_hash).start(bot_token = bot_token)