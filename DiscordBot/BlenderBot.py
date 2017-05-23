#!/usr/bin/python3.5

#All code written by Rishabh Ekbote and Alex Boyle
#With special assistance from Gary, Tyler, Otto, Pat and Nick <3

import discord
import asyncio

from Global import *

import Commands.TermCommands as TermCommands
import Commands.GifCommands as GifCommands
import Commands.ImgRand as ImgRand
import Commands.WeatherCommands as WeatherCommands

client = discord.Client()

@client.event
async def on_ready():
	''

@client.event
async def on_message(message):

    #Gif Commands
    if message.content.startswith('$'):
        out = GifCommands.gifs(message)
        if out != None:
            await client.send_message(message.channel,out)

    #Terms and conditions commands
    if message.content.startswith('!'):
        out = TermCommands.terms(message)
        if out != None:
            await client.send_message(message.channel,out)

    #Weather commands
    if message.content.startswith('+'):
        out = WeatherCommands.weather(message)
        if out != None:
            await client.send_message(message.channel,out)
    #Greeting
    if (('hello' in message.content.lower()) or ('hi' in message.content.lower())) and botid in message.content.lower():
        await client.send_message(message.channel,'Hello, <@!%s>!' % (message.author.id))
    #Random Image from imgur
    if 'random image' in message.content.lower() and ('please' in message.content.lower() or 'pls' in message.content.lower()):
        out = ImgRand.imgrand(ImgRand.options)
        await client.send_message(message.channel,out)
    #Random NSFW Image
    if message.content.lower() == "i am a filthy boy who needs an nsfw image" or message.content.lower() == "i am a filthy girl who needs an nsfw image":
        out = ImgRand.dirtyimage()
        await client.send_message(message.channel,out)

client.run(Token)
