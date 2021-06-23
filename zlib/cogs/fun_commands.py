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

async def rps(ctx, a):
        a=a.lower()
        RPC=['rock','paper','scissors']
        b= RPC[random.randrange(0,2)]
        if a in RPC:
            if a==b:
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}', color = 0x808080)
                embed.set_footer (text = 'Tie!')
                await ctx.send (embed = embed)
            elif a=='rock' and b=='scissors':
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}', color = 0xFFDF00)
                embed.set_footer (text = 'Win!, 50 tokens added')
                await ctx.send (embed = embed)
            elif a=='scissors' and b=='rock':
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}')
                embed.set_footer (text = 'Loss!')
                await ctx.send (embed = embed)
            elif a=='paper' and b=='rock':
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}', color = 0xFFDF00)
                embed.set_footer (text = 'Win!, 50 tokens added')
                await ctx.send (embed = embed)
            elif a=='rock' and b=="paper":
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}')
                embed.set_footer (text = 'Loss!')
                await ctx.send (embed = embed)
            elif a=='scissors' and b=="paper":
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}', color = 0xFFDF00)
                embed.set_footer (text = 'Win!, 50 tokens added')
                await ctx.send (embed = embed)
            elif a=="paper" and b=="scissors":
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}')
                embed.set_footer (text = 'Loss!')
                await ctx.send (embed = embed)
            else:
                await ctx.send ("That's not a choice")

async def casino(ctx):
    chance = random.randrange(0,101)
    symbols = ['💎', '💰', '💵', '💩', '🎲', '7️⃣']
    if chance == 50:
        for i in range (3):
          e = random.choices(symbols)
          e = e[0]
        embed = discord.Embed(title = f"  You won!",description = f"〘{e}|{e}|{e}", color = 0xFFDF00 )
        await ctx.send(embed=embed)

    else:
        yes = random.randrange(0,4)
        a = random.sample(symbols, 1)
        b = random.sample(symbols, 1)
        a = a[0]
        b = b[0]
        while a == b:
            a = random.sample(symbols, 1)
            a = a[0]
        if yes == 1:
            embed = discord.Embed(title = f"  You lost!", description = f"〘{a}|{b}|{b}〙\n\n{ctx.author.mention}'s roll", color = 0xFF5733)
            await ctx.send(embed=embed)
        elif yes == 2:
            embed = discord.Embed(title = f"  You lost!", description = f"〘{b}|{b}|{a}〙\n\n{ctx.author.mention}'s roll", color = 0xFF5733)
            await ctx.send(embed=embed)
        elif yes == 3:
            embed = discord.Embed(title = f"  You lost!", description = f"〘{b}|{a}|{b}〙\n\n{ctx.author.mention}'s roll", color = 0xFF5733)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title = f"  You lost!", description = f"〘{a}|{b}|{a}〙\n\n{ctx.author.mention}'s roll", color = 0xFF5733)
            await ctx.send(embed=embed)