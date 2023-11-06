import discord
from ip2geotools.databases.noncommercial import DbIpCity
import nmap3
import os
import subprocess

bot = discord.Bot()

# we need to limit the guilds for testing purposes
# so other users wouldn't see the command that we're testing

@bot.command(description="Sends the bot's latency.") # this decorator makes a slash command
async def arch(ctx): # a slash command will be created with the name "ping"
    await ctx.respond(f"# Arch Linux is the best distro ever")
@bot.command(description="declaratie de dragoste dragului nostru prieten Valentin")
async def vali(ctx):
    await ctx.respond("# <@886986362262286357> SUGE PULA LA TOT SERVERU")
bot.run("MTE0ODI1MjY4MDU2NTgyMTUwMA.GDX9QH.EU4aFYHblRkiaRQM-7aMwtZIv8DOc4lCDhKWBM")
