from pyrogram import Client, filters
from pyrogram.types import Message
from app import Bot
from configs import ADMINS
from TeamTeleroid.database import full_userbase, del_user
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked
from asyncio import sleep

@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("Broadcasting...")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await sleep(e.value)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
            total += 1
        
        status = f"""Broadcast Completed
Total Users: {total}
Successful: {successful}
Blocked Users: {blocked}
Deleted Accounts: {deleted}
Unsuccessful: {unsuccessful}"""
        
        return await pls_wait.edit(status)
    else:
        await message.reply("Reply to a message to broadcast.")