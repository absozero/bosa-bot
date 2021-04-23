import discord
from discord.ext import commands


client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print('Starting server')
    print('Bot prepared for use')
    print('We have logged in as {0.user}'.format(client))
    print('Running bot...')

@client.command()
async def ping(ctx):
    await ctx.send('pong')


client.run('ODI5MjM5OTQyNDk5NTMyODUw.YG1P4A.W8Lp8rqKIUjY4t7zt--RLTiI4aA')
    