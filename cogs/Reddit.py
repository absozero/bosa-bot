import discord
from discord.ext import commands
import praw
import json

with open("info.json") as file:
    info = json.load(file)

class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def rdit(self, ctx):
        await ctx.send(info["reddit_username"])

def setup(bot):
    bot.add_cog(Reddit(bot))