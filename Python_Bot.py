#!/usr/bin/python3

import discord
import asyncio
import random

import TermCommands
import PingCommands
import VoteCommands


pingObj = []
voteObj = []
terms = TermCommands.Terms()
def terms(message):
    global terms
     #reference term by number
    if message.content.startswith('!t '):
        return terms.term(message.content[3:])

    #search through terms
    if message.content.startswith('!ts '):
        return terms.termSearch(message.content[4:])

    #recall 5 most recent terms
    if message.content == '!r' :
        return  terms.recent()

    #link to t&c
    if message.content == '!link' :
        return 'http://bit.do/termcon'

    #source code
    if message.content == '!code' :
        return 'https://github.com/AlexBoyle/Spicier_Bot'

    #pull up list of TermCommands
    if message.content == '!help' :
        return terms.help()

    #Finds and prints all terms referenced in the last !ts or !t command
    if message.content == '!ref':
        return terms.reference()

    #Random term
    if message.content == '!tr':
         return terms.term(str(random.randint(1,len(TermCommands.termlist))))

def vote(message):

    global voteObj
    i = 0
    for e in  voteObj:
       if e[0] == message.channel:
            break
       i += 1
    if i == len(voteObj):
        voteObj.append([message.channel,VoteCommands.Vote()])


    if message.content.startswith("%vote "):
        return voteObj[i][1].callVote(message)

    if message.content.startswith("%v "):
        return voteObj[i][1].vote(message)

    if message.content.startswith("%result"):
        return voteObj[i][1].results()

    if message.content.startswith("%clear"):
        return voteObj[i][1].clear()

    if message.content.startswith("%help"):
        return voteObj[i][1].help()

def ping(message):
    global pingObj
    i = 0
    for e in  pingObj:
       if e[0] == message.channel:
            return None
       i += 1
    if i == len(pingObj):
        pingObj.append([message.channel,ping()])
    if message.content.strip() == ">ly":
        return ping[i][1].leagueYes()

    if message.content.strip() == ">ln":
        return ping[i][1].leagueNo()

    if message.content.strip() == ">league":
        return ping[i][1].league(message)
client = discord.Client()
 
@client.event
async def on_message(message):

    #Terms and conditions commands
    if message.content.startswith('!'):
        out = terms(message)
        if out != None:
            await client.send_message(message.channel,out)

    #Ping Commands
    if message.content.startswith('>'):
        out = ping(message)
        if out != None:
            await client.send_message(message.channel,out)

    #Vote Commands
    if message.content.startswith('%'):
        out = vote(message)
        if out != None:
            await client.send_message(message.channel,out)

client.run('buymyasianbaby@gmail.com','suchpassword1')
