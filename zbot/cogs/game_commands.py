import discord
from ... import ownership
import random
from config import config
import config2

async def rps(ctx, a):
        a=a.lower()
        RPC=['rock','paper','scissors']
        b= RPC[random.randrange(0,2)]
        if a in RPC:
            if a==b:
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}', color = 0x808080)
                embed.set_footer (text = f'Tie {ownership.Watermark}!')
                await ctx.send (embed = embed)
            elif a=='rock' and b=='scissors':
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}', color = 0xFFDF00)
                await ctx.send (embed = embed)
            elif a=='scissors' and b=='rock':
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}')
                embed.set_footer (text = f'Loss! {ownership.Watermark}')
                await ctx.send (embed = embed)
            elif a=='paper' and b=='rock':
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}', color = 0xFFDF00)
                await ctx.send (embed = embed)
            elif a=='rock' and b=="paper":
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}')
                embed.set_footer (text = f'Loss! {ownership.Watermark}')
                await ctx.send (embed = embed)
            elif a=='scissors' and b=="paper":
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}', color = 0xFFDF00)
                await ctx.send (embed = embed)
            elif a=="paper" and b=="scissors":
                embed = discord.Embed(title = 'RPS results', description = f'{ctx.author.mention}: {a}\nMe: {b}')
                embed.set_footer (text = f'Loss! {ownership.Watermark}')
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
        embed.set_footer(text = {ownership.Watermark})
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
            embed.set_footer(text = {ownership.Watermark})
            await ctx.send(embed=embed)
        elif yes == 2:
            embed = discord.Embed(title = f"  You lost!", description = f"〘{b}|{b}|{a}〙\n\n{ctx.author.mention}'s roll", color = 0xFF5733)
            embed.set_footer(text = {ownership.Watermark})
            await ctx.send(embed=embed)
        elif yes == 3:
            embed = discord.Embed(title = f"  You lost!", description = f"〘{b}|{a}|{b}〙\n\n{ctx.author.mention}'s roll", color = 0xFF5733)
            embed.set_footer(text = {ownership.Watermark})
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title = f"  You lost!", description = f"〘{a}|{b}|{a}〙\n\n{ctx.author.mention}'s roll", color = 0xFF5733)
            embed.set_footer(text = {ownership.Watermark})
            await ctx.send(embed=embed)