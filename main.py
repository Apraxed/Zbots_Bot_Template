import discord, zlib, os
from discord.ext import commands
from config import config
from zlib.ext import funcmds, modcmds

# import dotenv
# from dotenv import loadenv
# from keep_aive import keep_alive # REPLIT ONLY

default_embed_color = config.EMBED_COLOR
# loadenv() # loads the env file

client = commands.Bot(command_prefix=config.PREFIX, pm_help=True, case_insensitive=True, help_command=None)

# keep_alive() # REPLIT ONLY
# TOKEN = os.getenv("TOKEN")
client.run(config.TOKEN, bot=True)