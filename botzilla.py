import discord
import logging
import os

from discord.ext import commands

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
#DEBUG, INFO, WARNING, DANGER, CRITICAL
# logger = logging.getLogger('discord')
# logger.setLevel(logging.INFO)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)

#commands.Discord()
client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print(f"Logged on")

@client.event
async def on_message(message):

    if message.content.startswith('$bing'):
        await message.channel.send('BONG!')

    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

    await client.process_commands(message)

@client.command()
async def ping(ctx):
    """
    This is the sample text
    """
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    await channel.connect()

client.run(TOKEN)
