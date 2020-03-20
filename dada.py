import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("DADA_TOKEN")
client = commands.Bot(command_prefix='~')



# !Response with a random awnseer
@client.command(aliases=['Estekhare', 'soal', 'Soal'])
async def estekhare(ctx, *, question):
    responses = [
        'gi nakhor dada!',
        'gi bokhor dada'
    ]
    await ctx.send(f'dar javabe solae: {question}\nbayad begam ke: {random.choice(responses)}')


# !Load and run
# Load
@client.command()
async def load(ctx, extention):
    client.load_extension(f'cogs.{extention}')

# Unload
@client.command()
async def unload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')

for filenmae in os.listdir('./cogs'):
    if filenmae.endswith('.py'):
        client.load_extension(f'cogs.{filenmae[:-3]}')

# to check bot is up or not
@client.event
async def on_ready():
    print('Bot is ready!')

client.run(token)
