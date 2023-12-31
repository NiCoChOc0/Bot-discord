import discord
from discord.ext import commands

class BanKick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Commande pour kick une personne du serveur 
    @commands.command()
    @commands.has_role('admin') # Seul les personnes avec le role "admin" peuvent l'utiliser
    async def kick(self, ctx, user: discord.User, reason):
        reason = " ".join(reason)
        await ctx.guild.kick(user, reason=reason)
        await ctx.send(f"{user} à été kick")

    # Si la syntaxe de la commande kick est pas bonne, le bot envoie un message pour donner la syntaxe
    @kick.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("il faut écrire : !kick @pesudo une raison de kick")

    # Comande pour ban
    @commands.command()
    @commands.has_role('admin')
    async def ban(self, ctx, user: discord.User, *reason):
        reason = " ".join(reason)
        await ctx.guild.ban(user, reason=reason)
        await ctx.send(f"{user} à été ban")

    @ban.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("il faut écrire : !ban @pesudo une raison de kick")
            
    #Commande pour unban
    @commands.command()
    @commands.has_role('admin')
    async def unban(self, ctx, user, *reason):
        reason = " ".join(reason)
        userName, idUser = user.split("#")
        bannedUsers = await ctx.guild.bans()
        for User in bannedUsers:
            if User.user.name == userName and User.user.discriminator == idUser:
                await ctx.guild.unban(User.user, reason=reason)
                await ctx.send(f"{user} à été unban")
        else:
            await ctx.send(f"{user} n'existe pas dans la liste bans")

    @unban.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("il faut écrire : !unban @pesudo une raison de kick")
