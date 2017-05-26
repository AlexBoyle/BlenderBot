#!/usr/bin/python3

#All code written by Rishabh Ekbote and Alex Boyle
#With special assistance from Gary, Tyler, Otto, Pat and Nick <3

import Commands.GifCommands as GifCommands
import Commands.ImgRand as ImgRand
import Commands.WeatherCommands as WeatherCommands
from Commands.TermCommands import *

import discord
import asyncio

from Global import *

commands = [
    {"sym":'', "file":(ImgRand), "desc":'(NSFW)Generate Random Imgur links',"exclusive":False},
    {"sym":'$', "file":(GifCommands), "desc":'(WIP)Commands to get reaction gifs',"exclusive":False},
    {"sym":'!', "file":(TermCommands('test')), "desc":'(WIP)Commands to easily look up our Terms and Conditions',"exclusive":True},
    {"sym":'+', "file":(WeatherCommands), "desc":'(WIP)Commands to quickly look up the weather in your area',"exclusive":False}
]

client = discord.Client()

@client.event
async def on_ready():
    for server in client.servers:
        print(server)

@client.event
async def on_message(message):
    out = ''
    for command in commands:
        if message.content.startswith(command['sym']):
            out = command['file'].run(message)
            if out != None:
                await client.send_message(message.channel,out)
    if (('help' in message.content.lower()) and (botid in message.content.lower())):
        out = ''
        out += "```\n"
        out += "@BlenderBot info - Info about Blender Bot\n"
        for command in commands:
            out += command['sym'] + "help -" + command['desc'] + "\n"
        out += "```"
        await client.send_message(message.channel,out)
    if (('info' in message.content.lower()) and (botid in message.content.lower())):
        out = ''
        out += "```\n"
        out += "Blender Bot:\n  This Bot was written by Alex Boyle and Rishabh Ekbote\nwith special assistance from Gary, Tyler, Otto, Pat and Nick <3\n\n  This bot is open source (github linked below). If you choose to use any files or major code blocks from this project, accreditation is appreciated."
        out += "``` https://github.com/AlexBoyle/Spicier_Bot (link to be updated)"
        await client.send_message(message.channel,out)
client.run(Token)
