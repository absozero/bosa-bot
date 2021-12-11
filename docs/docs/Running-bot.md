# If you are running the bot yourself, everything from [Setup](Bot-Setup-on-local-computer) MUST be completed.
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

###  Join the help server for faster replies: [BOSA-bot server](https://discord.gg/tmFf5zt827)