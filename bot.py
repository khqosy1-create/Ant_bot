import os
from telethon import TelegramClient, events

api_id = int(os.environ.get("API_ID", 0))
api_hash = os.environ.get("API_HASH", "")
bot_token = os.environ.get("BOT_TOKEN", "")

client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    await event.respond('أهلاً بك! بوت الحماية يعمل بنجاح على مدار الساعة 🛡️')

print("Bot is running...")
client.run_until_disconnected()
