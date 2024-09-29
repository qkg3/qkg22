import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

API_ID = int(getenv("API_ID", "23077975"))
API_HASH = getenv("API_HASH", "45407fde510529dc2041ce03b0f36a1d")
BOT_TOKEN = getenv("BOT_TOKEN", "6499198312:AAFMUSlhIdOGBGP01r6JkTe1_NggL_083Ag")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "AgCIVfMARteM6ZNQf3Wv-Ztek72l7LM9sNTV8fGHByX6i8l2WyqRV8_c64zzp6egst1Y2n0F1DEjao9D9AKr8cjFovEWCR5khB9paH3AR1B0UGc-pXw084zceUAQSeXbKsXNtN8uqduRmfJFEAYI6FZ1uQR7fhevTFYUeJAGKFlzAyYhIb0ZZ_QFQ3tB52RyIt_4hb-3n3Y8OjSFLVBHlj3aRSXeaTu9BTpl3dNDlDRlprQhBbb2n5nrlUfOuO22yIRP1dVXhs1w-r6ZBq6dZgKrTaBBH5Pr8yZs9IugpryZHHBPFIfqMYM3Xd1LRLBFx8syRWcj-aQsH5YPYWSlFecvSUBCjQAAAAEv9SzoAA")
BOT_USERNAME = getenv("BOT_USERNAME", "LROBOT")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5099564264").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "5099564264").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002428993908")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "AFTU2")
GROUP = getenv("GROUP", "AFTU2")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


