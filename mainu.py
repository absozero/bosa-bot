import os

#Simple code to emulate CLI input and command

os.system("git pull https://github.com/absozero/BOSA-bot.git main")



if os.path.exists("bot"):
    os.chdir('bot')
    os.system("python bot.py")
else:
    print('This file is in the wrong place, make sure it is with the other files from the repo.')

#IMPORTANT!
#The requirements required to run this bot must still be downloaded, they are in requirements.txt