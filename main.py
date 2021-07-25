#!/usr/bin/env python3

import discord
import requests
from bs4 import BeautifulSoup
from discord.ext.commands import Bot

from config import CONFIG
from help import HELP

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

@bot.command(name = 'manga', help = HELP['manga'])
async def manga(ctx, manga_number):
    url = f"https://readm.org/manga/{manga_number}"
    page = requests.get(url)
    html_text = page.text
    soup = BeautifulSoup(html_text, 'lxml')

    media_meta = soup.find_all('div', class_ = "media-meta")[0]
    SUMMARY = soup.find_all('div', class_ = "series-summary-wrapper")[0]

    manga_name = soup.h1.string

    manga_cover = f"https://readm.org/{soup.find_all('img', class_ = 'series-profile-thumb')[0].get('src')}"

    # manga_description = SUMMARY.find_all('p', id = "")[0].string

    genres_list = []
    for a in SUMMARY.find_all('a'):
        genres_list.append(a.string)
    genres = ", ".join(genres_list)

    first_chapter = media_meta.find_all('a')[0].get('title').split()[-1]

    last_chapter = soup.find_all('a', class_ = 'item active')[-1]
    last_chapter = str(last_chapter).split()[-4]

    embed_var = discord.Embed(title = manga_name, url = url, color = 0X19A6FF)
    embed_var.set_thumbnail(url = manga_cover)
    embed_var.add_field(name = "Genres:", value = genres, inline=False)
    embed_var.add_field(name = "First chapter:", value = first_chapter)
    embed_var.add_field(name = "Last chapter:", value = last_chapter)
    await ctx.send(embed = embed_var)

bot.run(CONFIG['token'])
