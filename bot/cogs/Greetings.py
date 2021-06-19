import discord
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bleh(self, ctx):
        await ctx.send('Yuck!')

def setup(bot):
    bot.add_cog(Greetings(bot))