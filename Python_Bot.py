#!/usr/bin/python3
 
import discord
import asyncio
import logging
import commands

############################################################################################
client = discord.Client()
 
@client.event
async def on_message(message):
   
    #reference term by number
    if message.content.startswith('!t '):
        term(message.content[3:])
       
    #search through terms
    if message.content.startswith('!ts '):
        termSearch(message.content[4:])
   
    #recall 5 most recent terms
    if message.content == '!r' :
        recent()
   
    #link to t&c
    if message.content == '!link' :
        await client.send_message(message.channel, 'http://bit.do/termcon')
   
    if message.content == '!help' :
        help()
 
                       
client.run('buymyasianbaby@gmail.com','suchpassword1')