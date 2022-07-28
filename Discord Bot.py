# Discord Bot

# Setup
import json, discord
from discord.ext import commands

# Discord Token - hidden key
with open('misc.json') as f:
    token = json.load(f)['api_keys']['discord_bot_token']

# Bot setup
client = commands.Bot("#!")

@client.event
async def on_ready():
    print("Bot ready!")
    print("----------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello. I'm a bot!")



# Run Bot
client.run(token)





