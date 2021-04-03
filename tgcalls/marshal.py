from typing import Dict
from pytgcalls import GroupCall
import sira
from . import client

GroupsPl: Dict[int, GroupCall] = {}
GroupsOn: Dict[int, Dict[str, bool]] = {}
async def setsong(chat_id: int, file: str):
    if chat_id not in GroupsOn:
        await boost(chat_id)
    getcl(chat_id).input_filename = file


def pause(chat_id: int) -> bool:
    if chat_id not in GroupsOn:
        return False
    elif not GroupsOn[chat_id]["playing"]:
        return False

    getcl(chat_id).pause_playout()
    GroupsOn[chat_id]["playing"] = False
    return True


def resume(chat_id: int) -> bool:
    if chat_id not in GroupsOn:
        return False
    elif GroupsOn[chat_id]["playing"]:
        return False

    getcl(chat_id).resume_playout()
    GroupsOn[chat_id]["playing"] = True
    return True


def mute(chat_id: int) -> int:
    if chat_id not in GroupsOn:
        return 2
    elif GroupsOn[chat_id]["muted"]:
        return 1

    getcl(chat_id).set_is_mute(True)
    GroupsOn[chat_id]["muted"] = True
    return 0


def unmute(chat_id: int) -> int:
    if chat_id not in GroupsOn:
        return 2
    elif not GroupsOn[chat_id]["muted"]:
        return 1

    getcl(chat_id).set_is_mute(False)
    GroupsOn[chat_id]["muted"] = False
    return 0


def intgcall(chat_id: int):
    if chat_id not in GroupsPl:
       GroupsPl[chat_id] = GroupCall(client)

    GroupsP = GroupsPl[chat_id]

    @GroupsP.on_playout_ended
    async def ___(__, _):
        Sira.task_done(chat_id)

        if sira.is_empty(chat_id):
            await stop(chat_id)
        else:
            GroupsP.input_filename = sira.get(chat_id)["file"]


def getcl(chat_id: int) -> GroupCall:
    intgcall(chat_id)
    return GroupsPl[chat_id]


async def boost(chat_id: int):
    await getcl(chat_id).start(chat_id)
    GroupsOn[chat_id] = {"playing": True, "muted": False}


async def gooff(chat_id: int):
    await getcl(chat_id).stop()

    if chat_id in GroupsOn:
        del GroupsOn[chat_id]


