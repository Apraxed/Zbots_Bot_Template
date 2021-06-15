import discord, zbot_library, os
from discord.ext import commands
from config import config
# import dotenv
# from dotenv import loadenv
# from keep_aive import keep_alive # REPLIT ONLY

default_embed_color = config.EMBED_COLOR
# loadenv() # loads the env file

client = commands.Bot(command_prefix=config.PREFIX, pm_help=True, case_insensitive=True, help_command=None)

# keep_alive() # REPLIT ONLY
# TOKEN = os.getenv("TOKEN")
client.run(config.TOKEN, bot=True# or 'TOKEN')

# if you want to hide your token, i featured everything here
# here is the pip lib that you need for .env files https://pypi.org/project/python-dotenv, check `requirements.txt` or in replit it should load automatically 