import discord
import random
import asyncio
import aiohttp
import os
from discord.ext import tasks,commands
from discord import Game, emoji
from index import jokes, me_sad_ans, ur_bad_ans, no_u_ans, wassup_ans, hi_ans, Eightball_answers
from datetime import datetime

bot = commands.Bot(command_prefix = '-')


@tasks.loop(seconds=1)
async def spm():
    channel = bot.get_channel(CHANNEL1)
    await channel.send("POGGERZ")

@tasks.loop(seconds=1)
async def spm1():
    channel = bot.get_channel(CHANNEL2)
    await channel.send("POGGERZ")

#Show that the bot is ready for usage
@bot.event
async def on_ready():
    await bot.change_presence(activity=Game(name="-help"))
    print('Starting bot code')
    print('Bot prepared for use')
    print('We have logged in as {0.user}'.format(bot))
    print('Running bot...')

#Find bot connection ping and send in the chat
@bot.command() 
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}' + 'ms')

#Test aiohttp usage to get memes from the popula social media site Reddit.
@bot.command()
async def meme(ctx):
    embed = discord.Embed(title="Post from r/memes.", description='Random meme from reddit', color=0xff0000)
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed, content=None)

@bot.command()
async def no_u(ctx):
    await ctx.send(random.choice(no_u_ans))

@bot.command()
async def joke(ctx):
    await ctx.send(random.choice(jokes))

@bot.command()
async def dice(ctx):
    await ctx.send(f'Your dice number is: {random.randint(1, 6)}')

@bot.command()
async def ball8(ctx):
    await ctx.send(random.choice(Eightball_answers))

@bot.command()
async def hi(ctx):
    await ctx.send(random.choice(hi_ans))

@bot.command()
async def ur_bad(ctx):
    await ctx.send(random.choice(ur_bad_ans))

@bot.command()
async def wassup(ctx):
    await ctx.send(random.choice(wassup_ans))

@bot.command()
async def date_time(ctx):
    now = datetime.now()
    await ctx.send(f'This is the time in PST. Please transpose as required \n The year is: {now.year} \n The month is: {now.month} \n The day is: {now.day} \n The hour is: {now.hour} \n The minute is: {now.minute} \n The second is: {now.second} \n The microsecond is: {now.microsecond}')

@bot.command()
async def date(ctx):
    now = datetime.now()
    await ctx.send(f'The date is in PST: It is the year {now.year}, the month of the year is the {now.month}th month, and it is the {now.day}th day of said month. \n In other words, {now.month}-{now.day}-{now.year}.')

@bot.command()
async def time(ctx):
    now = datetime.now()
    await ctx.send(f'The date is in PST: It is the {now.hour}th hour of the day, the minutes are at {now.minute} for the hour, and the seconds are at {now.second}, while the miscroseconds are at {now.microsecond} \n In other words, the time is- {now.hour} : {now.minute} .{now.second} - ms:{now.microsecond}')


@bot.command()
async def wholesome(ctx):
    yo = discord.Embed(title='Wholesome', description='Just a wholesome gif.', color=0xF08080)
    yo.set_author(name='POG bot', url='https://absozero.github.io/POG-bot/', icon_url='https://cdn.discordapp.com/attachments/793648359231586327/833616210603016233/unknown.png')
    yo.set_image(url='https://media.giphy.com/media/dsKiou8r9h2cjMuhr3/giphy-downsized-large.gif')
    yo.set_footer(text='Hope you liked the wholesomeness!')
    await ctx.send(embed=yo)

@bot.command()
async def me_sad(ctx):
    await ctx.send(random.choice(me_sad_ans))


@bot.command()
async def bruh(ctx):
    embed0 = discord.Embed(title='Uhh, what?', description='What did you say, \'bruh\'?', color=0xF08080)
    embed0.add_field(name='PUNISHMENT', value='You say bruh. I say Noooooooooooooooooooo youuuuuuuuuuuuuuuuuuuuuu!', inline=False)
    embed0.set_thumbnail(url='https://i.kym-cdn.com/photos/images/original/001/507/393/910.jpg')
    embed0.set_image(url='https://media1.tenor.com/images/a59a51288bbc1cda522d5aec1978f12f/tenor.gif')
    embed0.set_footer(text='Remember to never mess with the pog bot', icon_url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.eyw7aUKJ6AtkrElG4Nl-rAHaDt%26pid%3DApi&f=1')
    embed0.set_author(name='POG bot', url='https://absozero.github.io/POG-bot/', icon_url='https://cdn.discordapp.com/attachments/793648359231586327/833616210603016233/unknown.png')

    await ctx.send(embed=embed0)

#An embed made to 'roast' the user who has entered the command 
@bot.command()
async def roast(ctx):
    myEmbed = discord.Embed(title='One day, I woke up', description='Then I saw you, and decided to go into eternal sleep right after.', color=0x00ff00)
    myEmbed.add_field(name='Haha, u just got roasted!', value='Ooooooooooooooooooooooooooooooohhhhhhhhhhhhhhhhhhhhhhhhhhhhh', inline=False)
    myEmbed.set_thumbnail(url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.1GdJUzMmarQqNeKjEVvdwQHaDt%26pid%3DApi&f=1')
    myEmbed.set_image(url='https://media2.giphy.com/media/cn9YaZ1gPc74vVJHWq/giphy.gif')
    myEmbed.add_field(name='U lost against me!', value='Bwahahaha', inline=False)
    myEmbed.set_footer(text='U will never beat the pog bot!', icon_url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.eyw7aUKJ6AtkrElG4Nl-rAHaDt%26pid%3DApi&f=1')
    myEmbed.set_author(name='POG bot', url='https://absozero.github.io/POG-bot/', icon_url='https://cdn.discordapp.com/attachments/793648359231586327/833616210603016233/unknown.png')

    await ctx.send(embed=myEmbed)

@bot.command()
async def boring(ctx):
    ctx.send('You are boring. It\'s a fact!')

@bot.command()
async def startspam(ctx):
    ermbed = discord.Embed(title='Spam Menu', description='Write \'-startspm1\' to start spam in one channel, change the number upwards until the spam doesn\'t work to choose between what servers to spam in.(Ex: -startspm(number), -startspm2...) and \'-startspmall\' for spam in as many channels as I can. \'-stopspam\' to stop the spamming.', color=0xF08080)
    ermbed.set_author(name='POG bot', url='https://absozero.github.io/POG-bot/', icon_url='https://cdn.discordapp.com/attachments/793648359231586327/833616210603016233/unknown.png')
        
    await ctx.send(embed=ermbed)

@bot.command()
async def startspm1(ctx):
    spm.start()

@bot.command()
async def startspm2(ctx):
    spm1.start()

@bot.command()
async def startspmall(ctx):
    await ctx.send('I will now start spamming in as many channels as I can. Enter \'-stopspam\' to stop.')
    spm.start()
    spm1.start()

#Command to stop ALL of the spam commands. 
#Will work regardless of how many 'spams' are going on, provided that they are included in the command
@bot.command()
async def stopspam(ctx):
    await ctx.send('Ending spams')
    spm.stop()
    spm1.stop()


#Token area: You replace 'Token goes here' with the token you got from
bot.run('Token goes here')

    