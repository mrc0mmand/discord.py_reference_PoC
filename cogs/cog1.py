import discord
from discord.ext import commands

class Cog1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def group1(self, ctx):
        await ctx.send("group1")

    @group1.command()
    async def command_g1(self, ctx):
        await ctx.send("command from Cog1")

def setup(bot):
    bot.add_cog(Cog1(bot))
