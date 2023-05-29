# DiscordLevelingCard
A library with Rank cards for your discord bot.

<h3 style="color:yellow;"> now create your own custom rank cards!</h3>

<br>

[![Downloads](https://pepy.tech/badge/discordlevelingcard)](https://pepy.tech/project/discordlevelingcard)

# card preview

`card1`

![card1](https://user-images.githubusercontent.com/77439837/234198272-3dcaabb0-0f38-4d51-9938-de4b0ad42123.png)


`card2`
![card2](https://user-images.githubusercontent.com/77439837/234198354-315e9420-9bd7-47bd-87ed-b21c3772646c.png)


`card3` *same as card2 but with background*
![card3](https://user-images.githubusercontent.com/77439837/234203410-a6a970ef-c01c-454b-be67-6dc7c1b2c807.png)

<br>

# installation

`for pypi version`
```sh
pip install discordlevelingcard
```

`for github developement version`
```sh
pip install git+https://github.com/krishsharma0413/DiscordLevelingCard
```

# How To Use

If you don't provide `path` then the method will return `bytes` which can directly be used in discord.py/disnake/pycord/nextcord 's `File class`.


<br>


# Example

`since no path was provided, it returns bytes which can directly be used in discord.py and its fork's File class.`

```py
from disnake.ext import commands
from DiscordLevelingCard import RankCard, Settings
import disnake

client = commands.Bot()
# define background, bar_color, text_color at one place
card_settings = Settings(
    background="url or path to background image",
    text_color="white",
    bar_color="#000000"
)

@client.slash_command(name="rank")
async def user_rank_card(ctx, user:disnake.Member):
    await ctx.response.defer()
    a = RankCard(
        settings=card_settings,
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

## Documentation


<details>

<summary> <span style="color:yellow">RankCard</span> class</summary>

<br>

`__init__` method

```py
RankCard(
    settings: Settings,
    avatar:str,
    level:int,
    current_exp:int,
    max_exp:int,
    username:str,
    rank: Optional[int] = None
)
```

- `settings` - Settings class from DiscordLevelingCard.

- `avatar` - avatar image url.

- `level` - level of the user.

- `current_exp` - current exp of the user.

- `max_exp` - max exp of the user.

- `username` - username of the user.

- `rank` - rank of the user. (optional)

## methods

- `card1`
- `card2`
- `card3`

</details>

<details>

<summary> <span style="color:yellow">Sandbox</span> class</summary>

<br>

`__init__` method

```py
RankCard(
    settings: Settings,
    avatar:str,
    level:int,
    current_exp:int,
    max_exp:int,
    username:str,
    cacheing:bool = True,
    rank: Optional[int] = None
)
```

- `settings` - Settings class from DiscordLevelingCard.

- `avatar` - avatar image url.

- `level` - level of the user.

- `current_exp` - current exp of the user.

- `max_exp` - max exp of the user.

- `username` - username of the user.

- `rank` - rank of the user. (optional)

- `cacheing` - if set to `True` then it will cache the image and will not regenerate it again. (default is `True`)
  

## methods
- `custom_card1`
  
</details>




<details>

<summary> <span style="color:yellow">Settings</span> class</summary>

<br>

`__init__` method

```py
Settings(
    background: Union[PathLike, BufferedIOBase, str],
    bar_color: Optional[str] = 'white',
    text_color: Optional[str] = 'white',
    background_color: Optional[str]= "#36393f"

)
```

- `background` - background image url or file-object in `rb` mode.
  - `4:1` aspect ratio recommended.

- `bar_color` - color of the bar [example: "white" or "#000000"]

- `text_color` - color of the text [example: "white" or "#000000"]

- `background_color` - color of the background [example: "white" or "#000000"]

</details>


<details>

<summary> <span style="color:yellow">card1</span> method</summary>


```py
RankCard.card1(resize: int = 100)
```

## attribute
- `resize` : resize the final image. (default is 100, treat it as a percentage.)



## returns 
- `bytes` which can directly be used within `discord.File` class.



![card1](https://user-images.githubusercontent.com/77439837/234198272-3dcaabb0-0f38-4d51-9938-de4b0ad42123.png)

<br>

</details>


<details>

<summary> <span style="color:yellow">card2</span> method</summary>


```py
RankCard.card2(resize: int = 100)
```

## attribute
- `resize` : resize the final image. (default is 100, treat it as a percentage.)

## returns
- `bytes` which can directly be used within `discord.File` class.



![card](https://user-images.githubusercontent.com/77439837/234198354-315e9420-9bd7-47bd-87ed-b21c3772646c.png)

<br>

</details>


<details>

<summary> <span style="color:yellow">card3</span> method</summary>


```py
RankCard.card3(resize: int = 100)
```

## attribute
- `resize` : resize the final image. (default is 100, treat it as a percentage.)

## returns
- `bytes` which can directly be used within `discord.File` class.



![card3](https://user-images.githubusercontent.com/77439837/234203410-a6a970ef-c01c-454b-be67-6dc7c1b2c807.png)

<br>

</details>

<details>

<summary> <span style="color:yellow">custom_card1</span> method</summary>


```py
Sandbox.custom_card1(card_colour:str = "black", resize: int = 100)
```

## attribute
- `resize` : resize the final image. (default is 100, treat it as a percentage.)
- `card_colour` : color of the card. (default is black)



## returns 
- `bytes` which can directly be used within `discord.File` class.


## examples
![custom_card1](https://raw.githubusercontent.com/krishsharma0413/DiscordLevelingCard/main/Examples/custom%20card%20examples/blue_card1.png)

![custom_card1](https://raw.githubusercontent.com/krishsharma0413/DiscordLevelingCard/main/Examples/custom%20card%20examples/white_card1.png)

![custom_card1](https://raw.githubusercontent.com/krishsharma0413/DiscordLevelingCard/main/Examples/custom%20card%20examples/black_card1.png)

<br>

</details>


<br><br>

if you want to see changelog then click [here](https://github.com/krishsharma0413/DiscordLevelingCard/blob/main/CHANGELOG.md)

<br><br>
please star the <a href="https://github.com/krishsharma0413/DiscordLevelingCard">repository</a> if you like it :D
