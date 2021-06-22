# Token(replit users i reccomend using the environ secrets)
TOKEN: str = "INSERT_TOKEN_HERE"

import os
envtoken = os.environ['TOKEN'] # for .env files and environ variable secrets


USER_REPORTS_CHANNEL_NAME = 'modmail' # userreports channel, change this to the name of any channel you have in your server that you want user reports to be delivered in


BOT_PREFIX = "!" # bot prefix

EMBED_COLOR = 0x433bdb  #replace after'0x' with desired hex code ex. '#ff0188' >> '0xff0188'

NoChannelsPassword = 'deleteall' # Password for the owner only command that deletes the channels, change to whatever you want

"""BELOW IS MAKING THE ABOVE CONFIG STUFF UNDERSTANDABLE FOR THE LIBRARY's CODE, DO NOT TOUCH UNLESS YOU KNOW WHAT YOU ARE DOING"""

TOKEN_ENV = envtoken

async def modmail_channel():
    USER_REPORTS_CHANNEL_NAME

async def prefix():
    BOT_PREFIX

async def ecolor():
    EMBED_COLOR

async def nukepass():
    NoChannelsPassword