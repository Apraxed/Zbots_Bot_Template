# yes yes main imports
import discord
from discord.ext import commands
import aiohttp
import random
import json
import moderation_commands

client = commands.Bot(command_prefix='', help_command=None)

async def modcmds(ctx, member: discord.Member, reason = None):
  async def tempban():
    moderation_commands.temp_ban10d
  async def pban():
    moderation_commands.permban
  async def kick():
    moderation_commands.kick

async def funcmds()