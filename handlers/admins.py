from pyrogram import Client, filters
from pyrogram.types import Message
from tgcalls import mashal
import sira
from config import SUDO_USERS
from cache.admins import set
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command("pause")
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def pause(client: Client, message: Message):
    if tgcalls.pause(message.chat.id):
        await message.reply_text("Paused⏺️")
    else:
        await message.reply_text("No stream detected")



@Client.on_message(
    filters.command("resume")
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def resume(client: Client, message: Message):
    if callsmusic.resume(message.chat.id):
        await message.reply_text("Resumed▶️")
    else:
        await message.reply_text("No paused stream detected 🎉🎉")


@Client.on_message(
    filters.command(["stop", "end"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def stop(client: Client, message: Message):
    if message.chat.id not in tgcalls.GroupsOn:
        await message.reply_text("Nothing is being streamed")
    else:
        try:
            sira.clear(message.chat.id)
        await tgcalls.gooff(message.chat.id)
        await message.reply_text("Cleared the queue and left the call!")

@Client.on_message(
    filters.command(["skip", "next"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def skip(client: Client, message: Message):
    if message.chat.id not in tgcalls.GroupsOn:
        await message.reply_text("No set stream")
    else:
        sira.task_done(message.chat.id)

        if sira.is_empty(message.chat.id):
            await tgcalls.gooff(message.chat.id)
        else:
            await tgcalls.setsong(
                message.chat.id, sira.get(message.chat.id)["file_path"]
            )

        await message.reply_text("Skipped!")

@Client.on_message(
    filters.command("admincache")
)
@errors
@admins_only
async def admincache(client, message: Message):
    set(message.chat.id, [member.user for member in await message.chat.get_members(filter="administrators")])
    await message.reply_text("❇️ Admin cache refreshed!")

@Client.on_message(
    filters.command("help")
    & filters.group
    & ~ filters.edited
)
async def helper(client , message:Message):
     await message.reply_text("The commands and there use is explained here-: \n `/saavn` To search song on jio saavan and play the first result \n `/deezer` To search the song on deezer and get good quality stream \n `/ytt` To search the song on Youtube and play the first matching result \n '/play` Reply this in response to a link or any telegram audio file it will be played \n `/skip` to skip current song \n `/stop or /kill` to stop the streaming of song \n `/pause` to pause the stream \n `/resume` to resume the playback. \n Inline search is also supported.")
