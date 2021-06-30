import discord
from config import config

client = discord.Client

async def playing():
    await client.change_presence(activity=discord.Game(name=config.status))

async def streaming():
    await client.change_presence(activity=discord.Streaming(name=config.status, url=config.twitch_url))

async def listening():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=config.status))

async def watching():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=config.status))