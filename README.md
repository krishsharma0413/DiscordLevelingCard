# DiscordLevelingCard
A library with Rank cards for your discord bot.

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

from disnake.ext import commands
from DiscordLevelingCard import RankCard
import disnake

client = commands.Bot()

@client.slash_command(name="rank")
async def user_rank_card(ctx, user:disnake.Member):
    await ctx.response.defer()
    a = RankCard(
        background="./my_cool_background.png",
        avatar=user.display_avatar.url,
        level=1,
        current_exp=1,
        max_exp=1,
        username="cool username",
        type="disnake"
    )
    image = await a.card1()
    await ctx.edit_original_message(file=image)

```

`or you can use no type`

```py
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
    await ctx.edit_original_message(file=disnake.File(image))
```

`if you want to use path`
```py
@client.slash_command(name="rank")
async def user_rank_card(ctx, user:disnake.Member):
    await ctx.response.defer()
    a = RankCard(
        background=user.banner.url,
        avatar=user.display_avatar.url,
        level=1,
        current_exp=1,
        max_exp=1,
        username="cool username",
        path="./user_cards/rank_card.png"
    )
    # image return the path provided i.e. "./user_cards/rank_card.png"
    image = await a.card1()
    await ctx.edit_original_message(file=disnake.File(image))
```