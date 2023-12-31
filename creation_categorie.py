import discord
from discord.ext import commands


class CreationCategorie(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def creacategorie(self,ctx, name):
        await ctx.guild.create_category(name)

    @commands.command()
    async def creachannel(self, ctx, name, categorie):
        for categori in ctx.guild.categories:
            if categori.name.upper() == categorie.upper():
                await ctx.guild.create_text_channel(name, category=categori)

    # Crée un rôle + des channels qui sont propre au role + aux admins
    @commands.command()
    async def team(self, ctx, name_cat):
        await ctx.guild.create_role(name=name_cat, colour=discord.Colour(0xe74c3c))
        await ctx.guild.create_category(name_cat)

        for categori in ctx.guild.categories:
            if categori.name.upper() == name_cat.upper():
                perms = discord.PermissionOverwrite()
                perms.read_messages = False
                perms2 = discord.PermissionOverwrite()
                perms2.read_messages = True
                role = discord.utils.get(ctx.guild.roles, name=name_cat)
                admin = discord.utils.get(ctx.guild.roles, name="admin")
                for rolle in ctx.guild.roles:
                    if rolle == role or rolle == admin:
                        await categori.set_permissions(rolle, overwrite=perms2)
                    else:
                        await categori.set_permissions(rolle, overwrite=perms)
                await ctx.guild.create_text_channel(f"{name_cat}", category=categori)
                await ctx.guild.create_voice_channel(f"{name_cat}", category=categori)
