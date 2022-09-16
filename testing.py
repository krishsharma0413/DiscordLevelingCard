from disnake.ext import commands
import dotenv
import os
from DiscordLevelingCard import RankCard
import disnake

dotenv.load_dotenv(".env")

# region [Constants]
client = commands.Bot(reload=True, intents=disnake.Intents().all(),test_guilds=[946821391183925328])
token = os.getenv("discord_token")
# endregion [Constants]

# region [Events]
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
# endregion [Events]

# client.load_extensions(f"commands")

@client.slash_command(name="abcde")
async def not_Testing(ctx):
    await ctx.response.defer()
    a = RankCard(
        background="https://cdn.discordapp.com/attachments/907213435358547968/1019966057294860328/final.png",
        avatar="https://cdn.discordapp.com/attachments/907213435358547968/1019966057294860328/final.png",
        level=1,
        current_exp=1,
        max_exp=1,
        username="test",
        type="disnake"
    )
    image = await a.card1()
    await ctx.edit_original_message(file=image)