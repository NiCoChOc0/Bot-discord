import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(AutoClear(bot))

class AutoClear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Permet de supprimmer automatiquement un message et de le renvoyer dans un channel
    @commands.Cog.listener('on_message')
    async def auto_supp_renvoie_message(self, message):
        channelId = message.channel.id
        if channelId == 777478533773000756:
            channelGuild = message.guild.channels
            for channell in range(len(channelGuild)):
                channelTest = channelGuild[channell]
                if 779649162513219584 == channelTest.id:
                    await channelTest.send(f"{message.author}/{message.author.mention} : \n{message.content}")
                    await message.delete()

    # Deux commandes qui permettent de supprimer un nombre choisi (nb) de message
    @commands.command()
    async def clear(self, ctx, nb=2):
        await ctx.channel.purge(limit=nb+1)

    @commands.command()
    async def clear2(self, ctx, nb=2):
        await ctx.message.delete()