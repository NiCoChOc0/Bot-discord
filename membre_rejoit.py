import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(OnMember(bot))

class OnMember(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Ecrit un message à l'arriver d'une personne
    @commands.Cog.listener()
    async def on_member_join(self, member):
        list_channel = member.guild.channels
        for channel in range(len(list_channel)):
            if list_channel[channel].id == 774937126864683018:
                channel_language = list_channel[channel]
            if list_channel[channel].id == 779654138018660354:
                channel_bienvenue = list_channel[channel]
                print(channel_bienvenue)

        await channel_bienvenue.send(f"Bienvenue à toi {member.mention}, n'hésites pas à jeter un oeuil à {channel_language.mention}")