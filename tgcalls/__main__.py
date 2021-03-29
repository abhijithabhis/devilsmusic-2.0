from pyrogram import filters
from .tgcalls import client
from . import group_call_instances
import sira


@client.on_message(filters.me & filters.command("start"))
async def pl(__, _):
    if _.chat.id in group_call_instances.GroupsOn:
        sira.add(_.chat.id, 'out.raw')
    else:
        await group_call_instances.setsong(_.chat.id, 'out.raw')


@client.on_message(filters.me & filters.command("stop"))
async def pl(__, _):
    await group_call_instances.gooff(_.chat.id)

client.run()
