import discord
from discord.ext import commands
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
                
                url = randsub.url

                embed = discord.Embed(title=name)
                embed.set_image(url = url)

                await ctx.send(embed = embed)
        elif number <= 0:
            await ctx.send(f'You sent for {number} reddit posts. That wont work because {number} is less than or equal to zero.')
    
        else:
            await ctx.send(f'You asked for {number} reddit posts. That\'s too much, way over the limit of 35! The reason the limit is at 35 is to avoid spamming, but 35 might be too much in itself')



        

def setup(bot):
    bot.add_cog(Reddit(bot))