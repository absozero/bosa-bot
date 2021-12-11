# This bot is currently being developed in:
**Python version:**
* _[3.9.6](https://www.python.org/downloads/)_
## It uses the modules:
* To install a module in python just open terminal and enter:
```python
pip install "module name"
```
***
**Built in python modules**
* There are multiple modules that come alongside python _3.9.6_ that are used to help the bot run. These modules do not need to be installed seperately.
***

**[discord.py](https://discordpy.readthedocs.io/en/latest/)**
* This module is the core of the bot and allows it to communicate with discord and set up commands. The bot will not function without this module. It is [open source](https://github.com/Rapptz/discord.py).


***

**[(async)](https://github.com/praw-dev/asyncpraw)[praw](https://github.com/praw-dev/praw)**
* This is a module that allows the bot to get data from posts on reddit. It is basically the praw module except for features that allow it to run asynchronously. Since the code to run the command that uses this module is located inside a cog, it is optional to install this module, but the command(s) related to getting reddit posts will not work.