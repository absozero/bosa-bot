# Installation

## Downloading requirements to run the bot
-Download source code from the 'main' branch on github or clone using git:
```
git clone https://github.com/absozero/BOSA-bot.git
```
- Requires ***python interpreter downloaded*** and the discord.py module with its subdependencies

  - <https://www.python.org/downloads> Install python and remember to select the option to ***install pip in the settings tab*** for the installation since we will be needing that for **installing packages.**

  - After the ***python interpreter has installed, open your terminal***(cmd, bash, powershell, etc.)
  - Change the terminal directory to the location of requirements.txt. You can do this by entering this in the terminal:
```shell
cd "full path to the folder where requirements.txt is stored" 
```
- An example of changing the directory:
```shell
(ex: cd C:/Users/Name/Desktop/bot, where inside the folder "bot" the "requirements.txt" file is located)
```
  - Enter this in and follow all of the prompts that the terminal may give you(Answer yes to everything it asks so the package installs properly. You can copy from github and past it in the terminal using the clipboard button and using Ctrl/Command-V).

  ```
  pip install -r requirements.txt
  ```

  - Congrats! You have finished ***downloading the requirements to run the bot!***
  


## Now, head to [Finish necessary bot registration and token collection and usage](Discord-Dev-page-and-getting-bot-token) to finish up the setup of the bot