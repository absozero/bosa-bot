# BOSA-bot

![Logo](https://cdn.discordapp.com/avatars/844755365191352358/9d8fd75f36f5bd4e2866e6fcd8acac26.png?size=128)

## Info
A discord spam bot that will become a general discord bot.
- It is being actively developed.
- May be slightly unstable


**Version 2.0**


## Downloading requirements to run the bot
-Download source code from 'releases' tab on github or clone using git:
```
git clone https://github.com/absozero/BOSA-bot.git
```
- Requires ***python interpreter downloaded*** and the discord.py module

  - <https://www.python.org/downloads> Install python and remember to select the option to ***install pip in the settings tab*** for the installation since we will be needing that for **installing packages.**

  - After the ***python interpreter has installed, open your terminal***(cmd, bash, powershell, etc.)

  - Enter this in and follow all of the prompts that the terminal may give you(Answer yes toeverything it asks so the package installs properly)

  ```
  pip install discord.py
  ```
  ![pip](https://cdn.discordapp.com/attachments/829239591952580651/845095266939568158/unknown.png)

  - Congrats! You have finished ***downloading the requirements to run the bot!***
  
## Initial setup to run the bot 
- After the requirements have successfully installed, create an application on the discord developer portal 
  - [Discord developer portal](https://discord.com/developers/applications)
  - After creating a bot in the bot tab, copy the token by pressing the copy button
  - ![Copy](https://cdn.discordapp.com/attachments/829239591952580651/845070279322370092/68747470733a2f2f73636f6e74656e742d6c6178332d312e63646e696e7374616772616d2e636f6d2f762f7435312e323838.png) 

- Then, in the 'bot' folder of the source code ***make a file called info.json.***

  - In ***info.json*** put the following(enter token you copied where it says to put it):
  ```json
  {
    "Token": "YOUR TOKEN GOES HERE"
  }
  ```

  - There is ***one last thing to do*** to be able to run the bot.
  - In bot.py, there should be this code
  ```python
  with open("BOSA-bot/bot/info.json") as f:
    info = json.load(f)
  ```
  - Change the value to this:
  ```python
  with open("info.json") as f:
    info = json.load(f)
  ```
  - Since we will be running the bot from inside the 'bot' folder.

  - ***You are now done with the initial setup!*** 

## Running the bot

- After, ***run the bot.py*** file using 
```py
python bot.py
```
-  In whatever terminal you use, make sure the ***terminal is at the directory*** in which the file is in.

- In most terminals, you can use this command to change the directory:
```
cd YOURPATHTOTHEFOLDER/bot
```
![terminal](https://cdn.discordapp.com/attachments/829239591952580651/845095992504483910/unknown.png)
  - Where **YOURPATHTOTHEFOLDER** is just the path to bot folder

  -If you have any specific problems on this part, [google](https://www.google.com/) may be a great place to go to.

- ***Don't change any of the files downloaded from github except the ones that were told to be changed unless you know what you are doing.***

- If you were able to run the command and ***two lines were printed in the terminal, then congrats! You have successfully ran your own instance*** of the bot!

![printedlines](https://cdn.discordapp.com/attachments/829239591952580651/845096493429817385/unknown.png)
- If there are error messages read the instructions in this README again and/or go to <https://www.google.com/> to find the reason for the error and the fixes.
## Another simple way to use
- Add the bot to your server(bot requires admin permissions):
- [Invite Link](https://discord.com/api/oauth2/authorize?client_id=844755365191352358&permissions=8&scope=bot)

- The bot will not be running all the time ***since I run it locally so the better option would definitely be to host it yourself. This option may be a good choice once I find a good vps to host the bot on.***

## Conclusion 

- Though the README may be long, I have made it to be as easy as possible to understand and use even for non-developers, and if there are any errors, the best thing to do is to read the README again or search it up on a search engine.

- Have fun while using the bot! (Being actively developed by 1 person, so development may be slow.)

## Website

[Website(based on this README)](https://absozero.github.io/BOSA-bot/)
