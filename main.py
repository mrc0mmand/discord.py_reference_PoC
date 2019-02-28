#!/usr/bin/env python3

import discord
import sys
from discord.ext import commands
from discord.ext.commands import Bot

enabled_exts = [
    "cogs.cog1",
    "cogs.cog2"
]

bot = Bot(description="TestBot", command_prefix=".")

for ext in enabled_exts:
    bot.load_extension(ext)


bot.run("1234")
