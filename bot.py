#Import statements

import discord
import random
import asyncio
import os
import aiohttp
import json
import re
import urllib
from urllib import parse, request

from discord.ext import tasks,commands
from discord import Game, emoji
from datetime import datetime


#The following to-do list will be either the same or a bit more updated than the list in the wiki of the repo.

#-----------Start list-----------------------------
# Move everything to seperate cogs
# Add economy commands
# Add help menu descriptions for all of the commands
# Add aliases to commands
# Add and find cool new commands to add
# Find other stuff to put on the to do list
#-----------End List-------------------------------


if not os.path.isfile("info.json"):
    print("A info.json was not made. Make it and fill it with the correct parameters, please.")
else:
    with open("info.json") as file:
        info = json.load(file)

bot = commands.Bot(command_prefix = '-')
bot.sniped_messages = {}

@bot.event
async def on_ready():
    await bot.change_presence(activity=Game(name="-help : Don't DM me I only work right in servers, not in DM's."))
    now = datetime.now()
    print('We have logged in as {0.user}'.format(bot))
    print(f'Bot has been activated at {now.month}-{now.day}-{now.year} {now.hour}:{now.minute}:{now.second}.{now.microsecond}')
    print('''
██████╗░░█████╗░░██████╗░█████╗░  ██████╗░░█████╗░████████╗
██╔══██╗██╔══██╗██╔════╝██╔══██╗  ██╔══██╗██╔══██╗╚══██╔══╝
██████╦╝██║░░██║╚█████╗░███████║  ██████╦╝██║░░██║░░░██║░░░
██╔══██╗██║░░██║░╚═══██╗██╔══██║  ██╔══██╗██║░░██║░░░██║░░░
██████╦╝╚█████╔╝██████╔╝██║░░██║  ██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░░╚════╝░╚═════╝░╚═╝░░╚═╝  ╚═════╝░░╚════╝░░░░╚═╝░░░''')

if os.path.exists("cogs"):
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')
else:
    print('There is no "cogs" folder found, make sure you have it! The bot will run without the cogs')

@bot.event
async def on_message_delete(message):
    bot.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

#delete user-inputted number of texts before the command is given
@bot.command()
async def delete(ctx, *, texts: int):

    '''A command to delete a number of texts specified by user. The limit is 500 deleted.
    The usage would be: 
    -delete [any whole number]'''
    if 1 <= texts <= 500:
        await ctx.channel.purge(limit=texts + 1)
        await ctx.send(f'{texts} texts were deleted. â›”'.format(texts), delete_after = 3)

    else:
        await ctx.send(f'You sent for {texts} messages to be deleted. That is over the limit of 500 texts deleted. The limit is set there because more than that would take a long time to process and would be laggy.')


@bot.command()
async def snipe(ctx):
    '''Snipes the last message deleted while the bot is active and in a channel the bot can access
    usage
    -snipe'''
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
async def dice(ctx):
    '''A command to simulate the roll of ONE DIE
    usage is:
    -dice'''
    await ctx.send(f'Your dice number is: {random.randint(1, 6)} ðŸŽ²')


@bot.command() 
async def ping(ctx):
    '''Sends the ping of the bot to the user
    usage:
    -ping'''
    await ctx.send(f'{round(bot.latency * 1000)} ms. âŒš')

@bot.command() 
async def code(ctx):
    '''Sends the source code of the bot to the user
    usage:
    -code'''
    await ctx.send(f'https://github.com/absozero/BOSA-bot')  

@bot.command(aliases=['time', 'date', 'second', 'ms', 'year', 'hour', 'date_time', 'week', 'day', 'timepls'])
async def rn(ctx):
    '''Gives the exact time as of when the command was entered.
    usage:
    -[]'''
    now = datetime.now()

    await ctx.send(f'This is the time in PST. Please transpose as required \n The year is: {now.year} \n The month is: {now.month} \n The day is: {now.day} \n The hour is: {now.hour} \n The minute is: {now.minute} \n The second is: {now.second} \n The microsecond is: {now.microsecond} \n â�²ï¸�')
    await ctx.send(f"Also known as '{now.month}-{now.day}-{now.year} {now.hour}:{now.minute}:{now.second}.{now.microsecond}'")

