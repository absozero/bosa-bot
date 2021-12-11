# This is also an important part of the setup process and CANNOT be skipped
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
  - If you are going to have the praw module with the bot then you need the following credentials here(You need a reddit account in order to use the praw functions. If you don't have and/or dont want to make a reddit account then just delete the 'reddit' function in Reddit.py in the cogs folder and use the legacy function to get images from reddit. The legacy command is named 'redit':
  - To learn how to get the reddit secret and client watch this video(from 0:16-0:50): [Reddit secret+client](https://www.youtube.com/watch?v=Q5u6MDQAG7I)
  ```json
  {
    "reddit_secret": "REDDIT_CLIENT",
    "reddit_secret": "REDDIT_SECRET",
    "reddit_username": "YOUR_USERNAME",
    "reddit_password": "YOUR_PASSWORD",
    "reddit_useragent": "pythonpraw" 
  }
  - **We have finished the setup of the bot. Now all there is is to run the bot.**

## Now, head to [Running the bot](Running-bot) to start running and using the bot on the discord service.