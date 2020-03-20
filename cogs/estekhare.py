import discord
import os
import random
from discord.ext import commands


def is_admin(member: discord.Member):
    for role in member.roles:
        if role.id == int(os.getenv("DADA_ADMIN_ID")):
            return True
    return False


class Estekhare(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Response with a random awnseer
    @commands.command(aliases=['Estekhare', 'soal', 'Soal, gi, Gi'])
    async def estekhare(self, ctx, *, question):
        responses = [
            'gi nakhor dada!',
            'gi bokhor dada'
        ]
        # await ctx.send(f'dar javabe solae: {question}\nbayad begam ke: {random.choice(responses)}')
        await ctx.send(f'{random.choice(responses)}')


def setup(client):
    client.add_cog(Estekhare(client))
