from pyrogram import Client, filters
from app import Bot
from configs import ADMINS
from TeamTeleroid.database import full_userbase
from TeamTeleroid.helpers import get_readable_time
from datetime import datetime

@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text="Fetching...")
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(f"BOT UPTIME: {time}")