import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']
USERBOT_STRING_SESSION = environ.get('USERBOT_STRING_SESSION')

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

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
START_MSG = """
**Hi  {first_name}  {last_name} 👋

I'm Leo Media Search Bot 🇱🇰**

Here you can find,
⭕️Musical Shows
⭕️Songs (English,Sinhala)
⭕️Wallpapers(4K)
⭕️Anime Films(English)
⭕️EDM Songs
⭕️Mod Apps

You can start searching by the "Search Here" button below 🙂

Support Group : @leosupportx 🇱🇰
Updates Channel: @new_ehi 🇱🇰
Developper : @naviya2 🇱🇰
"""

SHARE_BUTTON_TEXT = """
Leo Media Search Bot 🇱🇰

Here you can find,
⭕️Musical Shows
⭕️Songs (English,Sinhala)
⭕️Wallpapers(4K)
⭕️Anime Films(English)
⭕️EDM Songs
⭕️Mod Apps

Support Group : @leosupportx 🇱🇰
Updates Channel: @new_ehi 🇱🇰
Developper : @naviya2 🇱🇰
"""
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')
