import discord
import random
from discord.ext import commands

hi_ans = ['Hi!',
 'Hello',
 'Hey, how are ya?',
 'What\'s up?',
 'Howdy!'
]

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('hi!')

    @commands.command(aliases=['hello', 'wassup', 'whaddup', 'hey', 'yo', 'sup'])
    async def hi(self, ctx):
        '''A command to simulate a return to a greeting
        usage:
        -[One of the command terms]'''
        await ctx.send(random.choice(hi_ans) + ' ðŸ‘‹')

def setup(bot):
    bot.add_cog(Greetings(bot))