# Installation

## Download requirements
-Download source code from the 'main' branch on github or clone using git:
```
git clone https://github.com/absozero/BOSA-bot.git
```
- Requires ***python interpreter downloaded*** and the discord.py module with its subdependencies

```shell
cd BOSA-bot
```
  - Install dependencies:

  ```
  pip install -r requirements.txt
  ```


## Discord Developer portal and getting Bot token 
- After the requirements have successfully installed, create an application on the discord developer portal 
  - [Discord developer portal](https://discord.com/developers/applications)
  - After creating a bot in the bot tab, copy the token by pressing the copy button
  - ![Copy](../img/token.png) 

- Then, in the folder of the source code where bot.py is ***make a file called info.json.***

  - In ***info.json*** put the following(enter token you copied where it says to put it, basically replace where it says to put your token underneath. Replace everything between the quotation marks with the token, but don't delete the quotation marks themselves):

  ```
  {
    "token": "YOUR_TOKEN_HERE"
  }
  ```

# Running bot

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

![terminal](../img/terminal.png)


![printedlines](../img/lines.png)

- _**To run the bot again, just run the "runner.py" file again using the instructions and guidelines mentioned at the beginning of this page.**_

- If there are error messages, please open an [issue](https://github.com/absozero/bosa-bot/issues) on github.

