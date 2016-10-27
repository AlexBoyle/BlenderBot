#!/usr/bin/python3

import discord
import asyncio
import random

import TermCommands
import PingCommands
import VoteCommands


ping = []
vote = []

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

def vote(message):
    global vote
    i = 0
    for e in  vote:
       if e[0] == message.channel:
            return None
       i += 1
    if i == len(vote):
        vote.append([message.channel,VoteCommands.Vote()])


    if message.content.startswith("%vote "):
        return vote[i][1].callVote(message)

    if message.content.startswith("%v"):
        return vote[i][1].vote(message)

    if message.content.startswith("%results"):
        return vote[i][1].results()

    if message.content.startswith("%clear"):
        return vote[i][1].clear()

    if message.content.startswith("%help"):
        return vote[i][1].help()

def ping(message):
    global ping
    i = 0
    for e in  ping:
       if e[0] == message.channel:
            return None
       i += 1
    if i == len(ping):
        ping.append([message.channel,PingCommands.Ping()])
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
