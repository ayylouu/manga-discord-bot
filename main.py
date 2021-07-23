#!/usr/bin/env python3

import json
import discord
import requests
from bs4 import BeautifulSoup
from discord.ext.commands import Bot

CONFIG_FILE = open('config.json', 'r')
CONFIG = json.load(CONFIG_FILE)
HELP = CONFIG['commands']
bot = Bot(command_prefix = CONFIG['prefix'])

@bot.event
async def on_ready():
    print("Ready!")
    await bot.user.edit(username = CONFIG['name'])

@bot.command(name = 'read', help = HELP['read'])
async def read(ctx, manga_number, chapter_number):
    url = f"https://readm.org/manga/{manga_number}/{chapter_number}/all-pages"
    page = requests.get(url)
    html_text = page.text
    soup = BeautifulSoup(html_text, 'lxml')
    page_number = 1
    for image in soup.find_all('img', class_ = 'img-responsive scroll-down'):
        embed_var = discord.Embed(title = f"{manga_number}", description = f"page {page_number}")
        embed_var.set_image(url=f"https://readm.org{image.get('src')}")
        await ctx.send(embed = embed_var)
        page_number += 1

bot.run(CONFIG['token'])
