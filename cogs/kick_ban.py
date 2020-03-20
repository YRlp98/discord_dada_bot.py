import discord
import os
from discord.ext import commands


def is_admin(member: discord.Member):
    for role in member.roles:
        if role.id == int(os.getenv("DADA_ADMIN_ID")):
            return True
    return False


class KickBan(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Kick
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if is_admin(ctx.author):
            await member.kick(reason=reason)
            await ctx.send(f'dada {member.mention} be dalile {reason}, kick shod!')
        else:
            await ctx.send(f'gi nakhor dada!')

    # Ban
    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if is_admin(ctx.author):
            await member.ban(reason=reason)
            await ctx.send(f'dada {member.mention} be dalile {reason}, ban shod!')
        else:
            await ctx.send(f'gi nakhor dada!')

    # Unban
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if is_admin(ctx.author):
                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f'dada {user.mention} unban shod!')
                return
            else:
                await ctx.send(f'gi nakhor dada!')


def setup(client):
    client.add_cog(KickBan(client))
