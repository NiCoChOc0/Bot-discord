# Importation des bibliothèques
import discord
from discord.ext import commands
from discord.utils import get
import Commande_de_base
import autoClear
import autoRole
import ban_kick
import creation_categorie
import membre_rejoit
import questionnaire_anglais
from keep_alive import keep_alive

# Création du bot avec ses statues 
intents = discord.Intents.default()
intents.members = True
activity = discord.Game(name="troll Cheiik")
bot = commands.Bot(command_prefix = "!", description="Bot de NiCoChOcO", intents=discord.Intents.all(), activity=activity)

# Vérification dès que le bot est lancé
@bot.event
async def on_ready():
    print("bot prêt !")

# Ecrit un message si la personne qui écrit une commande n'a pas un rôle qui lui permet
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("Tu n'as pas la permition d'utiliser cette commande")

# Les cog sont les bibliothèques mais qu'il faut préciser au bot pour qu'il les utilise (c'est peut être propre au python)

bot.add_cog(Commande_de_base.CommandeDeBase(bot))
bot.add_cog(autoClear.AutoClear(bot))
bot.add_cog(autoRole.AutoRole(bot))
bot.add_cog(ban_kick.BanKick(bot))
bot.add_cog(creation_categorie.CreationCategorie(bot))
bot.add_cog(membre_rejoit.OnMember(bot))
bot.add_cog(questionnaire_anglais.Questionnaire(bot))


# Lancement du bot + code pour qu'un hébergeur en ligne puisse le maintenir connecté
#keep_alive()
bot.run("Nzc0OTEyNzQyNjIwMDA0MzYz.X6eruw.qKqiQXRRmD23wjjTUnCbDnH-QKM")