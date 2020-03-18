import discord
from discord.ext import commands

token = 'Njg5NTM1MjAwNzQwMjQ1NjIy.XnJcYQ.jRyMZOk1nogZf6ckqRieGsN0OFg'
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Bot is ready!')

client.run(token)
