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

<details>

<summary> <span style="color:yellow">custom_canvas</span> method</summary>


```py
Sandbox.custom_canvas(
    resize:int = 100,

    senstivity:int = 200,
    card_colour: str = "black",

    border_width: int = 25,
    border_height: int = 25,
    
    avatar_frame: str = "curvedborder",
    avatar_size: int = 260,
    avatar_position: tuple = (53, 36),
    
    text_font: str = "levelfont.otf",

    username_position: tuple = (330,130),
    username_font_size: int = 50,

    level_position: tuple = (500,40),
    level_font_size: int = 50,

    exp_position: tuple = (775,130),
    exp_font_size: int = 50,

)
```

## attribute
  - `has_background` : if set to `True` then it will add a background to the image. (default is `True`)
  - `background_colour` : color of the background. (default is `black`)
  - `canvas_size` : size of the canvas. (default is `(1000, 333)`)
  - `resize` : resize the final image. (default is 100, treat it as a percentage.)
  - `overlay` : A list of overlays to be placed on the background. (Default is `[[(1000-50, 333-50),(25, 25), "black", 200]]`.)
  - `avatar_frame` : `circle` `square` `curvedborder` `hexagon` or path to a self created mask. (Default is `curvedborder`.)
  - `text_font` : Default is `levelfont.otf` or path to a custom otf or ttf file type font.
  - `avatar_size` : size of the avatar. (default is `260`)
  - `avatar_position` : position of the avatar. (default is `(53, 36)`)
  - `username_position` : position of the username. (default is `(330,130)`)
  - `username_font_size` : font size of the username. (default is `50`)
  - `level_position` : position of the level. (default is `(500,40)`)
  - `level_font_size` : font size of the level. (default is `50`)
  - `exp_position` : position of the exp. (default is `(775,130)`)
  - `exp_font_size` : font size of the exp. (default is `50`)
  - `exp_bar_width` : width of the exp bar. (default is `619`)
  - `exp_bar_height` : height of the exp bar. (default is `50`)
  - `exp_bar_background_colour` : color of the exp bar background. (default is `white`)
  - `exp_bar_position` : position of the exp bar. (default is `(330, 235)`)
  - `exp_bar_curve` : curve of the exp bar. (default is `30`)
  - `extra_text` : A list of extra text to be placed on the image. (Default is `None`.)
  - `exp_bar` : The calculated exp of the user. (Default is `None`.)


## returns 
- `bytes` which can directly be used within `discord.File` class.


## examples

![custom_canvas](https://raw.githubusercontent.com/krishsharma0413/DiscordLevelingCard/main/Examples/custom%20card%20examples/custom%20card3%20example-1.png)

![custom_canvas](https://raw.githubusercontent.com/krishsharma0413/DiscordLevelingCard/main/Examples/custom%20card%20examples/custom%20card3%20unholy%20example-2.png)


An Example that i really loved was this one, here is the code for it as well. (you might have to tweak a lot to make it work for you though. )

```py
from DiscordLevelingCard import Sandbox, Settings
import asyncio
from PIL import Image

setting = Settings(
    background="./bg.jpg",
    bar_color="green",
    text_color="white")

async def main():
    rank = Sandbox(
        username="krishsharma0413",
        level=1,
        current_exp=10,
        max_exp=400,
        settings=setting,
        avatar=Image.open("./avatarimg.png")
    )
    result = await rank.custom_canvas(
        avatar_frame="square",
        avatar_size=233,
        avatar_position=(50, 50),
        exp_bar_background_colour = "black",
        exp_bar_height=50,
        exp_bar_width=560,
        exp_bar_curve=0,
        exp_bar_position=(70, 400),
        username_position=(320, 50),
        level_position=(320, 225),
        exp_position=(70, 330),
        canvas_size=(700, 500),

        overlay=[[(350, 233),(300, 50), "white", 100],
                 [(600, 170),(50, 300), "white", 100]],

        extra_text=[
            ["bio-", (320, 110), 25, "white"],
            ["this can very well be a bio", (320, 140), 25, "white"],
            ["even mutiple lines!", (320, 170), 25, "white"],
            ["if we remove bio- even more!", (320, 200), 25, "white"],
            ]

    )
    
    # you don't need this line if you are using this in discord.py
    Image.open(result).save("result.png", "PNG")


asyncio.run(main())
```

and this is how it looks :D

![custom_canvas](https://raw.githubusercontent.com/krishsharma0413/DiscordLevelingCard/main/Examples/custom%20card%20examples/extra%20canvas%20example.png)

<br>

</details>


<br><br>

if you want to see changelog then click [here](https://github.com/krishsharma0413/DiscordLevelingCard/blob/main/CHANGELOG.md)

<br><br>
please star the <a href="https://github.com/krishsharma0413/DiscordLevelingCard">repository</a> if you like it :D
