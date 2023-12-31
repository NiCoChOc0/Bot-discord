import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(AutoRole(bot))

class AutoRole(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Permet de faire un auto role (ajout du role quand on fait une réaction)
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild = self.bot.get_guild(payload.guild_id)
        role = discord.utils.get(guild.roles, name="Python")
        if payload.message_id == 777584117364686878 and payload.channel_id == 774937126864683018 and payload.emoji.name == "Python":
            await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        guild = self.bot.get_guild(payload.guild_id)
        role = discord.utils.get(guild.roles, name="Python")
        member = await self.bot.get_guild(payload.guild_id).fetch_member(payload.user_id)
        if payload.message_id == 777584117364686878 and payload.channel_id == 774937126864683018 and payload.emoji.name == "Python":
            await member.remove_roles(role)