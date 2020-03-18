import discord
from discord.ext import commands

token = 'Njg5NTM1MjAwNzQwMjQ1NjIy.XnJmIg.vVSX0t31rqlDzBUwVqnemZyIJSw'
client = commands.Bot(command_prefix='~')

# !to check bot is up or not
@client.event
async def on_ready():
    print('Bot is ready!')

# !the bot commands
# show user ping
@client.command()
async def ping(ctx):
    await ctx.send(f':stopwatch: {round(client.latency * 1000)}ms')


client.run(token)
