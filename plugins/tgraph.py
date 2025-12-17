from pyrogram import Client, filters
from app import Bot
from configs import ADMINS

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('tgraph'))
async def tgraph(client: Client, message: Message):
    await message.reply("Generating graph... (Implement graph logic.)")