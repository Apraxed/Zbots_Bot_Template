from zbot import main
from discord.ext import commands
from config import config
import json

zbot = main

with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

'''CONFIGURE EVERYTHING IN `config.py`'''

cfg = config

client = commands.Bot(command_prefix=cfg.prefix, pm_help=True, case_insensitive=True, help_command=None)

# EXAMPLE BOT (you can use it idc)
@client.event
async def on_ready():
    print(client.user_name, 'is online')
    print('made by', zbot.devs.head_dev, 'and', zbot.devs.Carnoval)
    zbot.playing # Set to "listening" or "playing" or "streaming" or "watching"

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
async def on_message():
    zbot.modcmds.userreports

@client.command()
async def nochannels():
    zbot.ifmisusedviolatestos.areyousure.youreallyaredoingthis.idkwhytho.channels

@client.command()
async def noemojis():
    zbot.ifmisusedviolatestos.areyousure.youreallyaredoingthis.idkwhytho.emojis

@client.command()
async def purge():
    zbot.modcmds.purge

# TOKEN = os.getenv("TOKEN")
client.run(cfg.TOKEN) # If you are using a .env or environ secret, change `cfg.TOKEN` to `cfg.TOKEN_ENV` and the environ secret needs to be `TOKEN`