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

To add in your group contact us at @DARK_TELEGRAMER 

Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ Source", url="https://github.com/abhijithabhis/NIVA_BOT"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Support", url="https://t.me/NivaBotSupport"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/gscatoffi"
                    ),
                [
                    InlineKeyboardButton(
                        "Donate the coder", url="https://www.paypal.me/devilgaurav"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
