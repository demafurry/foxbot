# -*- coding: utf-8 -*-
import config
import discord
import requests
import json
import random
import datetime
import time
import asyncio
import plyer
from discord.ext import commands
from memory_profiler import memory_usage
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord import utils
from discord.utils import get
import youtube_dl
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import os
import sys
import platform
import site
from os.path import join
import pafy
import psutil
import yt_search
import youtube_search
from youtube_search import YoutubeSearch
import colorama
import logging
import tkinter
from tkinter import *
import flask
from flask import Flask
import json
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix='>>', intents = discord.Intents.all())

bot.remove_command('help')

nowtime = datetime.datetime.now()
filename = "logs/" + str(nowtime.year) + "." + str(nowtime.month) + "." + str(nowtime.day) + " " + str(nowtime.hour) + "." + str(nowtime.minute) + "." + str(nowtime.second) + " main.log"
logging.basicConfig(filename=filename, filemode='w', format=u'%(name)s | %(levelname)s | %(message)s', level=logging.INFO)

@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.listening, name=">>help")
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    user = bot.get_user(677156845332332556)
    nowtime = datetime.datetime.now()
    logging.info('[' + str(nowtime.year) + '/' + str(nowtime.month) + '/' + str(nowtime.day) + ' ' + str(nowtime.hour) + ':' + str(nowtime.minute) + ':' + str(nowtime.second) + ']' + ' Бот ' + str(bot.user.name) + ' запущен.')
    await user.send('Бот ' + str(bot.user.name) + ' запущен.')

@bot.event
async def on_command_error(ctx, error):
    nowtime = datetime.datetime.now()
    logging.error(str('[' + str(nowtime.year) + '/' + str(nowtime.month) + '/' + str(nowtime.day) + ' ' + str(nowtime.hour) + ':' + str(nowtime.minute) + ':' + str(nowtime.second) + '] <' + str(ctx.guild.name) + '(' +str(ctx.guild.id) + ')> <' + str(ctx.channel.name) + '(' + str(ctx.channel.id) + ')> <' + str(ctx.author.name) + '#' + str(ctx.author.discriminator) + '(' + str(ctx.author.id) + ')> ' + str(error)))

