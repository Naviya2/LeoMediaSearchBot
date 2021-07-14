# ©Naviya2

import asyncio
import info
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message


async def ForceSub(bot: Client, event: Message):
    """
    Custom Pyrogram Based Telegram Bot's Force Subscribe Function by @Naviya2.
    If User is not Joined Force Sub Channel Bot to Send a Message & ask him to Join First.
    
    :param bot: Pass Client.
    :param event: Pass Message.
    :return: It will return 200 if Successfully Got User in Force Sub Channel and 400 if Found that User Not Participant in Force Sub Channel or User is Kicked from Force Sub Channel it will return 400. Also it returns 200 if Unable to Find Channel.
    """
    
    try:
        invite_link = await bot.create_chat_invite_link(chat_id=(int(info.UPDATES_CHANNEL) if info.UPDATES_CHANNEL.startswith("-100") else info.UPDATES_CHANNEL))
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, event)
        return fix_
    except Exception as err:
        print(f"Unable to do Force Subscribe to {info.UPDATES_CHANNEL}\n\nError: {err}\n\nContact Support Group: https://t.me/leosupportx")
        return 200
    try:
        user = await bot.get_chat_member(chat_id=(int(info.UPDATES_CHANNEL) if info.UPDATES_CHANNEL.startswith("-100") else info.UPDATES_CHANNEL), user_id=event.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=event.from_user.id,
                text="Sorry Dear, You are Banned to use me ☹️\nFeel free to say in our [Support Group](https://t.me/leosupportx).",
                parse_mode="markdown",
                disable_web_page_preview=True,
                reply_to_message_id=event.message_id
            )
            return 400
        else:
            return 200
    except UserNotParticipant:
        await bot.send_message(
            chat_id=event.from_user.id,
            text="**Hey there 👋\n\nYou cant use me untill subscribe our updates channel ☹️\nSo Please join our updates channel by the following button and restart our bot by ( /start ) command 😊**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Join Our Updates Channel 🗣", url=invite_link.invite_link)
                    ]
                ]
            ),
            parse_mode="markdown",
            reply_to_message_id=event.message_id
        )
        return 400
    except FloodWait as e:
        await asyncio.sleep(e.x)
        fix_ = await ForceSub(bot, event)
        return fix_
    except Exception as err:
        print(f"Something Went Wrong! Unable to do Force Subscribe.\nError: {err}\n\nContact Support Group: https://t.me/leosupportx")
        return 200
