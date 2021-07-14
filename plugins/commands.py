import os
import time
import psutil
import traceback
import shutil
import string
import asyncio
import info
import logging
from pyromod import listen
from pyrogram import Client, filters
from asyncio import TimeoutError
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from pyrogram import Client, filters
from info import START_MSG, CHANNELS, ADMINS, INVITE_MSG
from helpers.database.access_db import db
from helpers.forcesub import ForceSub
from helpers.broadcast import broadcast_handler
from helpers.database.add_user import AddUserToDatabase
from helpers.humanbytes import humanbytes
from utils import Media

logger = logging.getLogger(__name__)


@Client.on_message(filters.command('start'))
async def start(bot, message):
    await AddUserToDatabase(bot, message)
    FSub = await ForceSub(bot, message)
    if FSub == 400:
        return
    """Start command handler"""
    if len(message.command) > 1 and message.command[1] == 'subscribe':
        user = message.from_user
        await message.reply(INVITE_MSG.format(username=message.from_user.username))
    else:
        buttons = [
            [
                InlineKeyboardButton('Updates Channel 🗣', url='https://t.me/new_ehi'),
                InlineKeyboardButton('Go Inline 🎭', switch_inline_query=''),
            ],
            [
                InlineKeyboardButton('Search Media 🔎', switch_inline_query_current_chat=''),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        user = message.from_user
        await message.reply(START_MSG.format(username=user.username, first_name=user.first_name, last_name=user.last_name), reply_markup=reply_markup)


@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
    await AddUserToDatabase(bot, message)
    FSub = await ForceSub(bot, message)
    if FSub == 400:
        return
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('total') & filters.user(ADMINS))
async def total(bot, message):
    await AddUserToDatabase(bot, message)
    FSub = await ForceSub(bot, message)
    if FSub == 400:
        return
    """Show total files in database"""
    msg = await message.reply("Processing...⏳\nLeo Projects 🇱🇰", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 Total files saved in Leo Media Search Bots Database: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')


@Client.on_message(filters.command('logger') & filters.user(ADMINS))
async def log_file(bot, message):
    await AddUserToDatabase(bot, message)
    FSub = await ForceSub(bot, message)
    if FSub == 400:
        return
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))


@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    await AddUserToDatabase(bot, message)
    FSub = await ForceSub(bot, message)
    if FSub == 400:
        return
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Processing...⏳\nLeo Projects 🇱🇰", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'mime_type': media.mime_type,
        'caption': reply.caption
    })
    if result.deleted_count:
        await msg.edit('File is successfully deleted from database\nLeo Projects🇱🇰')
    else:
        await msg.edit('File not found in database\nLeo Projects🇱🇰')


@Client.on_message(filters.private & filters.command("broadcast") & filters.user(info.BOT_OWNER) & filters.reply)
async def _broadcast(_, bot: Message):
    await broadcast_handler(bot)


@Client.on_message(filters.private & filters.command("stats") & filters.user(info.BOT_OWNER))
async def show_status_count(_, bot: Message):
    total, used, free = shutil.disk_usage(".")
    total = humanbytes(total)
    used = humanbytes(used)
    free = humanbytes(free)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    total_users = await db.total_users_count()
    await bot.reply_text(
        text=f"**Total Disk Space:** {total} \n**Used Space:** {used}({disk_usage}%) \n**Free Space:** {free} \n**CPU Usage:** {cpu_usage}% \n**RAM Usage:** {ram_usage}%\n\n**Total Users in DB:** `{total_users}`\n\n@leoinlinesearchbot 🇱🇰",
        parse_mode="Markdown",
        quote=True
    )
