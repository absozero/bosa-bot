import os
from sys import platform

os.system('git pull https://github.com/absozero/BOSA-bot.git main')

import os
#Code to run the bot

if os.path.isfile("bot.py"):
        os.system("python bot.py")
if platform == "linux" or platform == "linux2":
        if os.path.isfile("bot.py"):
                os.system("python3 bot.py")
else:
    print('This file is in the wrong place, or bot.py file is not available. Make sure it is with the other files from the repo.')
