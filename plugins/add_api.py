from pyrogram import Client, filters
from app import Bot
from configs import ADMINS

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('add_api'))
async def add_api(client: Client, message: Message):
    # Logic to add API, e.g., for shortener
    await message.reply("API added. (Implement storage here.)")