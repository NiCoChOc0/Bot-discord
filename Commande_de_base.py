import discord
from discord.ext import commands

class CommandeDeBase(commands.Cog):
    def __init__ (self, bot):
        self.bot = bot

    # petite conversation avec le bot
    @commands.command()
    async def coucou(self, ctx):
        await ctx.send("Coucou !")
        await ctx.send("Comment allez vous ?")

    # Récupère des stats du serveur
    @commands.command()
    async def serveurInfo(self, ctx):
        server = ctx.guild
        serverName = server.name
        nbTextChannel = len(server.text_channels)
        nbVoiceChannel = len(server.voice_channels)
        serverDescription = server.description
        nbPerson = server.member_count
        message = f"Le serveur **{server.name}** à *{nbPerson} personnes*.\nLa description du serveur {serverDescription}.\nLe serveur possède {nbTextChannel} channels textuels et {nbVoiceChannel} channels vocaux"
        await ctx.send(message)

    # Le bot répète ce que tu dis
    @commands.command()
    async def say(self, ctx, *text):
        await ctx.send(" ".join(text))

    # Ecriture dans un style chinois
    @commands.command()
    async def chinese(self, ctx, *text):
        chineseChar = "丹书匚刀巳下呂廾工丿片乚爪冂口尸Q尺丂丁凵V山乂Y乙"
        chineseText = []
        for word in text:
            for char in word:
                char = char.lower()
                if char.isalpha():
                    index = ord(char) - ord("a")  # Position ascci du char
                    charTransformed = chineseChar[index]
                    chineseText.append(charTransformed)
                else:
                    chineseText.append(char)
            chineseText.append(" ")
        await ctx.send("".join(chineseText))