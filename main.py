import logging
from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler
import random

bot = Bot(token=os.getenv("BOT_TOKEN"))
user_id = 123456789  # آیدی عددی عشقت

messages = [
    "صبح بخیر عشق من ☀️ روزت مثل لبخندت روشن باشه 💖",
    "تو دلیل لبخند هر روز منی 😍",
    "هر صبح با یاد تو طلوع می‌کنه 🌅",
    "بی‌تو صبحا بی‌معناست… دوستت دارم 💌",
    "خورشید طلوع می‌کنه، ولی تویی که دلمو روشن می‌کنی ☀️❤️"
]

def send_romantic_message():
    msg = random.choice(messages)
    bot.send_message(chat_id=user_id, text=msg)

scheduler = BlockingScheduler()
scheduler.add_job(send_romantic_message, 'cron', hour=7, minute=0)

logging.basicConfig(level=logging.INFO)
print("LoveBot running… ❤️")
scheduler.start()
