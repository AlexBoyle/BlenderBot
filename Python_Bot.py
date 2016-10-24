#!/usr/bin/python3
 
import discord
import asyncio
import logging
import commands


client = discord.Client()

@client.event
async def on_message(message):

    #reference term by number
    if message.content.startswith('!t '):
        await client.send_message(message.channel, commands.term(message.content[3:]))

    #search through terms
    if message.content.startswith('!ts '):
        await client.send_message(message.channel, commands.termSearch(message.content[4:]))

    #recall 5 most recent terms
    if message.content == '!r' :
        await client.send_message(message.channel,  commands.recent())

    #link to t&c
    if message.content == '!link' :
        await client.send_message(message.channel, 'http://bit.do/termcon')

    if message.content == '!help' :
        await client.send_message(message.channel, message.channel,commands.help())


client.run('buymyasianbaby@gmail.com','suchpassword1')
