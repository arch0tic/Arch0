import discord
from ip2geotools.databases.noncommercial import DbIpCity
import nmap3
import os
import subprocess
import requests
import json
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

bot = discord.Bot()
@bot.command(description="Sends the bot's latency.")
async def arch(ctx): 
    await ctx.respond(f"# Arch Linux is the best distro ever")
@bot.command(description="Inspiring quote")
async def inspire(ctx):
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]["q"]
    await ctx.respond(quote)
@bot.event
async def on_message(message):
    if(message.content.startswith('inspire')):
        print("yes")
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]["q"]
        await message.channel.send(quote)
@bot.event
async def on_ready():
    activity = discord.Game(name="Arch BTW!")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
bot.run("MTE0ODI1MjY4MDU2NTgyMTUwMA.GDX9QH.EU4aFYHblRkiaRQM-7aMwtZIv8DOc4lCDhKWBM")
