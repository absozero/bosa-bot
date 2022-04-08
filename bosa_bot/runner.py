import os
from sys import platform
#Code to run the bot
def main():

    os.system('git pull https://github.com/absozero/BOSA-bot.git main')
    print(platform)

    if os.path.isfile("requirements.txt"):
        os.system("pip install -r requirements.txt")
    if platform == "linux" or platform == "linux2":
        if os.path.isfile("requirements.txt"):
                os.system("pip3 install -r requirements.txt")


    if os.path.isfile("./bosa_bot/main.py"):
        os.system("python bosa_bot/main.py")
    if platform == "linux" or platform == "linux2":
        if os.path.isfile("./bosa_bot/main.py"):
                os.system("python3 bosa_bot/main.py")
    else:
        print('This file is in the wrong place, or bot.py file is not available. Make sure it is with the other files from the repo.')
