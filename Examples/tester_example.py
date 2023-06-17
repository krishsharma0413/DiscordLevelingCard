from DiscordLevelingCard import Settings, Tester
import asyncio

setting = Settings(
    # a path is always preferred over a url atleast in a production environment
    background="./bg.jpg", # this is an example name only
    background_color="#36393f",
    bar_color="white",
    bar_outline_color="black",
    text_color="white")

async def main():
    rank = Tester(
        username="krishsharma0413",
        level=10,
        current_exp=100,
        max_exp=400,
        settings=setting,
        rank=1,

        #This is an example only
        avatar="./avatarimg.png", # provide a path to the avatar image instead of a url.

        path = "./example", # the result will be saved in this path as example.png here
        # don't provide the ".png" extension, it will be added automatically
        cacheing = True, # if you want to cache the image, set this to True
    )

    # test card1
    await rank.test_card1(resize=100)  # resize to 100% i.e. original size

    # test card2
    await rank.test_card2(resize=100)  # resize to 100% i.e. original size

    # test card3
    await rank.test_card3(resize=100)  # resize to 100% i.e. original size

    # test card4
    await rank.test_card4(resize=100, use_image=True)  # resize to 100% and to use the custom background

    # test sandbox card1
    # card_colour attributes changes the color from black to something else
    # card_colour can be any valid color name (eg. "red") or hex code (eg. "#000000")
    await rank.test_sandbox_card1(resize=100, card_colour="red") # resize to 100% i.e. original size

    # border width and height is uderstandable
    # senstivity changes the transparency of the black box
    # avatar_frame can be "circle" "square" "hexagon" "curved border" or
    # add your own by providing the path to the mask
    # there are a lot of features which might take a long time to explain...
    await rank.test_sandbox_card3(border_height=0, border_width=0, senstivity=100, avatar_frame="./uwudiscord.png")


# even though you dont need to go in this much depth, i added it for those who would love to.
from PIL import Image, ImageDraw, ImageFont

# since the original image is 1000x333, we need to calculate the width of the text
draw = ImageDraw.Draw(Image.new("RGBA", (1000,333), "black"))

# the variable "w" is very useful if you want to algin the text to the right
w = draw.textlength("100/400", font=ImageFont.truetype("./fontt.ttf", 20))


async def main_2():
    rank = Tester(
        username="krishsharma0413",
        avatar = "./av.png",
        level=10,
        current_exp=100,
        max_exp=400,
        settings=setting,
        cacheing=True
    )

    await rank.test_sandbox_card3(
        border_height=0,
        border_width=0,
        senstivity=80,
        card_colour="black",
        text_font="./fontt.ttf",
        # avatar_frame="circle",
        # use defaults like "square" "circle" "hexagon" "curvedborder" or provide a path to your own mask
        avatar_frame="./uwudiscord.png",

        # avatar_size is the size of the avatar. Default is 260
        avatar_size=230,
        # avatar_position is the position of the avatar. Default is (53, 36)
        avatar_position=(53, 76),

        # username_font_size is the size of the username. Default is 50
        username_font_size=25,

        # too much to write...
        # i hope you understand yourself... if not, then you can always ask me

        username_position=(330, 200),

        level_font_size=20,
        level_position=(330, 295),

        exp_font_size=20,
        exp_position=(930, 295)
        
        )

# since all the functions are coroutines, we need to run them in an event loop
asyncio.run(main())