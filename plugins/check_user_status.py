from pyrogram import Client, filters
from app import Bot
from configs import ADMINS
from TeamTeleroid.database import present_user

@Bot.on_message(filters.private & filters.command('status') & filters.user(ADMINS))
async def check_status(client: Client, message: Message):
    user_id = message.from_user.id
    if await present_user(user_id):
        await message.reply("User is active.")
    else:
        await message.reply("User not found.")