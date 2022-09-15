# from aiohttp import ClientSession
import asyncio
# from io import BytesIO

from src.DiscordLevelingCard.core.image_handler import CardMaker

async def check():
    a = CardMaker()
    await a.level_maker(
        background="https://cdn.discordapp.com/attachments/907213435358547968/996372414181150830/unknown.png",
        avatar="https://cdn.discordapp.com/attachments/907213435358547968/994608810457047172/unknown.png",
        username="ResetXD",
        level=1,
        current_exp=0,
        max_exp=100,
        bar_color="#ff0000",
        text_color="#ffffff"
    )
#     async with ClientSession() as session:
#         async with session.get("https://cdn.discordapp.com/attachments/992333362503106630/1016265062480105592/final.png") as response:
#             data = await response.read()
#             image = Image.open(BytesIO(data))
#             image.save("damn.png")

asyncio.run(check())