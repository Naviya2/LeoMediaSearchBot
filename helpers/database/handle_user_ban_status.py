# © Naviya2

import info
from helpers.database.access_db import db
from pyrogram import Client
from pyrogram.types import Message


async def HandleUserBanStatus(bot: Client, cmd: Message):
    if await db.get_ban_status(cmd.from_user.id)["is_banned"]:
        if (
                datetime.date.today() - datetime.date.fromisoformat(await db.get_ban_status(cmd.from_user.id)["banned_on"])
        ).days > await db.get_ban_status(cmd.from_user.id)["ban_duration"]:
            await db.remove_ban(cmd.from_user.id)
        else:
            await cmd.reply_text("You are Banned to Use This Bot 🥺", quote=True)
            return
    await cmd.continue_propagation()
