# Discord Bot

# Setup
import json, discord, requests
from discord.ext import commands
from discord import FFmpegPCMAudio

# Discord hidden keys
with open('misc.json') as f:
    token = json.load(f)['api_keys']['discord_bot_token']
with open('misc.json') as f:
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

@client.command(pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('C:\\Users\\48513\\Music\\ucho.mp3')
        player = voice.play(source)
    else:
        await ctx.send("You are not in a voice channel!")

@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left the voice chat")
    else:
        await ctx.send("I'm not in a voice channel!")

@client.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Not playing anything!")

@client.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Not playing anything!")

@client.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
    else:
        await ctx.send("Not playing anything!")

@client.command(pass_context = True)
async def play(ctx, arg):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio(arg)
    player = voice.play(source)












# Run Bot
client.run(token)





