import discord
from discord.ext import commands
import aiohttp
import random
import asyncpraw
import json

with open("info.json") as file:
    info = json.load(file)

reddit = asyncpraw.Reddit(client_id = info["reddit_client"],
client_secret = info["reddit_secret"],
username = info["reddit_username"],
password = info["reddit_password"],
user_agent = info["reddit_useragent"])

class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reddit(self, ctx, subred: str, number: int):
        if 1 <= number <= 35:
            x = range(number)
            for i in x:
                subreddit = await reddit.subreddit(subred)
                all = []

                hot = subreddit.hot(limit = 13)

                async for submission in hot:
                    all.append(submission)

                randsub = random.choice(all)

                name = randsub.title

                x = ('ups: {}, downs: {}'.format(randsub.ups, randsub.downs))
                
                print(dir(randsub))               
                url = randsub.url
                ups = randsub.ups
                sub = randsub.subreddit
                auth = randsub.author

                embed = discord.Embed(title=name)
                embed.set_thumbnail(url=url)
                embed.set_image(url = url)

                embed.add_field(name='reddit', value=url)
                embed.add_field(name='Subreddit', value=sub)

                embed.set_footer(text=auth)

                await ctx.send(embed = embed)
        elif number <= 0:
            await ctx.send(f'You sent for {number} reddit posts. That wont work because {number} is less than or equal to zero.')
    
        else:
            await ctx.send(f'You asked for {number} reddit posts. That\'s too much, way over the limit of 35! The reason the limit is at 35 is to avoid spamming, but 35 might be too much in itself')

    @commands.command()
    async def redit(self, ctx, sub: str, num: int):
        ''' Send pictures from a reddit subreddit 
        usage: limit is 35 to avoid spamming.
        -reddit [subreddit name] [number of photos] '''
        if 1 <= num <= 35:
            x = range(num)
            for i in x:
                embed = discord.Embed(title=f"A Post from r/{sub}.", description=f'Random picture from r/{sub}', color=0xff0000)
                async with aiohttp.ClientSession() as cs:
                    async with cs.get(f'https://www.reddit.com/r/{sub}/new.json?sort=hot') as r:
                        res = await r.json()
                        embed.set_image(url=res['data']['children'] [random.randint(0, 15)]['data']['url'])
                        await ctx.send(embed=embed, content=None)
        elif num <= 0:
            await ctx.send(f'You sent for {num} reddit posts. That wont work because {num} is less than or equal to zero.')
        
        else:
            await ctx.send(f'You asked for {num} reddit posts. That\'s too much, way over the limit of 35! The reason the limit is at 35 is to avoid spamming, but 35 might be too much in itself')
        

def setup(bot):
    bot.add_cog(Reddit(bot))