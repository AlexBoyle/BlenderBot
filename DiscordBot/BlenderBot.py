#!/usr/bin/python3

#All code written by Alex Boyle and Rishabh Ekbote
#With special assistance from Gary, Tyler, Otto, Pat and Nick <3

from Commands.WeatherCommands import *
from Commands.TermCommands import *
from Commands.ImageRand import *
from Global import *
from Utility import *

import discord
import asyncio
import datetime

commands = [
    {"sym":'-', "file":(ImageRandom()), "desc":'(NSFW)Generate Random Imgur links',"exclusive":False},
    {"sym":'!', "file":(TermCommands), "desc":'Commands to easily look up our Terms and Conditions',"exclusive":True},
    {"sym":'+', "file":(Weather()), "desc":'Commands to quickly look up the weather in your area',"exclusive":False}
]
exclusive = {}
start_time = datetime.datetime.now()
messages = 0

client = discord.Client()

@client.event
async def on_ready():
    client.change_presence()
    util = Utility()
    server_ids = util.get_server_ids()
    for command in commands:
        if(command['exclusive']):
            arr = {}
            for server_id in server_ids:
                arr[server_id] = command['file']('test')
            exclusive[command['sym']] = arr

@client.event
async def on_message(message):
    #messages += 1
    out = ''
    for command in commands:
        if message.content.startswith(command['sym']):
            if(command['exclusive']):
                out = exclusive[command['sym']][str(message.server.id)].run(message)
            else:
                out = command['file'].run(message)
            if out != None:
                await client.send_message(message.channel,out)
    #Bot Information
    if (('help' in message.content.lower()) and (botid in message.content.lower())):
        out = ''
        out += "```\n"
        out += "@BlenderBot info - Info about Blender Bot\n"
        for command in commands:
            out += command['sym'] + "help -" + command['desc'] + "\n"
        out += "```"
        await client.send_message(message.channel,out)
    if (('info' in message.content.lower()) and (botid in message.content.lower())):
        out = (
            "```\n"
            "Blender Bot:\n  This Bot was written by Alex Boyle and Rishabh Ekbote\nwith special "
            "assistance from Gary, Tyler, Otto, Pat and Nick <3\n\n  This bot is open source "
            "(github linked below). If you choose to use any files or major code blocks from this "
            "project, accreditation is appreciated."
            "``` https://github.com/AlexBoyle/Spicier_Bot (link to be updated)"
        )
        await client.send_message(message.channel,out)
    if (('status' in message.content.lower()) and (botid in message.content.lower())):
        out = (
            ""
        )
        await client.send_message(message.channel,out)

if __name__ == '__main__':
    client.run(Token)
