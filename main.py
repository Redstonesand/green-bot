import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

sampah_organik=["buah","daun"]
sampah_anorganik=["plastik"]

@bot.command()
async def pilih(ctx,sampah):
    if sampah in sampah_organik:
        await ctx.send("masukkan ke dalam organik")
    if sampah in sampah_anorganik:
        await ctx.send("masukan ke dalam anorganik")
bot.run("You bot token here")
