import os
import re
from os import environ
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', '')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
APP_ID = int(environ['APP_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')
BOT_OWNER = int(os.environ.get("BOT_OWNER", 1069002447))
BOT_USERNAME = os.environ.get("BOT_USERNAME")

# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 10))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#for broadcast and force sub
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", ""))
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)

#ban/unban
BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))

#for broadcast and user stts db
MONGODB_URI = os.environ.get("MONGODB_URI", "")
SESSION_NAME = os.environ.get("SESSION_NAME", "LeoMediaSearchBot")

# Messages
default_start_massege = """
**Hi {}👋

I'm Leo Media Search Bot**

You can start searching by the "Search Media 🔎" button below 😊
"""

default_share_button_text = """
Leo Mod Apps Search Bot 🇱🇰

Here you can find any mod app by searching its name 😊

Bot : {username} 🤖
Support Group : @leosupportx 🇱🇰
Updates Channel: @new_ehi 🇱🇰
Developper : @naviya2 🇱🇰
"""

START_MSG = environ.get('START_MSG', default_start_massege)

SHARE_BUTTON_TEXT = environ.get('SHARE_BUTTON_TEXT', default_share_button_text)

INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')

HELP_TEXT = """
Hello {}👋

<b>You should know following instructions get mod apps😊</b>

🔰<code>At first, Please touch on the bellow "Search Mod Apps 🔎" button</code>

🔰<code>Then type mod app which you want in the type bar</code>

🔰<code>Then our bot will show all the result of your search</code>

🔰<code>Then touch on the result mod app you want</code>
"""
ABOUT_TEXT = """
    
🔰 **Bot :** [Leo Mod Apps Bot 🇱🇰](https://t.me/leoinlinesearchbot)
🔰 **Developer :** [Naviya 🇱🇰](https://telegram.me/naviya2)
🔰 **Updates Channel :** [Leo Updates 🇱🇰](https://telegram.me/new_ehi)
🔰 **Support Group :** [Leo Support 🇱🇰](https://telegram.me/leosupportx)
🔰 **Language :** [Python3](https://python.org)
🔰 **Library :** [Pyrogram](https://pyrogram.org)
🔰 **Server :** [Heroku](https://heroku.com)
"""

HOME_BUTTONS = InlineKeyboardMarkup(
       [
            [
                InlineKeyboardButton('Updates Channel 🗣', url='https://t.me/new_ehi'),
                InlineKeyboardButton('Go Inline 🎭', switch_inline_query=''),
            ],
            [
                InlineKeyboardButton('Help Menu 🆘', callback_data='help'),
            ],
            [
                InlineKeyboardButton('Search Mod Apps 🔎', switch_inline_query_current_chat=''),
            ],
        ]
    )

HELP_BUTTONS = InlineKeyboardMarkup(
       [
            [
                InlineKeyboardButton('About ❗️', callback_data='about'),
                InlineKeyboardButton('Home 🏠', callback_data='home'),
            ],
            [
                InlineKeyboardButton('Search Mod Apps 🔎', switch_inline_query_current_chat=''),
            ],
        ]
    )         

ABOUT_BUTTONS = InlineKeyboardMarkup(
       [
            [
                InlineKeyboardButton('Home 🏠', callback_data='home'),
                InlineKeyboardButton('Help Menu 🆘', callback_data='help'),
            ],
            [
                InlineKeyboardButton('Close ❎', callback_data='close'),
            ],
        ]
    )
