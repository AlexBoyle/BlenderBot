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

commands = [
    {"sym":'$', "file":(GifCommands), "desc":'Commands to get reaction gifs'},
    {"sym":'!', "file":(TermCommands), "desc":'Commands to easily look up our Terms and Conditions'},
    {"sym":'+', "file":(WeatherCommands), "desc":'Commands to quickly look up the weathe rin your area'}
]

@client.event
async def on_message(message):
    out = ''
    for command in commands:
        if message.content.startswith(command['sym']):
            out = command['file'].run(message.content[1:])
            if out != None:
                await client.send_message(message.channel,out)
    #help
    if (('help' in message.content.lower()) and (botid in message.content.lower())):
        out += "```\n"
        for command in commands:
            out += command['sym'] + "help -" + command['desc'] + "\n"
        out += "```"
        await client.send_message(message.channel,out)
    #Greeting
    if (('hello' in message.content.lower()) or ('hi' in message.content.lower())) and botid in message.content.lower():
        await client.send_message(message.channel,'Hello, <@!%s>!' % (message.author.id))
    #Random Image from imgur
    if 'random' in message.content.lower() and ('image' in message.content.lower() or 'pic' in message.content.lower()) and ('please' in message.content.lower() or 'pls' in message.content.lower()):
        out = ImgRand.genLink()
        await client.send_message(message.channel,out)
    #Random NSFW Image
    if message.content.lower() == "i am a filthy boy who needs an nsfw image" or message.content.lower() == "i am a filthy girl who needs an nsfw image":
        out = ImgRand.dirtyimage()
        await client.send_message(message.channel,out)

client.run(Token)
