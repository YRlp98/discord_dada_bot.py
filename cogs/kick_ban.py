import discord
from discord.ext import commands


class KickBan(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Kick
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'dada {member.mention} be dalile {reason}, kick shod!')

    # Ban
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'dada {member.mention} be dalile {reason}, ban shod!')

    # Unban
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'dada {user.mention} unban shod!')
                return


def setup(client):
    client.add_cog(KickBan(client))