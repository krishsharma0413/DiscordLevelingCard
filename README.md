# DiscordLevelingCard
[ WIP ] A library with leveling cards for your discord bot.

<br>


## How To Use

```py
from DiscordLevelingCard import CardMaker

card = CardMaker()
card.type1(
    background= "./background.png",
    avatar= "https://url-to-avtar.com",
    level= 100,
    username= "Username",
    current_exp=1000,
    max_exp=10000,
    bar_color="white",
    text_color="#000000",
    path="./user_cards/Username.png"
)
```
If you don't provide `path` then the method will return `bytes` which can directly be used in discord.py/disnake/pycord/nextcord 's `File class`.


<br>

## card preview

`type1`

![card preview](https://cdn.discordapp.com/attachments/907213435358547968/994620579816681572/unknown.png)


## Example

```py

import disnake


