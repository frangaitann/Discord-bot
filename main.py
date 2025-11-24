import asyncio
from modules.cmds import *
from modules.events import *
from modules.defs import bot

token = "TOKEN" # <---- Here it goes your discord developer portal bot token

async def main():
    
    await asyncio.gather(
        bot.start(token),
    )
    
asyncio.run(main())

# This bot is an example one, with the structure ready to run, you can modify the code for adding/removing/modifying features and many things can be improved as logs system, channel id variables, etc.



# Added features:
# Event Logs, Embed Builder command, Epic Games free-weekly games notifier, Clean command, Messi funny command


# ADVICE: All the texts are in spanish, but the whole code is in english for better understanding.
