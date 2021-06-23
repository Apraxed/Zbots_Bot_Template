# moderation commands
import discord
from discord import commands
from asyncio.tasks import sleep
import json

client = commands.Bot(command_prefix='', help_command=None)

with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []

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
      guild = ctx.guild.name
      await ctx.send(f"{member}'s ban has expired and they can now rejoin")
      await member.send(f"Your ban in {guild} has expired, rejoin if you want to")
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

async def warn(ctx,user:discord.User.*reason:str):
    if not reason:
        await client.say("Please provide a reason")
        return
    reason = ' '.join(reason)
    for current_user in report['users']:
        if current_user['name'] == user.name:
        current_user['reasons'].append(reason)
        break
    else:
        report['users'].append({
          'name':user.name,
          'reasons': [reason,]
        })
  with open('reports.json','w+') as f:
    json.dump(report,f)