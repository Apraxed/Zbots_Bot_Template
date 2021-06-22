# moderation commands
import discord
from discord import commands
from asyncio.tasks import sleep

client = commands.Bot(command_prefix='', help_command=None)

# this is a long command
async def temp_ban10d(ctx, member: discord.Member, reason = None):
      if reason == None:
        reason = 'Breaking the rules'
      length = '10 days'
      author = ctx.author
      authorid = ctx.author.id
      await member.send(f'You have been banned from {ctx.guild.name} for {reason} by {author} for {length}, this is a unnapealable ban')
      await ctx.guild.ban(member, reason = reason)
      await ctx.channel.send(f'{member} has been banned for {reason} by <@{authorid}> for {length}')
      await sleep(14400)
      await ctx.guild.unban(member)
      await ctx.send(f"{member}'s ban has expired and they can now rejoin")
      await member.send("Your ban in blueyedevil07's discord server has expired, rejoin if you want to")
      await member.send('https://discord.gg/xuq48V8YRc')

async def permban(ctx, member: discord.Member, reason = None):
      if reason == None:
           reason = 'Breaking the rules'
      author = ctx.author
      authorid = ctx.author.id
      await member.send(f'You have been banned from {ctx.guild.name} for {reason} by {author}, this is a unnapealable, permenent ban')
      await ctx.guild.ban(member, reason = reason)
      await ctx.channel.send(f'{member} has been permbanned for {reason} by <@{authorid}> ')

async def kick():
  @client.command()
  @commands.has_permissions(kick_members=True)
  async def kick(ctx, member: discord.Member, reason = None):
    if reason == None:
      reason = 'Breaking the rules'
    author = ctx.author
    authorid = ctx.author.id
    invitelink = await ctx.channel.create_invite(max_uses=1,unique=True)
    server = ctx.guild
    await member.send(f'{author} has kicked you from {server} for {reason}. rejoin with this link {invitelink}')
    await ctx.send(f'Kicked {member} for you <@{authorid}>, they have recived another invite link but they have hopefully learned')
    await ctx.guild.kick(member, reason = reason)

