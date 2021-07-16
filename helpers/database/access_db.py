import info
from helpers.database.database import Database

db = Database(info.MONGODB_URI, info.SESSION_NAME)
