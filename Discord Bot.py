# Discord Bot

# Setup
import json, discord
from discord.ext import commands

# Discord hidden keys
with open('misc.json') as f:
    token = json.load(f)['api_keys']['discord_bot_token']
    channel_id = json.load(f)['discord_bot']['channel_id']

# Bot Setup
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="^", intents=intents)

@client.event
async def on_ready():
    print("Bot ready!")
    print("----------")

# Bot Events

@client.event
async def on_member_join(member):
    channel = client.get_channel(channel_id)
    await channel.send("Hello "+member)

# Bot Commands

@client.command()
async def hello(ctx):
    await ctx.send("Hello. I'm a bot!")



# Run Bot
client.run(token)





