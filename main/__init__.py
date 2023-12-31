#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "1814890"
API_HASH = "346db519688cd678a2bc5908d3791967"
BOT_TOKEN = "6559784740:AAHnMsnhL2n4OLa_md1UTLj2yZ7hYf1nSBU"
SESSION = "1BVtsOJcBu4Cp_nY0lwWJ_OCAputqf8f1a7LeD1IIwy4jdbCmbMugPU-9lJRlTbGVmFbzc6_Kyp7DTS903U7UQt_DLj3UtBPipBE_EllQJb_3SLMWWhRwbytFF2CoLmdQWmdcfeXoMaIrZNZ4hFqh4lsojxA80GduTAl_H9ks4BofTJk9oWlX6wSJYcEt2x2Kxs7pjp6yvuLUVo3kS6cc0TkAptDh7qHq9uVTVx0JrF1QD5_xislJwxYXIvTAQ8iyvdKgCeMhymPMNHipmHGpMVVepRStdmfzLJQKhBKRwiLgVBrWuk2j1yPdehEc3pv2Rc-KmhrPEUTykGMVju86gU5o6k5UESY="
FORCESUB = "TNTOONBOT"
AUTH = "1171653845"

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
