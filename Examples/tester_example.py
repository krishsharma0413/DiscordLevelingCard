from DiscordLevelingCard import Settings, Tester
import asyncio

setting = Settings(
    # a path is always preferred over a url atleast in a production environment
    background="./bg.jpg", # this is an example name only
    bar_color="white",
    text_color="white")

async def main():
    rank = Tester(
        username="krishsharma0413",
        level=10,
        current_exp=100,
        max_exp=400,
        settings=setting,

        #This is an example only
        avatar="./avatarimg.png", # provide a path to the avatar image instead of a url.

        path = "./example", # the result will be saved in this path as example.png here
        # don't provide the ".png" extension, it will be added automatically
        cacheing = True, # if you want to cache the image, set this to True
    )

    # test card1
    await rank.test_card1(resize=100) # resize to 100% i.e. original size

    # test card2
    await rank.test_card2(resize=100) # resize to 100% i.e. original size

    # test card3
    await rank.test_card3(resize=100) # resize to 100% i.e. original size

    # test sandbox card1
    # card_colour attributes changes the color from black to something else
    # card_colour can be any valid color name (eg. "red") or hex code (eg. "#000000")
    await rank.test_sandbox_card1(resize=100, card_colour="red") # resize to 100% i.e. original size


# since all the functions are coroutines, we need to run them in an event loop
asyncio.run(main())