from pyrogram import Client, filters
from app import Bot
from configs import LOG_CHANNEL_ID, CHANNEL_ID, ADMINS
from TeamTeleroid.helpers import encode
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Bot.on_message(filters.group & filters.chat(LOG_CHANNEL_ID) & ~filters.command(['start']) & ~filters.user(ADMINS))
async def handle_query(client: Client, message: Message):
    movie_name = message.text.strip().lower()
    # Search database channel for matching caption
    search_results = []
    async for msg in client.search_messages(CHANNEL_ID, query=movie_name, limit=1):  # Limit to 1 for simplicity
        if msg.document or msg.video:
            search_results.append(msg.id)
    
    if search_results:
        msg_id = search_results[0]
        string = f"get-{msg_id * abs(client.db_channel.id)}"
        base64_string = await encode(string)
        link = f"https://t.me/{client.username}?start={base64_string}"
        reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Get File", url=link)]])
        await message.reply(f"Found {movie_name}. Click to access:", reply_markup=reply_markup)
    else:
        await message.reply(f"No match for {movie_name}.")