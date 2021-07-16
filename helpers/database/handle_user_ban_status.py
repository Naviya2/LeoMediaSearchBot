# © Naviya2

import info
import datetime
from pyromod import listen
from helpers.database.access_db import db
from pyrogram import Client
from pyrogram.types import Message


async def handle_user_ban_status(bot: Client, message: Message):
    ban_status = await db.get_ban_status(message.from_user.id)
    if ban_status["is_banned"]:
        if (
                datetime.date.today() - datetime.date.fromisoformat(ban_status["banned_on"])
        ).days > ban_status["ban_duration"]:
            await db.remove_ban(message.from_user.id)
        else:
            await message.reply_text("You are Banned to Use This Bot 🥺", quote=True)
            return
    await message.continue_propagation()
