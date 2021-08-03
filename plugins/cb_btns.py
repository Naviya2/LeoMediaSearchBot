import os
import info
from pyrogram import Client
from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_callback_query()
async def cb_data(bot, message):
    if message.data == "home":
        await message.message.edit_text(
            text=info.START_MSG.format(message.from_user.mention),
            reply_markup=info.HOME_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "help":
        await message.message.edit_text(
            text=info.HELP_TEXT.format(message.from_user.mention),
            reply_markup=info.HELP_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "about":
        await message.message.edit_text(
            text=info.ABOUT_TEXT,
            reply_markup=info.ABOUT_BUTTONS,
            disable_web_page_preview=True
        )
    elif message.data == "refreshme":
        if info.UPDATES_CHANNEL:
            invite_link = await bot.create_chat_invite_link(int(info.UPDATES_CHANNEL))
            try:
                user = await bot.get_chat_member(int(info.UPDATES_CHANNEL), message.message.chat.id)
                if user.status == "kicked":
                    await message.message.edit(
                        text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/leosupportx).",
                        parse_mode="markdown",
                        disable_web_page_preview=True
                    )
                    return
            except UserNotParticipant:
                await message.message.edit(
                    text="<b>Hey</b> {},\n\n<b>You still didn't join our Updates Channel ☹️ \nPlease Join and hit on the 'Refresh 🔄' Button</b>".format(message.from_user.mention),
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("Join Our Updates Channel 🗣", url=invite_link.invite_link)
                            ],
                            [
                                InlineKeyboardButton("Refresh 🔄", callback_data="refreshme")
                            ],
                        ]
                    ),
                    parse_mode="HTML"
                )
                return
            except Exception:
                await message.message.edit(
                    text="Something went Wrong. Contact my [Support Group](https://t.me/leosupportx).",
                    parse_mode="markdown",
                    disable_web_page_preview=True
                )
                return
        await message.message.edit(
            text=info.START_MSG.format(message.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=info.HOME_BUTTONS,
        )
    else:
        await message.message.delete()
