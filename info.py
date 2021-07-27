import os
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'LeoMediaSearchBot')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
APP_ID = int(environ.get('APP_ID', 1481861))
API_HASH = environ.get('API_HASH', '8c99a2b1329cc263f71da0439cad959f')
BOT_TOKEN = environ.get('BOT_TOKEN', '1745816793:AAHNHaAVJW_YIyOy5x1K2FTyt9xbZ6DSZaY')
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION', 'LeoMediaSearchBotUser')
BOT_OWNER = int(os.environ.get("BOT_OWNER", 1069002447))
BOT_USERNAME = os.environ.get("BOT_USERNAME", "testleonvibot")
AUTH_USERS = int(environ.get('AUTH_USERS', -100))
AUTH_CHANNEL = environ.get('AUTH_CHANNEL')


# Bot settings
MAX_RESULTS = int(environ.get('MAX_RESULTS', 10))
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = int(environ.get('ADMINS', 1069002447))
CHANNELS = int(environ.get('CHANNELS', -1001560862542))
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL",  -1001560862542))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', 'mongodb+srv://Naviyaa:navi18572@cluster0.swycj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
DATABASE_NAME = environ.get('DATABASE_NAME', 'Test')
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#for broadcast and force sub
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
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

I'm Leo Media Search Bot**

You can start searching by the "Search Media 🔎" button below 😊
"""

SHARE_BUTTON_TEXT = """
Leo Media Search Bot 🇱🇰

Here you can find any media file by searching its name 😊

Bot : {username} 🤖
Support Group : @leosupportx 🇱🇰
Updates Channel: @new_ehi 🇱🇰
Developper : @naviya2 🇱🇰
"""

START_MSG = environ.get('START_MSG', default_start_massege)

INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')
