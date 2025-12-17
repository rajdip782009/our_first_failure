from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from app import Bot
from configs import OWNER_ID

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"? Creator : [This Person](tg://user?id={OWNER_ID})\n? Language : `Python3`\n? Library : Pyrogram",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup([
                [ InlineKeyboardButton("Close", callback_data = "close") ]
            ])
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
    elif data == "verify_gplink":
        # Simulate verification; in real, check if user visited link
        # Here, on click, send the file (assume message has data)
        await query.answer("Verified! Sending file...")
        # Get the file ID from query.message or context (implement based on start.py)
        file_msg_id = query.data.split("_")[1]  # Example: verify_gplink_123
        msg = await client.get_messages(client.db_channel.id, int(file_msg_id))
        await msg.copy(query.from_user.id)
        await query.message.delete()