@bot.event
async def on_guild_join(guild):
    user = bot.get_user(677156845332332556)
    await user.send("Бот " + str(bot.user.name) + " добавлен на сервер: " + str(guild.name))
    guildowner = guild.owner
    embed = discord.Embed(color = 0xffa500, title="FoxBot", description="Привет, `" + str(guildowner.name) + "`,спасибо что добавили меня на сервер `" + str(guild.name) + "`. Ниже расположена вся необходимая информация:\n:exclamation: Прежде чем использовать бота, желательно добавить на свой сервер роль `FoxAdminAccess` и выдать её нужным участникам(Советуем не выдавать данную роль не доверенным лицам, так-как они, в противном случае - смогут почти полностью управлять вашим сервером, что опасно). Просим выдать боту роль с максимальными правами, иначе бот может работать некорректно.\n:bangbang: Данного бота можно использовать во многих сценариях, но главным всё же остаётся РП.\n:anger: В случае неисправности, просим написать главному разработчику `demafurry#4811` и, желательно, подробно описать ошибку.\n:hotsprings: Данный бот написан на ЯП Python, все претензии к нему: :snake: , а не к разработчику. Если же вы считаете, что виноват *именно* ***разработчик***, а не :snake: , то писать тоже `demafurry#4811`.\n:globe_with_meridians: Бот в большинстве случаев использует чужое api из интернета, из-за которого иногда могут происходить ошибки.\n:white_check_mark: Для получения помощи, а именно, списка комманд для бота, напишите: `>>help` на сервере.")
    embed.set_footer(text="Fox 2020 | demafurry#4811")
    nowtime = datetime.datetime.now()
    logging.info('[' + str(nowtime.year) + '/' + str(nowtime.month) + '/' + str(nowtime.day) + ' ' + str(nowtime.hour) + ':' + str(nowtime.minute) + ':' + str(nowtime.second) + ']' + "Бот " + str(bot.user.name) + " добавлен на сервер: " + str(guild.name))
    await guildowner.send(embed=embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.event
async def on_command(ctx):
    nowtime = datetime.datetime.now()
    logging.info(str('[' + str(nowtime.year) + '/' + str(nowtime.month) + '/' + str(nowtime.day) + ' ' + str(nowtime.hour) + ':' + str(nowtime.minute) + ':' + str(nowtime.second) + '] <' + str(ctx.guild.name) + '(' +str(ctx.guild.id) + ')> <' + str(ctx.channel.name) + '(' + str(ctx.channel.id) + ')> <' + str(ctx.author.name) + '#' + str(ctx.author.discriminator) + '(' + str(ctx.author.id) + ')> ' + " Use command: " + str(ctx.message.content)))
    embed = discord.Embed(color = 0xffa500, title="FoxBot", description="Здравствуйте, приносим свои извинения за неполадки в работе бота. Мы не ожидали что наш бот будет стоять на большом кол-ве серверов, из-за чего идёт очень большая нагрузка. Мы вынуждены ограничить скорсть использования комманд до 10 секунд. Мы постараемся вскоре решить эту проблему. Приносим свои извинения. По всем вопросам - пишите разработчику: `demafurry#4811`")
    await ctx.channel.send(embed=embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@has_permissions(manage_messages=True)
@bot.event
async def on_command(ctx):
    await ctx.message.delete()

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def ping(ctx):
    testmsg = await ctx.send("Working...")
    await testmsg.delete()
    embed = discord.Embed(color = 0xffa500, title="Pong, " + str(ctx.author.name) + "!")
    embed.add_field(name="ws/API Latency:", value=str(round(bot.latency, 5)) + "s", inline=False)
    embed.add_field(name="Message Latency:", value=str(testmsg.created_at.microsecond - ctx.message.created_at.microsecond) + "ms", inline=False)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="Fox 2020 | demafurry#4811")
    await ctx.send(embed=embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def slap(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            randgif = random.randint(0, 14)
            imagegif = "https://kurobot.pw/gifs/slap/" + str(randgif) + ".gif"
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " дал(-а) пощёчину всем"
            else:
                embeddescription = str(ctx.author.mention) + " дал(-а) пощёчину " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Fox 2020 | demafurry#4811")
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Вы не можете выполнить данное действие.", color=0xffa500)
            embed.set_footer(text="Fox 2020 | demafurry#4811")
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Вы не можете выполнить данное действие.", color=0xffa500)
        embed.set_footer(text="Fox 2020 | demafurry#4811")
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def hug(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            randgif = random.randint(0, 14)
            imagegif = "https://kurobot.pw/gifs/hug/" + str(randgif) + ".gif"
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " обнял(-а) всех"
            else:
                embeddescription = str(ctx.author.mention) + " обнял(-а) " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Fox 2020 | demafurry#4811")
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Вы не можете выполнить данное действие.", color=0xffa500)
            embed.set_footer(text="Fox 2020 | demafurry#4811")
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Вы не можете выполнить данное действие.", color=0xffa500)
        embed.set_footer(text="Fox 2020 | demafurry#4811")
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def lick(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            randgif = random.randint(0, 14)
            imagegif = "https://kurobot.pw/gifs/lick/" + str(randgif) + ".gif"
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " лизнул(-а) всех"
            else:
                embeddescription = str(ctx.author.mention) + " лизнул(-а) " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Fox 2020 | demafurry#4811")
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Вы не можете выполнить данное действие.", color=0xffa500)
            embed.set_footer(text="Fox 2020 | demafurry#4811")
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Вы не можете выполнить данное действие.", color=0xffa500)
        embed.set_footer(text="Fox 2020 | demafurry#4811")
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def pet(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            randgif = random.randint(0, 14)
            imagegif = "https://kurobot.pw/gifs/pat/" + str(randgif) + ".gif"
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " погладил(-а) всех"
            else:
                embeddescription = str(ctx.author.mention) + " погладил(-а) " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Fox 2020 | demafurry#4811")
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Вы не можете выполнить данное действие.", color=0xffa500)
            embed.set_footer(text="Fox 2020 | demafurry#4811")
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Вы не можете выполнить данное действие.", color=0xffa500)
        embed.set_footer(text="Fox 2020 | demafurry#4811")
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def kiss(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            randgif = random.randint(0, 14)
            imagegif = "https://kurobot.pw/gifs/kiss/" + str(randgif) + ".gif"
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " поцеловал(-а) всех"
            else:
                embeddescription = str(ctx.author.mention) + " поцеловал(-а) " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Fox 2020 | demafurry#4811")
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Вы не можете выполнить данное действие.", color=0xffa500)
            embed.set_footer(text="Fox 2020 | demafurry#4811")
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Вы не можете выполнить данное действие.", color=0xffa500)
        embed.set_footer(text="Fox 2020 | demafurry#4811")
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def punch(ctx, arg:discord.Member="None"):
    bot = int(760437599524487189)
    argid = ctx.guild.get_member(arg)
    if argid != bot:
        if argid != ctx.author.id:
            randgif = random.randint(0, 14)
            imagegif = "https://kurobot.pw/gifs/punch/" + str(randgif) + ".gif"
            if arg == "None":
                embeddescription = str(ctx.author.mention) + " ударил(-а) всех"
            else:
                embeddescription = str(ctx.author.mention) + " ударил(-а) " + str(arg.mention)
            embed = discord.Embed(description=embeddescription, color=0xffa500)
            embed.set_footer(text="Fox 2020 | demafurry#4811")
            embed.set_image(url=imagegif)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error:", description="Вы не можете выполнить данное действие.", color=0xffa500)
            embed.set_footer(text="Fox 2020 | demafurry#4811")
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error:", description="Вы не можете выполнить данное действие.", color=0xffa500)
        embed.set_footer(text="Fox 2020 | demafurry#4811")
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def invitebot(ctx):
    embed = discord.Embed(title="Share this invite link | UwU", description="https://bit.ly/3kVIgEh/\nVK group: https://vk.com/foxbot_discord/", color=0xffa500)
    embed.set_footer(text="Fox 2020 | demafurry#4811")
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def randomfox(ctx):
    response = requests.get('https://randomfox.ca/floof/')
    json_data = json.loads(response.text)
    embed = discord.Embed(color = 0xffa500, title = 'Рандомная фотография лисы:')
    embed.set_footer(text="Fox 2020 | demafurry#4811")
    embed.set_image(url = json_data['image'])
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def randomdog(ctx):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    json_data = json.loads(response.text)
    embed = discord.Embed(color = 0xffa500, title = 'Рандомная фотография собаки:')
    embed.set_footer(text="Fox 2020 | demafurry#4811")
    embed.set_image(url = json_data['message'])
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def randomcat(ctx):
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    json_data = json.loads(response.text)
    json_data = json_data[0]
    embed = discord.Embed(color = 0xffa500, title = 'Рандомная фотография кошки:')
    embed.set_footer(text="Fox 2020 | demafurry#4811")
    embed.set_image(url = json_data['url'])
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed = embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def shipp(ctx, user1, user2):
    embed = discord.Embed(color = 0xffa500, description=str(ctx.author.mention) + " зашиперил " + str(user1) + " с " + str(user2))
    embed.set_footer(text="Fox 2020 | demafurry#4811")
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def user(ctx, user=None):
    if user == None:
        user = ctx.author
    elif user != None:
        user = ctx.guild.get_member(int(user[3:21]))
    if user.bot == True:
        botcheck = "(Bot)"
    elif user.bot == False:
        botcheck = ""
    authorroles = user.roles
    msgid = False
    statuseslist = {
        "online": "Онлайн",
        "idle": "Не активен",
        "dnd": "Не беспокоить",
        "offline": "Оффлайн"}
    monthslist = [
        "Янв",
        "Фев",
        "Март",
        "Апр",
        "Май",
        "Июнь",
        "Июль",
        "Авг",
        "Сент",
        "Окт",
        "Нояб",
        "Дек"]
    for role in range(len(authorroles)):
        if str(authorroles[role]) == "FoxAdminAccess":
            foxadminstatus = "Ok"
            embed = discord.Embed(color = 0xffa500, title=user.name + str(botcheck))
            embed.add_field(name="Пользователь:", value="Имя пользователя: **" + str(user.name) + "#" + str(user.discriminator) + "**\nID: **" + str(user.id) + "**\nСтатус: **" + str(statuseslist[str(user.status)]) + "**\nЗарегистрировался: **" + str(user.created_at.day) + " " + str(monthslist[int(user.created_at.month) - 1]) + ". " + str(user.created_at.year) + " г., " + str(user.created_at.hour) + ":" + str(user.created_at.minute) + ":" + str(user.created_at.second) + "**", inline=True)
            embed.add_field(name="Сервер:", value="Зашёл: **" + str(user.joined_at.day) + " " + str(monthslist[int(user.joined_at.month) - 1]) + ". " + str(user.joined_at.year) + " г., " + str(user.joined_at.hour) + ":" + str(user.joined_at.minute) + ":" + str(user.joined_at.second) + "**", inline=True)
            embed.add_field(name="FoxBot:", value="FoxAdminAccess: **" + str(foxadminstatus) + "**", inline=False)
            embed.set_footer(text="Fox 2020 | demafurry#4811")
            embed.set_thumbnail(url=user.avatar_url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            if msgid == False:
                if foxadminstatus == "Ok":
                    msgid = await ctx.send(embed=embed)
                else:
                    msgid = False
    if msgid == False:
        foxadminstatus = "Canceled"
        embed = discord.Embed(color=0xffa500, title=user.name + str(botcheck))
        embed.add_field(name="Пользователь:", value="Имя пользователя: **" + str(user.name) + "#" + str(user.discriminator) + "**\nID: **" + str(user.id) + "**\nСтатус: **" + str(statuseslist[str(user.status)]) + "**\nЗарегистрировался: **" + str(user.created_at.day) + " " + str(monthslist[int(user.created_at.month) - 1]) + ". " + str(user.created_at.year) + " г., " + str(user.created_at.hour) + ":" + str(user.created_at.minute) + ":" + str(user.created_at.second) + "**", inline=True)
        embed.add_field(name="Сервер:", value="Зашёл: **" + str(user.joined_at.day) + " " + str(monthslist[int(user.joined_at.month) - 1]) + ". " + str(user.joined_at.year) + " г., " + str(user.joined_at.hour) + ":" + str(user.joined_at.minute) + ":" + str(user.joined_at.second) + "**", inline=True)
        embed.add_field(name="FoxBot:", value="FoxAdminAccess: **" + str(foxadminstatus) + "**", inline=False)
        embed.set_footer(text="Fox 2020 | demafurry#4811")
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command()
async def server(ctx):
    nsfwchannelscount = 0
    memberscount = 0
    botscount = 0
    onlinememberscount = 0
    offlinememberscount = 0
    idlememberscount = 0
    dndmemberscount = 0
    for channel in range(len(ctx.guild.text_channels)):
        if ctx.guild.text_channels[channel].nsfw == True:
            nsfwchannelscount += 1
    for member in range(len(ctx.guild.members)):
        if ctx.guild.members[member].bot == False:
            memberscount += 1
        elif ctx.guild.members[member].bot == True:
            botscount += 1
    for member in range(len(ctx.guild.members)):
        if ctx.guild.members[member].bot == False:
            if ctx.guild.members[member].status == discord.Status.online:
                onlinememberscount += 1
            elif ctx.guild.members[member].status == discord.Status.offline:
                offlinememberscount += 1
            elif ctx.guild.members[member].status == discord.Status.idle:
                idlememberscount += 1
            elif ctx.guild.members[member].status == discord.Status.dnd:
                dndmemberscount += 1
    regionslist = {
        "brazil": ":flag_br: Brazil",
        "eu-central": ":flag_eu: Central Europe",
        "singapore": ":flag_sg: Singapore",
        "us-central": ":flag_us: U.S. Central",
        "sydney": ":flag_au: Sydney",
        "us-east": ":flag_us: U.S. East",
        "us-south": ":flag_us: U.S. South",
        "us-west": ":flag_us: U.S. West",
        "eu-west": ":flag_eu: Western Europe",
        "vip-us-east": ":flag_us: VIP U.S. East",
        "london": ":flag_gb: London",
        "amsterdam": ":flag_nl: Amsterdam",
        "hongkong": ":flag_hk: Hong Kong",
        "russia": ":flag_ru: Russia",
        "southafrica": ":flag_za:  South Africa"}
    verifylvlslist = {
        "none": "Без проверки",
        "low": "Низкий",
        "medium": "Ниже среднего",
        "high": "Средний",
        "table_flip": "Выше среднего",
        "extreme": "Высокий",
        "double_table_flip": "Выше высокого",
        "very_high": "Максимальный"}
    monthslist = [
        "Янв",
        "Фев",
        "Март",
        "Апр",
        "Май",
        "Июнь",
        "Июль",
        "Авг",
        "Сент",
        "Окт",
        "Нояб",
        "Дек"]
    embed = discord.Embed(color = 0xffa500, title=ctx.guild.name)
    embed.add_field(name="Участники:", value="Всего: **" + str(len(ctx.guild.members)) + "**\nУчастников: **" + str(memberscount) + "**\nБотов: **" + str(botscount) + "**", inline=True)
    embed.add_field(name="По статусам:", value=":green_circle: Онлайн: **" + str(onlinememberscount) + "**\n:crescent_moon: Не активен: **" + str(idlememberscount) + "**\n:no_entry: Не беспокоить: **" + str(dndmemberscount) + "**\n:black_circle: Оффлайн: **" + str(offlinememberscount) + "**", inline=True)
    embed.add_field(name="Каналы:", value="Всего: **" + str(len(ctx.guild.channels)) + "**\nТекстовых: **" + str(len(ctx.guild.text_channels)) + "**\nГолосовых: **" + str(len(ctx.guild.voice_channels)) + "**\nNSFW: **" + str(nsfwchannelscount) + "**", inline=False)
    embed.add_field(name="Владелец:", value=str(ctx.guild.owner), inline=True)
    embed.add_field(name="Регион:", value=str(regionslist[str(ctx.guild.region)]), inline=True)
    embed.add_field(name="Уровень проверки:", value=str(verifylvlslist[str(ctx.guild.verification_level)]), inline=True)
    embed.add_field(name="ID:", value=str(ctx.guild.id), inline=True)
    embed.add_field(name="Дата создания:", value=str(ctx.guild.created_at.day) + " " + str(monthslist[int(ctx.guild.created_at.month) - 1]) + ". " + str(ctx.guild.created_at.year) + " г., " + str(ctx.guild.created_at.hour) + ":" + str(ctx.guild.created_at.minute) + ":" + str(ctx.guild.created_at.second), inline=True)
    embed.set_footer(text="Fox 2020 | demafurry#4811")
    embed.set_thumbnail(url=ctx.guild.icon_url)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def avatar(ctx, user=None):
    if user == None:
        user = ctx.author
    elif user != None:
        user = bot.get_user(int(user[3:21]))
    embed = discord.Embed(color = 0xffa500, title="Аватар " + user.name + ":")
    embed.set_footer(text="Fox 2020 | demafurry#4811")
    embed.set_image(url=user.avatar_url)
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def say(ctx, *, message):
    authorroles = ctx.author.roles
    for role in range(len(authorroles)):
        if str(authorroles[role]) == "FoxAdminAccess":
            embed = discord.Embed(color = 0xffa500, title=str(ctx.author.name) + " говорит:", description=str(message))
            embed.set_footer(text="Fox 2020 | demafurry#4811")
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            msgid = await ctx.send(embed=embed)
            if message[0] == "!":
                end = False
                while end != True:
                    embed = discord.Embed(color = 0xffa500, title=str(ctx.author.name) + " говорит:", description="➟ " + str(message[1:len(message)]))
                    embed.set_footer(text="Fox 2020 | demafurry#4811")
                    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                    await msgid.edit(embed=embed)
                    await asyncio.sleep(0.5)
                    embed = discord.Embed(color=0xffa500, title=str(ctx.author.name) + " говорит:", description="➠ " + str(message[1:len(message)]))
                    embed.set_footer(text="Fox 2020 | demafurry#4811")
                    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                    await msgid.edit(embed=embed)
                    await asyncio.sleep(0.5)
            elif message[0] != "!":
                await msgid.edit(embed=embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def botinfo(ctx):
    botobj = ctx.guild.get_member(760437599524487189)
    allusers = 0
    allbots = 0
    textchannelscount = 0
    voicechannelscount = 0
    nsfwchannelscount = 0
    allofflineusers = 0
    allonlineusers = 0
    allidleusers = 0
    alldndusers = 0
    #for guild in range(len(bot.guilds)):
        #for user in range(len(bot.guilds[guild].members)):
            #if bot.guilds[guild].members[user].bot == False:
                #allusers += 1
            #elif bot.guilds[guild].members[user].bot == True:
                #allbots += 1
    #for guild in range(len(bot.guilds)):
        #for user in range(len(bot.guilds[guild].members)):
            #if bot.guilds[guild].members[user].bot == False:
                #if bot.guilds[guild].members[user].status == discord.Status.offline:
                    #allofflineusers += 1
                #elif bot.guilds[guild].members[user].status == discord.Status.online:
                    #allonlineusers += 1
                #elif bot.guilds[guild].members[user].status == discord.Status.idle:
                    #allidleusers += 1
                #elif bot.guilds[guild].members[user].status == discord.Status.dnd:
                    #alldndusers += 1
    for guild in range(len(bot.guilds)):
        for channel in range(len(bot.guilds[guild].text_channels)):
            textchannelscount += 1
    for guild in range(len(bot.guilds)):
        for channel in range(len(bot.guilds[guild].voice_channels)):
            voicechannelscount += 1
    for guild in range(len(bot.guilds)):
        for channel in range(len(bot.guilds[guild].text_channels)):
            if bot.guilds[guild].text_channels[channel].nsfw == True:
                nsfwchannelscount += 1
    monthslist = [
        "Янв",
        "Фев",
        "Март",
        "Апр",
        "Май",
        "Июнь",
        "Июль",
        "Авг",
        "Сент",
        "Окт",
        "Нояб",
        "Дек"]
    osnameslist = {
        "posix": "POSIX",
        "nt": "Windows NT",
        "ce": "Windows CE",
        "os2": "OC2",
        "riscos": "RISC OS",
        "ibmi": "IBM",
        "java": "Jython"}
    ossysplatformslist = {
        "linus": "Linux",
        "win32": "Windows API",
        "cygwin": "Cugwin",
        "darwin": "Darwin"}
    totalram = (psutil.virtual_memory().total / 1000) / 1024
    embed = discord.Embed(color = 0xffa500, title="Информация о боте:")
    embed.add_field(name="Главное:", value="Имя пользователя: **" + str(bot.user.name) + "#" + str(bot.user.discriminator) + "**\nID: **" + str(bot.user.id) + "**\nАккаунт создан: **" + str(botobj.created_at.day) + " " + str(monthslist[int(botobj.created_at.month) - 1]) + ". " + str(botobj.created_at.year) + " г., " + str(botobj.created_at.hour) + ":" + str(botobj.created_at.minute) + ":" + str(botobj.created_at.second) + "**\nБот зашёл на данный сервер: **" + str(botobj.joined_at.day) + " " + str(monthslist[int(botobj.joined_at.month) - 1]) + ". " + str(botobj.joined_at.year) + " г., " + str(botobj.joined_at.hour) + ":" + str(botobj.joined_at.minute) + ":" + str(botobj.joined_at.second) + "**", inline=True)
    embed.add_field(name="Сервера:", value="Кол-во серверов: **" + str(len(bot.guilds)) + "**\nКол-во текстовых каналов: **" + str(textchannelscount) + "**\nКол-во голосовых каналов: **" + str(voicechannelscount) + "**\nКол-во NSFW каналов: **" + str(nsfwchannelscount) + "**", inline=True)
    #embed.add_field(name="Пользователи:", value="Кол-во пользователей: **" + str(allusers) + "**\nОнлайн: **" + str(allonlineusers) + "**\nНе активен: **" + str(allidleusers) + "**\nНе беспокоить: **" + str(alldndusers) + "**\nОффлайн: **" + str(allofflineusers) + "**\nКол-во ботов: **" + str(allbots) + "**", inline=False)
    embed.add_field(name="Системная информация:", value="RAM usage: **" + str(round(memory_usage()[0], 3)) + "/" + str(round(totalram, 3)) + "mb**\nOperating system family: **" + str(osnameslist[str(os.name)]) + "**\nOperating system platform: **" + str(ossysplatformslist[str(os.sys.platform)]) + "**\nProcessor: **" + str(platform.processor()) + "**\nOperating system: **" + str(platform.system()) + " " + str(platform.release()) + "**\nMachine: **" + str(platform.machine()) + "**\nArchitecture: **" + str(platform.architecture()[0]) + " | " + str(platform.architecture()[1]) + "**", inline=False)
    embed.set_thumbnail(url=bot.user.avatar_url)
    embed.set_footer(text="Fox 2020 | demafurry#4811")
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

connections = {}

voice_client = None

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def mplay(ctx, *, url="august"):
    guild = ctx.message.guild 
    member = ctx.message.author
    guild_id = guild.id
    voice = member.voice
    
    if "youtu.be" in url:
        videou = pafy.new(url)
        url = pafy.new(url).getbestaudio().url_https
    elif "youtube.com" in url:
        videou = pafy.new(url)
        url = pafy.new(url).getbestaudio().url_https
    elif "youtube.ru" in url:
        videou = pafy.new(url)
        url = pafy.new(url).getbestaudio().url_https
    elif "youtube.de" in url:
        videou = pafy.new(url)
        url = pafy.new(url).getbestaudio().url_https
    elif "youtube.co.uk" in url:
        videou = pafy.new(url)
        url = pafy.new(url).getbestaudio().url_https
    elif "youtube.fr" in url:
        videou = pafy.new(url)
        url = pafy.new(url).getbestaudio().url_https
    else:
        videos = YoutubeSearch(str(url), max_results=2).to_dict()
        url = videos[0]
        url = url.get("id")
        videou = "https://youtu.be/" + str(url)
        videou = pafy.new(videou)
        url = pafy.new(url).getbestaudio().url_https

    if not voice:
        embed = discord.Embed(color = 0xffa500, title="Error:", description="You did not connected to any voice channel yet.")
        embed.set_footer(text="Fox 2020 | demafurry#4811")
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        return await ctx.send(embed=embed)

    voice_channel = voice.channel

    if guild_id not in connections:
        connections[guild_id] = voice_client = await voice_channel.connect()
    else:
        voice_client = connections.get(guild_id)

    if voice_client.is_playing():
        voice_client.stop()
    FFMPEG = { 'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn', }
    voice_client.play(discord.FFmpegPCMAudio(url, **FFMPEG))
    embed = discord.Embed(color = 0xffa500, title="FoxBot Music")
    embed.add_field(name="Видео: ", value="Название: **" + str(videou.title) + "**\nПросмотров: **" + str(videou.viewcount) + "**\nПродолжительность: **" + str(videou.duration) + "**", inline=False)
    embed.set_image(url=str(videou.bigthumb))
    embed.set_footer(text="Fox 2020 | demafurry#4811")
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def mstop(ctx):
    guild = ctx.guild
    guild_id = guild.id
    if guild_id in connections:
        connections.get(guild_id).stop()
        embed = discord.Embed(color = 0xffa500, title="FoxBot Music", description="Музыка остановлена")
        embed.set_footer(text="Fox 2020 | demafurry#4811")
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def mleave(ctx):
    guild = ctx.guild
    guild_id = guild.id
    if guild_id in connections:
        connections.get(guild_id).stop()
        await connections.get(guild_id).disconnect()
        del connections[guild_id]
        embed = discord.Embed(color = 0xffa500, title="FoxBot Music", description="Бот вышел из голосового канала")
        embed.set_footer(text="Fox 2020 | demafurry#4811")
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

@commands.cooldown(1, 10, commands.BucketType.user)
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(color=0xffa500, title="Commands list:", description="Реакция Дать пощёчину:\n"
        "```>>slap {user}```Реакция Ударить:\n"
        "```>>punch {user}```Реакция Обнять:\n"
        "```>>hug {user}```Реакция Погладить:\n"
        "```>>pet {user}```Реакция Поцеловать:\n"
        "```>>kiss {user}```Реакция Лизнуть:\n"
        "```>>lick {user}```Показать пинг бота:\n"
        "```>>ping```Показать ссылку для приглашения бота:\n"
        "```>>invitebot```Показать доступные команды:\n"
        "```>>help```Рандомная фотография лисы:\n"
        "```>>randomfox```Рандомная фотография собаки:\n"
        "```>>randomdog```Рандомная фотография кота:\n"
        "```>>randomcat```Зашиперить:\n"
        "```>>shipp {user1} {user2}```Информация о участнике:\n"
        "```>>user {user}```Информация о сервере:\n"
        "```>>server```Аватар участника:\n"
        "```>>avatar {user}```Сказать что-либо от имени бота(Только для роли `FoxAdminAccess`):\n"
        "```>>say {text( ! - В начале, чтобы выделить анимацией ➟➠ )}```Информация о боте:\n"
        "```>>botinfo```Включить музыку(YouTube, nsfw контент игнорируется, может не сработать с 1 раза):\n"
        "```>>mplay {url | search}```Выключить музыку:\n"
        "```>>mstop```Выгнать бота из голосового чата:\n"
        "```>>mleave```")
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="Fox 2020 | demafurry#4811")
    await ctx.send(embed=embed)

bot.run(config.TOKEN)