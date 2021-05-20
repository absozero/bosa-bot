#Import statements

import discord
import random
import asyncio
import os
import aiohttp
import json
import re

from discord.ext import tasks,commands
from discord import Game, emoji
from index import wassup_ans, hi_ans, Eightball_answers
from index import jokes, roastgif, bruhgif, wholesomegif
from datetime import datetime

bot = commands.Bot(command_prefix = '-')
bot.sniped_messages = {}

with open("BOSA-bot/bot/info.json") as f:
    info = json.load(f)

token = info["Token"]


@bot.event
async def on_ready():
    await bot.change_presence(activity=Game(name="-help : Don't DM me I only work right in servers, not in DM's."))
    print('We have logged in as {0.user}'.format(bot))
    print('Bot has been activated') 


@bot.event
async def on_message_delete(message):
    bot.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

@bot.command()
async def snipe(ctx):
    '''Snipes the last message deleted while the bot is active and in a channel the bot can access'''
    try:
        contents, author, channel_name, time = bot.sniped_messages[ctx.guild.id]
        
    except:
        await ctx.channel.send("The bot couldn't find a message to snipe!")
        return

    embed = discord.Embed(description=contents, color=discord.Color.purple(), timestamp=time)
    embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")

    await ctx.channel.send(embed=embed)

@bot.command() 
async def ping(ctx):
    '''Sends the ping of the bot to the user'''
    await ctx.send(f'{round(bot.latency * 1000)}' + 'ms')

#delete user-inputted number of texts before the command is given
@bot.command()
async def delete(ctx, texts: int):
    await ctx.channel.purge(limit=texts)
    await ctx.send(f'{texts} texts were deleted.'.format(texts), delete_after = 3)

@bot.command()
async def reddit(ctx, reddit: str):
    embed = discord.Embed(title="Post from the subreddit of your choice(enter it in as -reddit [subreddit name]).", description='Random post from a subreddit of your choice', color=0xff0000)
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://www.reddit.com/r/{reddit}/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed, content=None)

@bot.command()
async def channelinfo(ctx):
    """
    Sends data about the current channel the command was run in as long as the bot is in the channel and has the right permissions
    """
    channel = ctx.channel
    embed = discord.Embed(title=f"Stat embed for **{channel.name}**", description=f"{'Category: {}'.format(channel.category.name) if channel.category else 'This channel is not in a category'}", color=0xff0000)
    embed.add_field(name="Channel's Guild", value=ctx.guild.name, inline=False)
    embed.add_field(name="Channel Id#", value=channel.id, inline=False)
    embed.add_field(name="Channel's Topic", value=f"{channel.topic if channel.topic else 'No topic.'}", inline=False)
    embed.add_field(name="Channel Position in channels", value=channel.position, inline=True)
    embed.add_field(name="Channel's Slowmode delay", value=channel.slowmode_delay, inline=True)
    embed.add_field(name="Channel is nsfw?", value=channel.is_nsfw(), inline=True)
    embed.add_field(name="Channel is news?", value=channel.is_news(), inline=True)
    embed.add_field(name="Channel's birth", value=channel.created_at, inline=True)
    embed.add_field(name="Channel's Permission sync'", value=channel.permissions_synced, inline=True)
    embed.add_field(name="Channel's Hash'", value=hash(channel), inline=False)

    await ctx.send(embed=embed)

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

#Following commands are for telling time and date
#It starts here
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
#And ends here

@bot.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)
    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    await ctx.send(embed=embed)

@bot.command()
async def serverinfo(ctx):
    role_count = len(ctx.guild.roles)
    bot_list = [bot.mention for bot in ctx.guild.members if bot.bot]

    embed = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
    embed.set_thumbnail(url=str(ctx.guild.icon_url))
    embed.add_field(name='Name', value=f"{ctx.guild.name}", inline=True)
    embed.add_field(name='Description', value=f"{ctx.guild.description}", inline=True)
    embed.add_field(name='Region', value=f"{ctx.guild.region}", inline=True)
    embed.add_field(name='ID', value=f"{ctx.guild.id}", inline=False)
    embed.add_field(name='Owner', value=f"{ctx.guild.owner}", inline=True)
    embed.add_field(name='Member Count', value=ctx.guild.member_count, inline=True)
    embed.add_field(name='Verification level', value=str(ctx.guild.verification_level), inline=False)
    embed.add_field(name='Highest Role', value=ctx.guild.roles[-2], inline=True)
    embed.add_field(name='Number of Roles', value=str(role_count), inline=True)
    embed.add_field(name='Bots', value=', '.join(bot_list), inline=False)

    await ctx.send(embed=embed)

@bot.command()
async def wholesome(ctx):
    yo = discord.Embed(title='Wholesome', description='Just a wholesome gif.', color=0xF08080)
    yo.set_author(name='POG bot', url='https://absozero.github.io/POG-bot/', icon_url='https://cdn.discordapp.com/attachments/793648359231586327/833616210603016233/unknown.png')
    yo.set_image(url=random.choice(wholesomegif))
    yo.set_footer(text='Hope you liked the wholesomeness!')
    await ctx.send(embed=yo)


@bot.command()
async def bruh(ctx):
    embed0 = discord.Embed(title='Uhh, what?', description='What did you say, \'bruh\'? I will kill u with my litten ex yaaaaa!', color=0xF08080)
    embed0.add_field(name='PUNISHMENT', value='You say bruh. I say Noooooooooooooooooooo youuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu!', inline=False)
    embed0.set_thumbnail(url='https://i.kym-cdn.com/photos/images/original/001/507/393/910.jpg')
    embed0.set_image(url=random.choice(bruhgif))
    embed0.set_footer(text='Remember to never mess with the pog bot', icon_url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.eyw7aUKJ6AtkrElG4Nl-rAHaDt%26pid%3DApi&f=1')
    embed0.set_author(name='POG bot', url='https://absozero.github.io/POG-bot/', icon_url='https://cdn.discordapp.com/attachments/793648359231586327/833616210603016233/unknown.png')

    await ctx.send(embed=embed0)

@bot.command()
async def roast(ctx):
    myEmbed = discord.Embed(title='One day, I woke up', description='Then I saw you, and decided to go into eternal sleep right after.', color=0x00ff00)
    myEmbed.add_field(name='Haha, u just got roasted!', value='Ooooooooooooooooooooooooooooooohhhhhhhhhhhhhhhhhhhhhhhhhhhhh', inline=False)
    myEmbed.set_thumbnail(url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.1GdJUzMmarQqNeKjEVvdwQHaDt%26pid%3DApi&f=1')
    myEmbed.set_image(url=random.choice(roastgif))
    myEmbed.add_field(name='U lost against me!', value='Bwahahaha', inline=False)
    myEmbed.set_footer(text='U will never beat the pog bot Mwahahahahahahahahahah', icon_url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.eyw7aUKJ6AtkrElG4Nl-rAHaDt%26pid%3DApi&f=1')
    myEmbed.set_author(name='POG bot', url='https://absozero.github.io/POG-bot/', icon_url='https://cdn.discordapp.com/attachments/793648359231586327/833616210603016233/unknown.png')

    await ctx.send(embed=myEmbed)


#Token ----> goes right under 
bot.run(token)
    