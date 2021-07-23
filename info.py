import os
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'LeoMediaSearchBot')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
APP_ID = int(environ['API_ID'])
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
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#for broadcast and force sub
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", ""))
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)


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
Leo Media Search Bot 🇱🇰

Here you can find any media file by searching its name 😊

Bot : {username} 🤖
Support Group : @leosupportx 🇱🇰
Updates Channel: @new_ehi 🇱🇰
Developper : @naviya2 🇱🇰
"""

START_MSG = environ.get('START_MSG', default_start_massege)

SHARE_BUTTON_TEXT = environ.get('SHARE_BUTTON_TEXT', default_share_button_text)

INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')
