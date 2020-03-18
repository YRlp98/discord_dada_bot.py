import discord
import random
from discord.ext import commands

token = 'Njg5NTM1MjAwNzQwMjQ1NjIy.XnJmIg.vVSX0t31rqlDzBUwVqnemZyIJSw'
client = commands.Bot(command_prefix='~')

# !to check bot is up or not
@client.event
async def on_ready():
    print('Bot is ready!')

# !the bot commands

# show user ping
@client.command(aliases=['Ping'])
async def ping(ctx):
    await ctx.send(f':stopwatch: {round(client.latency * 1000)}ms')

# Response with a random awnseer
@client.command(aliases=['Estekhare', 'soal', 'Soal'])
async def estekhare(ctx, *, question):
    responses = [
        'gi nakhor dada!',
        'gi bokhor dada'
    ]
    await ctx.send(f'dar javabe solae: {question}\nbayad begam ke: {random.choice(responses)}')


client.run(token)
