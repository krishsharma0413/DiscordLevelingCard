# DiscordLevelingCard
A library with Rank cards for your discord bot.



## card preview

`card1`

![card1](https://cdn.discordapp.com/attachments/907213435358547968/994620579816681572/unknown.png)


<br>

## installation

`for pypi version`
```sh
pip install discordlevelingcard
```

`for github developement version`
```sh
pip install git+https://github.com/ResetXD/DiscordLevelingCard
```

## How To Use

If you don't provide `path` then the method will return `bytes` which can directly be used in discord.py/disnake/pycord/nextcord 's `File class`.


<br>


## Example

`since no path was given, it returns bytes which can directly be used in discord.py and its fork 's File class.`

```py

from disnake.ext import commands
from DiscordLevelingCard import RankCard
import disnake

client = commands.Bot()

@client.slash_command(name="rank")
async def user_rank_card(ctx, user:disnake.Member):
    await ctx.response.defer()
    a = RankCard(
        background=user.banner.url,
        avatar=user.display_avatar.url,
        level=1,
        current_exp=1,
        max_exp=1,
        username="cool username"
    )
    image = await a.card1()
    await ctx.edit_original_message(file=disnake.File(image, filename="rank.png")) # providing filename is very important

```

<br>

`if you want to use path`
```py
@client.slash_command(name="rank")
async def user_rank_card(ctx, user:disnake.Member):
    await ctx.response.defer()
    a = RankCard(
        background="https://cool-banner-url.com",
        avatar=user.display_avatar.url,
        level=1,
        current_exp=1,
        max_exp=1,
        username="cool username",
        bar_color="red",
        text_color="white",
        path="./user_cards/rank_card.png"
    )
    # image return the path provided i.e. "./user_cards/rank_card.png"
    image = await a.card1()
    await ctx.edit_original_message(file=disnake.File(image, filename="rank.png")) # providing filename is very important
```


## Documentation

`RankCard` class

`__init__` method

```py
RankCard(
    background:Union[PathLike, BufferedIOBase],
    avatar:Union[PathLike, BufferedIOBase],
    level:int,
    current_exp:int,
    max_exp:int,
    username:str,
    bar_color:str="white",
    text_color:str="white",
    path:str=None
)
```

`background` - background image url or file-object in `rb` mode

`avatar` - avatar image url or file-object in `rb` mode

`level` - level of the user

`current_exp` - current exp of the user

`max_exp` - max exp of the user

`username` - username of the user

`bar_color` - color of the bar [example: "white" or "#000000"]

`text_color` - color of the text [example: "white" or "#000000"]

`path` - path to save the card [if not provided will return `bytes` instead]

<br>

`card1` method

```py
RankCard.card1()
```

`returns` - `path` if `path` was provided in `__init__` or `bytes` if `path` was not provided in `__init__`

<br>

## todo

- [ ] add more cards
- [ ] better documentation
