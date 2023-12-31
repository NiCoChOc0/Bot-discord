# Importation des bibliothèques
import discord
from discord.ext import commands
from discord import app_commands
from keep_alive import keep_alive

# Création du bot avec ses statues 
activity = discord.Game(name="Prêt pour jouer !")
bot = commands.Bot(command_prefix = "!", description="Bot de NiCoChOcO", intents=discord.Intents.all(), activity=activity)

# Vérification dès que le bot est lancé
@bot.event
async def on_ready():
    print("Ready !")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

# Commande de test
@bot.tree.command(name="say")
@app_commands.describe(thing_to_say = "What should the bot gonna say")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(thing_to_say)

# Création d'une todo
@bot.tree.command(name="createtodo")
@app_commands.describe(title="Title of the ToDo list", description="Description of the ToDo list")
async def createtodo(interaction: discord.Interaction, title: str, description: str):
    todo_embed = discord.Embed(description=description, title=title, type="article", colour=discord.Colour.blue())

    todo_embed.set_thumbnail(url=interaction.user.display_avatar.url)
    todo_embed.set_author(name=f'{interaction.user.name}#{interaction.user.discriminator}')

    await interaction.response.send_message(embed=todo_embed)

@bot.tree.command(name="give_console_info")
async def give_console_info(interaction: discord.Interaction):
    await interaction.response.send_message(type(interaction.user.name))



# Ecrit un message si la personne qui écrit une commande n'a pas un rôle qui lui permet
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("Tu n'as pas la permition d'utiliser cette commande")
    else:
        await ctx.send(f"Il y a une erreur inconnue : {error}")









# Lancement du bot + code pour qu'un hébergeur en ligne puisse le maintenir connecté
#keep_alive() A DECOMMENTERS
bot.run("Nzc0OTEyNzQyNjIwMDA0MzYz.X6eruw.qKqiQXRRmD23wjjTUnCbDnH-QKM")