#!/usr/bin/python3
 
import discord
import asyncio
import random
 
import TermCommands
import PingCommands
import VoteCommands
 

 
 
def terms(message):
     #reference term by number
    if message.content.startswith('!t '):
        return TermCommands.term(message.content[3:])
 
    #search through terms
    if message.content.startswith('!ts '):
        return TermCommands.termSearch(message.content[4:])
 
    #recall 5 most recent terms
    if message.content == '!r' :
        return  TermCommands.recent()
 
    #link to t&c
    if message.content == '!link' :
        return 'http://bit.do/termcon'
 
    #source code
    if message.content == '!code' :
        return 'https://github.com/AlexBoyle/Spicier_Bot'
 
    #pull up list of TermCommands
    if message.content == '!help' :
        return TermCommands.help()
 
    #Finds and prints all terms referenced in the last !ts or !t command
    if message.content == '!ref':
        return TermCommands.reference()
 
    #Random term
    if message.content == '!tr':
         return TermCommands.term(str(random.randint(1,len(TermCommands.termlist))))
 
#def vote(message):
 
 
def ping(message):
    if message.content.strip() == ">ly":
        return PingCommands.leagueYes()
 
    if message.content.strip() == ">ln":
        return PingCommands.leagueNo()


client = discord.Client()
 
@client.event
async def on_message(message):
 
    #Terms and conditions commands
    if message.content.startswith('!'):
        await client.send_message(message.channel,terms(message))
 
    #Ping Commands
    if message.content.startswith('>'):
        await client.send_message(message.channel,ping(message))
 
    #Vote Commands
    if message.content.startswith('%'):
        await client.send_message(message.channel,vote(message))
 
client.run('buymyasianbaby@gmail.com','suchpassword1')