import discord
import random
from discord.ext import commands

hi_ans = ['Hi!',
 'Hello',
 'Hey, how are ya?',
 'What\'s up?',
 'Howdy!'
]

Eightball_answers = ["Simply yes",
 "It is certain",
 "Definetly yes"
 "Outlook good",
 "You may rely on it",
 "Ask again later",
 "Concentrate and ask again",
 "Reply hazy, try again",
 "My reply is no",
 "My sources say no",
 "Certainly not",
 "Simply no",
 "Certainly maybe"
]

jokes = ['What did the traffic light say to the car? Don’t look! I’m about to change.',
 'Today at the bank, an old lady asked me to help check her balance. So I pushed her over.', 
 'My boss told me to have a good day.. so I went home.',
 'I know a lot of jokes about unemployed people but none of them work.',
 'Bitter bought some butter but the butter was bitter so bitter bought some more butter to make the bitter butter better. Now say that 3 times real fast.',
 'BACTERIA 1: [runs toward pizza that has just been dropped on the floor] BACTERIA 2: [football tackles him to the ground] YOU HAVE TO WAIT FIVE SECONDS SEBASTIAN',
 '1st date: I love the spiderman movies Me: So do I [thinking of something to say to impress her] Me: I used to be a spider',
 'Go to a fancy restaurant. Order the lobster. Order it alive. When it comes, order food for your new pet lobster. Then take lobster home.',
 'Pennies smell nice. The zinc in them give a special smell, a tinge, of sorts'
]

class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['hello', 'wassup', 'whaddup', 'hey', 'yo', 'sup'])
    async def hi(self, ctx):
        '''A command to simulate a return to a greeting
        usage:
        -[One of the command terms]'''
        await ctx.send(random.choice(hi_ans) + ' ðŸ‘‹')

    @commands.command(aliases=['humor', 'funny', 'haha', 'laugh', 'lol'])
    async def joke(self, ctx):
        '''This command sends a jome from a random asosrtment of jokes
        usage is:
        -joke'''
        await ctx.send(random.choice(jokes) + ' ðŸ¤£')

    @commands.command()
    async def ball8(self, ctx):
        '''A command to simulate a fortune 8-ball
        usage:
        -ball8'''
        await ctx.send(random.choice(Eightball_answers) + ' ðŸŽ±')

def setup(bot):
    bot.add_cog(Greetings(bot))