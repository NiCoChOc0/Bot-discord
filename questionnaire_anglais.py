import discord
from discord.ext import commands
import random

class Questionnaire(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    # Un petit jeu de questionnaire (pas du tout optimisé et très mal fait)
    @commands.command()
    async def questionnaire(self, ctx):

        nb_question_pose = -1
        score =0
        dico_anglais = {"household": "foyer", "on her laps": "sur ses genoux", "armchair": "fauteuil",
                        "a laptop": "un ordinateur portable", "a doll": "une poupée", "leaning over": "pencher sur",
                        "laying the table": "mettre la table", "to hang on": "accrocher sur", "above": "au-dessus",
                        "shallow": "superficiel", "lay": "poser",
                        "make smb aware of smth": "attirer l'attention de qqn avec qqch",
                        "want smb to +BV": "vouloir qqch de qqn", "the waist": "taille", "wear": "porter",
                        "clothes": "habits", "tight": "moulant", "loose": "ample", "weight": "poids",
                        "figure": "silhouette", "a ladder": "une echelle", "pay attention to": "etre attentif à",
                        "a suit": "un costume", "a costume": "un deguisement", "labour market": "marché du travaille",
                        "a tie": "une cravate", "both": "chacun", "a brief case": "une malette",
                        "confident": "confient en lui même", "worried": "inquiet"}
        player = ctx.message.author
        for index in range(len(ctx.guild.members)):
            if player == ctx.message.guild.members[index]:
                for i in range(10):

                    mot = list(dico_anglais)
                    Index = random.randint(0, len(mot) - (
                                2 + nb_question_pose))
                    mot_choisi = mot[Index]
                    reponse = dico_anglais[mot_choisi]

                    await ctx.send(f"Traduit : {mot_choisi}")
                    rep = await self.bot.wait_for('message')

                    if rep.content == reponse:
                        await ctx.send("bien joué, t'es le meilleur")
                        score +=1
                    else:
                        await ctx.send(f"t'es con ou quoi c'était: {reponse}" )

                    del dico_anglais[mot_choisi]
        await ctx.send(f"Le questionnaire est fini. Tu as {score} bonne(s) réponse(s)")

    @questionnaire.error
    async def on_command_error(self, ctx, error):
        print(error)
