#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("1814890", default=None, cast=int)
API_HASH = config("346db519688cd678a2bc5908d3791967", default=None)
BOT_TOKEN = config("6559784740:AAHnMsnhL2n4OLa_md1UTLj2yZ7hYf1nSBU", default=None)
SESSION = config("BQHBmd8AIGksJcgQx2fPuF2IUaHBYPnCtbO8RiX4L6UqZnBYzTd423YOKFa306XCbsOEN7Jy2VprHdJhjSYSWc9gUMRPe7tM0xtD2QL0viAw1xOZAS-KO1rZgrCTx8-pEJPNyGIFgjZNIi-7x72iIMvAVBupr4tgYHd2eJj8lgRiZAXNR55EWY0VXE-yNccb3Xcewbv2_JGz0d7AdJ-lVOnZOWaZUwzLNiudWiVWV7PyosYbwfy8dOZ7Q1f-62Fwc0fOwnf1aGj0xantiJS1Wt1SwxZg8IVYf6TlrcnlBfeOBuBM5u4t6m96dL3ScKE57cKSCbtKhivpiz4w_uU21qU_ySU-3gAAAABF1gTVAA", default=None)
FORCESUB = config("TNTOONBOT", default=None)
AUTH = config("1171653845", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
