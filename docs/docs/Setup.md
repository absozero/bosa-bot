# Installation

## Download requirements
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

## Discord Developer portal and getting Bot token 
- After the requirements have successfully installed, create an application on the discord developer portal 
  - [Discord developer portal](https://discord.com/developers/applications)
  - After creating a bot in the bot tab, copy the token by pressing the copy button
  - ![Copy](https://cdn.discordapp.com/attachments/829239591952580651/845070279322370092/68747470733a2f2f73636f6e74656e742d6c6178332d312e63646e696e7374616772616d2e636f6d2f762f7435312e323838.png) 

- Then, in the folder of the source code where bot.py is ***make a file called info.json.***

  - In ***info.json*** put the following(enter token you copied where it says to put it, basically replace where it says to put your token underneath. Replace everything between the quotation marks with the token, but don't delete the quotation marks themselves):
  ```json
  {
    "token": "YOUR_TOKEN_HERE"
  }
  ```
  - Since we are making a variable with the token in it that the bot.py file can call, it uses the token inside the variable to run the discord bot.
  - **We have finished the setup of the bot. Now all there is is to run the bot.**

# Running bot
-  In whatever terminal you use, make sure the ***terminal is at the directory*** in which the file is in.

- In most terminals, you can use this command to change the directory:
```shell
cd "Full Path to folder where the bot files are"
```
- An example of changing the directory:
```shell
(example: cd C:/Users/Name/Desktop/bot, where inside the folder "bot", there is the file "main.py")
```
Run the file called **runner.py** that, when run, will automatically pull from the stable main branch.
- **To be run, this file requires the repo to have been initially cloned using git(or overwritten by cloning this repo from git) and ***git must be installed on your computer for this.*** 
```python
python runner.py
```
If on linux, this should work:
```python
python3 runner.py
```
- You could also just run **bot.py** from the main source code folder, it does the same thing. There is just more code to look at and if it fails to load there will be a long error message.

![terminal](https://cdn.discordapp.com/attachments/829239591952580651/845095992504483910/unknown.png)

  -If you have any specific problems on this part, [google](https://www.google.com/) may be a great place to go to.

- ***Don't change any of the files downloaded from github except the ones that were told to be changed unless you know what you are doing.***

- If you were able to run the command and ***A few lines about the bot and it starting are printed, then congrats! You just successfully ran your own instance*** of the bot!

![printedlines](https://cdn.discordapp.com/attachments/829239591952580651/845096493429817385/unknown.png)
- _**To run the bot again, just run the "BOTSTARTER.py" file again using the instructions and guidelines mentioned at the beginning of this page.**_
- If there are error messages read the instructions in the wiki again and/or go to <https://www.google.com/> to find the reason for the error and the fixes for the problem.

- Otherwise, if the error is my fault, go to the [Issues tab](https://github.com/absozero/BOSA-bot/issues) to open an issue about it.
