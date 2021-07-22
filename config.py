import os


class Config(object):
BOT_TOKEN = environ('BOT_TOKEN', '1745816793:AAHNHaAVJW_YIyOy5x1K2FTyt9xbZ6DSZaY')
API_HASH = environ('API_HASH', '8c99a2b1329cc263f71da0439cad959f')
API_ID = int(environ('API_ID', 1481861))
SESSION = environ.get('SESSION', 'Testn')
USER_SESSION = environ.get('USER_SESSION', 'User_Bot')
BOT_OWNER = int(os.environ.get("BOT_OWNER", 1069002447))
BOT_USERNAME = os.environ.get("BOT_USERNAME", "testleonvibot")
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ('ADMINS', 1069002447).split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ('CHANNELS', -1001560862542).split()]
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001560862542))
DATABASE_URI = environ('DATABASE_URI', 'mongodb+srv://Naviyaa:navi18572@cluster0.swycj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
DATABASE_NAME = environ('DATABASE_NAME', 'Test')
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", -1001231683570)
MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://Naviyaa:navi18572@cluster0.swycj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SESSION_NAME = os.environ.get("SESSION_NAME", "LeoMediaSearchBot")
