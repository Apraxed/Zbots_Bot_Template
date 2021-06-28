import discord 
from discord.ext import commands
from asyncio.tasks import sleep
import aiohttp
import random
from config import config

cfg = config
client = commands.Bot(command_prefix='', help_command=None)



# meme command
async def memecmd():
  @client.command(pass_context=True)
  async def meme(ctx):
    embed = discord.Embed(title="Welcome to r/dankmemes (or r/memes)", description=f"<@{ctx.author.id}>", color = cfg.ecolor)
    rng = random.randit(1, 2)
    async with aiohttp.ClientSession() as cs:
      if rng == 1:
        async with cs.get(f'https://www.reddit.com/r/{cfg.subreddit1}/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
      if rng == 2:
        async with cs.get(f'https://www.reddit.com/r/{cfg.subreddit2}/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

# Random Number Generator
async def rng(ctx):
  rng = random.randit(1, 1000)
  await ctx.send('Generating RNG')
  await sleep(4)
  await ctx.send('Your random number is...')
  await sleep(1)
  await ctx.send(f'{rng}!!!!')
  print(ctx.author)
  print(f'got {rng} from the random number generator')

# pp size command
async def pp_size(ctx):
    embed = discord.Embed(title = f"{ctx.author} your pp size is...", description = (random.randint(1, 500)), color = cfg.ecolor)
    await ctx.send(embed = embed)

async def questions(ctx, *question):
    responses=['No','I think so',' I think not','Yes','Not sure','Try again later','Try harder', 'Nah fam', 'Get richer then try again']
    embed = discord.Embed(title = '8ball results', description = f'Question: {question}\n{random.choice(responses)}, {ctx.author.mention}.', color = cfg.ecolor)
    await ctx.send(embed = embed)

