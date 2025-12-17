from pyrogram import Client, filters
from app import Bot
from configs import ADMINS

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('connect'))
async def connect(client: Client, message: Message):
    await message.reply("Connected to channels. (Implement connection logic if needed.)")