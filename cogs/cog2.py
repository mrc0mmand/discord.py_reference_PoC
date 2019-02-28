import discord
from discord.ext import commands
from .cog1 import Cog1

class Cog2(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog1.group1.command()
    async def command_g2(self, ctx):
        await ctx.send("command from Cog2")

def setup(bot):
    bot.add_cog(Cog2(commands.Cog))
