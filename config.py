import os

class Config(object):
    
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 12345))
    API_HASH = os.environ.get("API_HASH")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    BANNED_USERS = []

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    TG_MAX_FILE_SIZE = 2097152000

    CHUNK_SIZE = 128

    SCREENSHOTS = os.environ.get("SCREENSHOTS", "True")

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 3600

    DEF_WATER_MARK_FILE = ""

    DB_URI = os.environ.get("DATABASE_URL", "")
