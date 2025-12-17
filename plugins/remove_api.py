from pyrogram import Client, filters
from app import Bot
from configs import ADMINS

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('remove_api'))
async def remove_api(client: Client, message: Message):
    # Logic to remove API
    await message.reply("API removed.")