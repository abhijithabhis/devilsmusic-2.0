from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi dear {message.from_user.first_name}!</b>

I am Niva Group Radio Bot, an open-source bot that lets you play music in your Telegram groups voice chat.
This bot is based on su music project and hamkers vc bot. 