@bot.command(aliases=['user', 'member'])
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
async def channelinfo(ctx):
    """
    Sends data about the current channel the command was run in as long as the bot is in the channel and has the right permissions
    usage:
    -channelinfo
    """
    channel = ctx.channel
    embed = discord.Embed(title=f"Channel stats for #**{channel.name}**", description=f"{'Category: {}'.format(channel.category.name) if channel.category else 'This channel is not in a category'}", color=0xff0000)
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
async def serverinfo(ctx):
    role_count = len(ctx.guild.roles)
    bot_list = [bot.mention for bot in ctx.guild.members if bot.bot]

    embed = discord.Embed(timestamp=ctx.message.created_at, color=ctx.author.color)
    embed.set_thumbnail(url=str(ctx.guild.icon_url))
    embed.add_field(name='Name', value=f"{ctx.guild.name}", inline=True)
    embed.add_field(name='Time of creation', value=f"{ctx.guild.created_at}", inline=True)
    embed.add_field(name='Description', value=f"{ctx.guild.description}", inline=True)
    embed.add_field(name='Region', value=f"{ctx.guild.region}", inline=True)
    embed.add_field(name='ID', value=f"{ctx.guild.id}", inline=False)
    embed.add_field(name='Owner', value=f"{ctx.guild.owner}", inline=True)
    embed.add_field(name='Member Count', value=ctx.guild.member_count, inline=True)
    embed.add_field(name='Verification level', value=str(ctx.guild.verification_level), inline=True)
    embed.add_field(name='Highest Role', value=ctx.guild.roles[-2], inline=True)
    embed.add_field(name='Number of Roles', value=str(role_count), inline=True)
    embed.add_field(name='Bots', value=', '.join(bot_list), inline=True)

    await ctx.send(embed=embed)

@bot.command()
async def reddit(ctx, subreddit: str, number: int):
    ''' Send pictures from a reddit subreddit 
    usage: limit is 35 to avoid spamming.
    -reddit [subreddit name] [number of photos] '''
    if 1 <= number <= 35:
        x = range(number)
        for i in x:
            embed = discord.Embed(title=f"A Post from r/{subreddit}.", description=f'Random picture from r/{subreddit}', color=0xff0000)
            async with aiohttp.ClientSession() as cs:
                async with cs.get(f'https://www.reddit.com/r/{subreddit}/new.json?sort=hot') as r:
                    res = await r.json()
                    embed.set_image(url=res['data']['children'] [random.randint(0, 15)]['data']['url'])
                    await ctx.send(embed=embed, content=None)
    elif number <= 0:
        await ctx.send(f'You sent for {number} reddit posts. That wont work because {number} is less than or equal to zero.')
    
    else:
        await ctx.send(f'You asked for {number} reddit posts. That\'s too much, way over the limit of 35! The reason the limit is at 35 is to avoid spamming, but 35 might be too much in itself')

@bot.command()
async def urbdict(ctx, *, query: str):
    '''Gets a query from the popular urban dictionary'''
    term = query.replace(' ', '_')
    await ctx.send('Here is your search from the urban dictionary')
    await ctx.send(f'https://www.urbandictionary.com/define.php?term={term}')

@bot.command()
async def wiki(ctx, *, search: str):
    term = search.replace(' ', '_')
    await ctx.send('Here is your search from wikipedia')    
    await ctx.send(f'https://en.wikipedia.org/wiki/{term}')


@bot.command(pass_context=True)
async def giphy(ctx, number: int, *, search: str):
    '''Get a gif into the chat from the giphy gif source'''

    if 1 <= number <= 20:
        x = range(number) 
        for gif in x:

            embed = discord.Embed(colour=discord.Color.blue())
            session = aiohttp.ClientSession()

            if search == '':
                response = await session.get('https://api.giphy.com/v1/gifs/random?api_key=Y4hnrG09EqYcNnv63Sj2gJvmy9ilDPx5')
                data = json.loads(await response.text())
                embed.set_image(url=data['data']['images']['original']['url'])
            else:
                search.replace(' ', '+')
                response = await session.get('http://api.giphy.com/v1/gifs/search?q=' + search + '&api_key=Y4hnrG09EqYcNnv63Sj2gJvmy9ilDPx5&limit=10')
                data = json.loads(await response.text())
                gif_choice = random.randint(0, 10)
                embed.set_image(url=data['data'][gif_choice]['images']['original']['url'])

            await session.close()

            await ctx.send(embed=embed)
    
    elif number <= 0:
        await ctx.send(f'You sent for {number} gifs from giphy. That wont work because {number} is less than or equal to zero.')
    
    else:
        await ctx.send(f'You asked for {number} gifs from giphy. That\'s too much, way over the limit of 20! The reason the limit is at 20 is to avoid spamming.')


@bot.command()
async def twitch(ctx, *, search: str):
    '''Allow the bot to send a twitch stream to the user, as long as the stream is 
    mentioning the right account and the stream is active.
    Otherwise, there will not be a stream for that request.
    usage:
    -twitch [streamer username]'''
    term = search.replace(' ', '_')
    await ctx.send('Here is the stream you searched for:')
    await ctx.send(f'https://twitch.tv/{term}')


@bot.command(aliases=['yt'])
async def youtube(ctx, num: int, *, search: str):
    ''' Gets a video from youtube with the search term. 
    The reason the command syntax is so wierd is because it will make the user have to puth their
    search term in quotation marks like:"[Example search term]", which may be annoying and take 
    longer to type. The wierd syntax fixes this and makes it faster and easier with a little practice.
    usage:
    -youtube [any whole number(including 0)] [your search term]'''
    searchy = search.replace(' ', '+')
    html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={searchy}")
    vid_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    await ctx.send(f'This is the {num}th video found when searching for the term \'{search}\'.')
    await ctx.send('https://www.youtube.com/watch?v=' + vid_id[num])



#Token ----> goes right under 
bot.run(info["token"])
    