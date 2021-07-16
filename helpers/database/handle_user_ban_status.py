# © Naviya2

import info
from helpers.database.access_db import db
from pyrogram import Client
from pyrogram.types import Message


async def HandleUserBanStatus(bot: Client, cmd: Message):
chat_id = cmd.from_user.id
ban_status = await db.get_ban_status(chat_id)
    if ban_status["is_banned"]:
        if (
                datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])
        ).days > ban_status["ban_duration"]:
            await db.remove_ban(chat_id)
        else:
            await cmd.reply_text("You are Banned to Use This Bot 🥺", quote=True)
            return
    await cmd.continue_propagation()
