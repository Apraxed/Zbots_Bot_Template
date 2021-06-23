import zlib
from discord.ext import commands
from config import config
import json

with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

# import dotenv
# from dotenv import loadenv
# from keep_aive import keep_alive # REPLIT ONLY
cfg = config
default_embed_color = cfg.ecolor
# loadenv() # loads the env file

client = commands.Bot(command_prefix=cfg.prefix, pm_help=True, case_insensitive=True, help_command=None)
zbot = zlib
# EXAMPLE BOT (you can use it idc)
@client.event
async def on_ready():
    print(client.user_name, 'is online')
    print('made by', zbot.devs.head_dev, 'and', zbot.devs.Carnoval)

@client.command()
async def pban():
    zbot.modcmds.pban

@client.command()
async def kick():
    zbot.modcmds.kick

@client.command()
async def rng():
    zbot.funcmds.randomnumgen

@client.command()
async def tempban10d():
    zbot.modcmds.tempban10d

@client.command(pass_context = True)
async def warn():
    zbot.modcmds.warn

@client.event()
async def oon_message():
    zbot.modcmds.userreports

# keep_alive() # REPLIT ONLY
# TOKEN = os.getenv("TOKEN")
client.run(cfg.TOKEN) # If you are using a .env or environ secret, change `cfg.TOKEN` to `cfg.TOKEN_ENV` and the environ secret needs to be `TOKEN`