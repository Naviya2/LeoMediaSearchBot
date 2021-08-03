import os
import re
from os import environ
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
APP_ID = int(environ.get('APP_ID', 1481861))
API_HASH = environ.get('API_HASH', '8c99a2b1329cc263f71da0439cad959f')
BOT_TOKEN = environ.get('BOT_TOKEN', '1844693567:AAEXgRNBBMcd_QapU6ZBGR_mAD5-OAutzZI')
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION', 'LeoMediaSearchBotUser')
BOT_OWNER = int(os.environ.get("BOT_OWNER", 1069002447))
BOT_USERNAME = os.environ.get("BOT_USERNAME", "leoinlinesearchbot")
AUTH_USERS = int(environ.get('AUTH_USERS')


# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 10))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', "False"))

# Admins, Channels & Users
ADMINS = int(environ.get('ADMINS', 1069002447))
CHANNELS = int(environ.get('CHANNELS', -1001578165465))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL",  -1001560862542))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', 'mongodb+srv://Erichdaniken:Erichdaniken@cluster0.mqvzd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
DATABASE_NAME = environ.get('DATABASE_NAME', 'Naviyaofficial')
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#for broadcast and force sub
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
UPDATES_CHANNEL = environ.get("UPDATES_CHANNEL", -1001231683570)

#ban/unban
BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))


#for broadcast and user stts db
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://Naviyaa:navi18572@cluster0.swycj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SESSION_NAME = os.environ.get("SESSION_NAME", "LeoMediaSearchBot")

# Messages
default_start_massege = """
**Hi {}👋

I'm Leo Mod Apps Bot**

You can start searching mod apps by the "Search Mod Apps 🔎" button below 😊
"""

SHARE_BUTTON_TEXT = """
Leo Mod Apps Bot 🇱🇰

Here you can find any mod app by searching its name 😊

Bot : {username} 🤖
Support Group : @leosupportx 🇱🇰
Updates Channel: @new_ehi 🇱🇰
Developper : @naviya2 🇱🇰
"""

START_MSG = environ.get('START_MSG', default_start_massege)

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
