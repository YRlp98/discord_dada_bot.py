import discord
import random
from discord.ext import commands

token = ''
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


# !Kick/Ban commands
# kick
@client.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)

# Ban
@client.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)

# !Response with a random awnseer
@client.command(aliases=['Estekhare', 'soal', 'Soal'])
async def estekhare(ctx, *, question):
    responses = [
        'gi nakhor dada!',
        'gi bokhor dada'
    ]
    await ctx.send(f'dar javabe solae: {question}\nbayad begam ke: {random.choice(responses)}')


client.run(token)
