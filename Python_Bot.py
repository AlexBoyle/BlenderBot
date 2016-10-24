#!/usr/bin/python3
 
import discord
import asyncio
import logging
 
#Creates dictionary and list for t&c.txt for future reference.
temp = open('t&c.txt')
data = temp.readlines()
temp.close()
termlist = []
for line in data:
    if not line[0].isdigit() :
        continue
    line = line.strip().split('. ')
    termlist.append(line)
termdict = {}
for entry in termlist:
    termdict[int(entry[0])] = entry[1]
############################################################################################
client = discord.Client()
 
@client.event
async def on_message(message):
   
    #reference term by number
    if message.content.startswith('!t '):
        msg = message.content[3:]
        if msg.isdigit():
            if int(msg) <= len(termlist):
                await client.send_message(message.channel, 'Term number %i: %s' % (int(msg),termdict[int(msg)]))
   
    #search through terms
    if message.content.startswith('!ts '):
        searchlist = []
        msg = message.content[4:]
        for entry in termlist:
            if msg.lower() in entry[1].lower() :
                searchlist.append(int(entry[0]))
        if len(searchlist) > 10:
            await client.send_message(message.channel, 'Be more specific.')
            return
        if len(searchlist) == 0:
            await client.send_message(message.channel, 'No terms found.')
            return
        for query in searchlist :
            await client.send_message(message.channel, 'Term number %i: %s' % (query,termdict[query]))
   
    #recall 5 most recent terms
    if message.content == '!r' :
        i = 5
        while i >= 0 :
            await client.send_message(message.channel, 'Term number %i: %s' % ((len(termlist)-i),termdict[len(termlist)-i]))
            i -= 1
   
    #link to t&c
    if message.content == '!link' :
        await client.send_message(message.channel, 'http://bit.do/termcon')
   
    #help command
    commandlist = [['!t', 'search term by number'],['!ts', 'search through terms using a keyword'],
                   ['!r','recall the five most recent terms'],['!link','see the entire list']]
   
    if message.content == '!help' :
        for entry in commandlist:
            await client.send_message(message.channel, 'Use "%s" to %s!' % (entry[0],entry[1]))
 
                       
client.run('buymyasianbaby@gmail.com','suchpassword1')