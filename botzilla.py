import logging
import os

import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
#DEBUG, INFO, WARNING, DANGER, CRITICAL
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print(f"Logged on")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$bing'):
        await message.channel.send('BONG!')

    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

@client.command()
async def ping(ctx):
    """
    This is the sample text
    """
    latency = client.latency
    await ctx.send(latency)

# class MyClient(commands.Bot):

#     async def on_ready(self):
#         print(f"Logged on as {self.user}")

#     # @client.event
#     async def on_message(self, message):
#         if message.author == client.user:
#             return

#         if message.content.startswith('$ping'):
#             await message.channel.send('PONG!')

#         if message.content.startswith('$greet'):
#             channel = message.channel
#             await channel.send('Say hello!')

#         # def check(m):
#         #     return m.content == 'hello' and m.channel == channel

#         # msg = await client.wait_for('message', check=check)
#         # await channel.send('Hello {.author}!'.format(msg))

#     async def test(self, ctx, arg):
#         print("hit this")


# client = MyClient(
#     command_prefix='$',
# )

client.run(TOKEN)
