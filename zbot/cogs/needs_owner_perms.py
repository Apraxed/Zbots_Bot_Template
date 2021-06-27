# WARNING!!!! IF MISUSED THESE COMMANDS CAN BREAK DISCORDS TOS, DO NOT MISUSE THESE COMMANDS
# THESE ARE MENT AS LAST RESORTS IN CASE PEOPLE ARE FLOODING CHANNELS FASTER THEN YOU CAN DELETE THEM
# LAST RESORT!!!!!!!!

from discord.ext import commands
from asycnio.tasks import sleep
from config import config

client = commands.Bot(command_prefix='')

async def deletechannels(ctx, password):
    if password == config.NukePass:
        await ctx.message.delete()
        for channel in list(ctx.message.guild.channels):
            try:
                await channel.delete()
                print (channel.name + " has been deleted")
            except:
                pass
        await sleep(100)
        channel =ctx.message.guild.create_text_channel('Nuked')
        await channel.send('Server Nuked')

    else:
        await ctx.send('Password incorrect')  
    print(f'Complete, ask {ctx.author}')

async def deleteemojis(ctx, password):
    if password == config.deleteemoji:
        await ctx.message.delete()
        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f'{emoji.name} has been yeeted')
            except:
                pass
        print(f'All emojis have been deleted, ask {ctx.author}')
    
    else:
        await ctx.send('Command not found or password incorrect')

from ... import ownership
async def devs(head, Dev1, Dev2):
    Head = ownership.devs.Zbot
    Dev1 = ownership.devs.Carnoval
    Dev2 = ownership.devs.aviation8816