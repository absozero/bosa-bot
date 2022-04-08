import discord
from discord.ext import commands
import aiohttp
import random
import json


class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


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