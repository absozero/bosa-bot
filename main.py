import discord
from discord.ext import tasks
from discord.ext import commands
from discord import Game


client = discord.Client()

@tasks.loop(seconds=1)
async def spm():
    channel = client.get_channel(CHANNELID1)
    await channel.send("POGGERZ")

@tasks.loop(seconds=1)
async def spm1():
    channel = client.get_channel(CHANNELID2)
    await channel.send("POGGERZ")

@tasks.loop(seconds=1)
async def spm2():
    channel = client.get_channel(CHANNELID3)
    await channel.send("POGGERZ")

@tasks.loop(seconds=1)
async def spm3():
    channel = client.get_channel(CHANNELID4)
    await channel.send('POGGERZ')

@tasks.loop(seconds=1)
async def spm4():
    channel = client.get_channel(CHANNELID5)
    await channel.send('POGGERZ')

@tasks.loop(minutes=1)
async def clmspm():
    channel1 = client.get_channel(CHANNELID6)
    await channel1.send("POGGERZ")
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('-hello'):
        await message.channel.send('Hi!')

    if message.content.startswith('-help'):
        embud = discord.Embed(title='Help menu', color=0xF08080)
        embud.set_author(name='POG bot', url='https://absozero.github.io/POG-bot/', icon_url='https://cdn.discordapp.com/attachments/793648359231586327/833616210603016233/unknown.png')
        embud.add_field(name='Spam commands', value='-startspam: Spam help menu', inline=True)
        embud.add_field(name='Casual commands', value='-hi for a casual greeting, -wassup for a dope start, and -im sad for a sad response. -bruh and -roast are for some very *special embeds')
        embud.set_footer(text='DM owner to turn on the bot.')

        await message.channel.send(embed=embud)

    if message.content.startswith('-hi'):
        await message.channel.send('Hey, how\'s it going?')

    if message.channel.send('-joke'):
        await message.channel.send('What did u saaayyyyyyyyyyyyyyyy?')

    if message.content.startswith('-wassup'):
        await message.channel.send('Whats up')

    if message.content.startswith('-im sad'):
        await message.channel.send('Too bad')

    if message.content.startswith('-bruh'):
        embed0 = discord.Embed(title='Uhh, what?', description='What did you say, \'bruh\'? I will kill u with my litten ex yaaaaa!', color=0xF08080)
        embed0.add_field(name='PUNISHMENT', value='You say bruh. I say Noooooooooooooooooooo youuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu!', inline=False)
        embed0.set_thumbnail(url='https://i.kym-cdn.com/photos/images/original/001/507/393/910.jpg')
        embed0.set_image(url='https://media1.tenor.com/images/a59a51288bbc1cda522d5aec1978f12f/tenor.gif')
        embed0.set_footer(text='Remember to never mess with the pog bot', icon_url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.eyw7aUKJ6AtkrElG4Nl-rAHaDt%26pid%3DApi&f=1')
        embed0.set_author(name='POG bot', url='https://absozero.github.io/POG-bot/', icon_url='https://cdn.discordapp.com/attachments/793648359231586327/833616210603016233/unknown.png')
        
        await message.channel.send(embed=embed0)
        
    if message.content.startswith('-roast'):
       
        myEmbed = discord.Embed(title='One day, I woke up', description='Then I saw you, and decided to go into eternal sleep right after.', color=0x00ff00)
        myEmbed.add_field(name='Haha, u just got roasted!', value='Ooooooooooooooooooooooooooooooohhhhhhhhhhhhhhhhhhhhhhhhhhhhh', inline=False)
        myEmbed.set_thumbnail(url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.1GdJUzMmarQqNeKjEVvdwQHaDt%26pid%3DApi&f=1')
        myEmbed.set_image(url='https://media2.giphy.com/media/cn9YaZ1gPc74vVJHWq/giphy.gif')
        myEmbed.add_field(name='U lost against me!', value='Bwahahaha', inline=False)
        myEmbed.set_footer(text='U will never beat the pog bot Mwahahahahahahahahahah', icon_url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.eyw7aUKJ6AtkrElG4Nl-rAHaDt%26pid%3DApi&f=1')
        myEmbed.set_author(name='POG bot', url='https://absozero.github.io/POG-bot/', icon_url='https://cdn.discordapp.com/attachments/793648359231586327/833616210603016233/unknown.png')

        await message.channel.send(embed=myEmbed)

     if message.content.startswith('-startspam'):
        ermbed = discord.Embed(title='Spam Menu', description='Write \'-startspm1\' to start spam in one channel, change the number upwards until the spam doesn\'t work to choose between what servers to spam in.(Ex: -startspm(number), -startspm2...) and \'-startspmall\' for spam in as many channels as I can, as well as \'-calmspm\' for a nice \'POGGERZ\' in one server every minute rather than second.\'-stopspam\' to stop the spamming.', color=0xF08080)
        ermbed.set_author(name='POG bot', url='https://absozero.github.io/POG-bot/', icon_url='https://cdn.discordapp.com/attachments/793648359231586327/833616210603016233/unknown.png')
        ermbed.set_footer(text='DM owner to turn on the bot.')
        
        await message.channel.send(embed=ermbed)   

    if message.content.startswith('-me sad'):
        await message.channel.send('I\'m sorry about that UwU.(UwU is still in style, haters!). Anyways, don\'t worry. Look at the fun stuff in life!')

    if message.content.startswith('-startspam'):
        await message.channel.send('Write \'-startspm1\' to start spam in one channel, change the number upwards until the spam doesn\'t work to choose between what servers to spam in.(Ex: -startspm(number), -startspm2...) and \'-startspmall\' for spam in as many channels as I can, as well as \'-calmspm\' for a nice \'POGGERZ\' in one server every minute rather than second.\'-stopspam\' to stop the spamming.')

    if message.content.startswith('-startspm1'):
        spm.start()

    if message.content.startswith('-startspm2'):
        spm1.start()

    if message.content.startswith('-startspm3'):
        spm2.start()

    if message.content.startswith('-startspm4'):
        spm3.start()

    if message.content.startswith('-startspm5'):
        spm4.start()
        

    if message.content.startswith('-startspmall'):
        await message.channel.send('If you are sure about this, I will start spamming \'POGGERZ\' in as many channels as possible. Say \'-stopspam\' for me to stop the spamming.')
        spm.start()
        spm1.start()
        spm2.start()
        spm3.start()
        spm4.start()

    if message.content.startswith('-calmspm'):
        clmspm.start()

    if message.content.startswith('-stopspam'):
        await message.channel.send('Alright, terminating spam system')
        spm.stop()
        spm1.stop()
        spm2.stop()
        spm3.stop()
        spm4.stop()
        clmspm.stop()



@client.event
async def on_ready():
    await client.change_presence(activity=Game(name="-help"))
    print('Starting server')
    print('Bot prepared for use')
    print('We have logged in as {0.user}'.format(client))
    print('Running bot...')

client.run('BOT TOKEN GOES HERE')