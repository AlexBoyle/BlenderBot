#!/usr/bin/python3

#All code written by Rishabh Ekbote and Alex Boyle
#With special assistance from Gary, Tyler, Otto, Pat and Nick <3

import discord
import asyncio

from Global import *

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
client.run(Token)
