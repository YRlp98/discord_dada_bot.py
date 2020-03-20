import discord
from discord.ext import commands


class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    # show user ping
    @commands.command(aliases=['Ping'])
    async def ping(self, ctx):
        await ctx.send(f':stopwatch: {round(self.client.latency * 1000)}ms')


def setup(client):
    client.add_cog(Ping(client))
