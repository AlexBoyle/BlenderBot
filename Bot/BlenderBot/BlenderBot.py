#!/usr/bin/python3

#All code written by Alex Boyle and Rishabh Ekbote
#With special assistance from Gary, Tyler, Otto, Pat and Nick <3
from Utility.sqlUtility import *
from Commands.WeatherCommands import *
from Commands.TermCommands import *
from Commands.ImageRand import *
from Global import *

import discord
import asyncio
import datetime
import sys
import traceback
commands = [
  {
    "sym":'-',
    "file":(ImageRandom()),
    "desc":'Generate Random image links',
    "exclusive":False,
    "help":True
  },
  {
    "sym":'!',
    "file":(TermCommands),
    "desc":'Commands to easily look up our Terms and Conditions',
    "exclusive":True,
    "help":True
  },
  {
    "sym":'+',
    "file":(WeatherCommands()),
    "desc":'Commands to quickly look up the weather in your area',
    "exclusive":False,
    "help":True
  }
]
exclusive = {}
def isme(m):
  return m.author == client.user


client = discord.Client()

#when BlenderBothas launched this is called
@client.event
async def on_ready():
  util = sql()
  servers = util.query("SELECT * FROM servers")
  for command in commands:
    if(command['exclusive']):
      arr = {}
      for server in servers:
        arr[server['id']] = command['file'](server['id'])
      exclusive[command['sym']] = arr

#When BlenderBot Joins a server this is called
@client.event
async def on_server_join(server):
  for command in commands:
    if(command['exclusive']):
      exclusive[command['sym']][server.id] = command['file'](server.id)

# All messages get sent through this function
@client.event
async def on_message(message):
  print(message.content)
  out = ''
  #all commands
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
      if(command['help']):
        out += command['sym'] + "help -" + command['desc'] + "\n"
    out += "```"
    await client.send_message(message.channel,out)
  #bot info
  if (('info' in message.content.lower()) and (botid in message.content.lower())):
    out = (
      "```\n"
      "Blender Bot:\n  This Bot was written by Alex Boyle and Rishabh Ekbote\nwith special "
      "assistance from Gary, Tyler, Otto, Pat and Nick <3\n\n  This bot is open source "
      "(github linked below). If you choose to use any files or major code blocks from this "
      "project, accreditation is appreciated."
      "``` https://github.com/AlexBoyle/BlenderBot"
    )
    await client.send_message(message.channel,out)
  #purge massages
  if(('purge' in message.content.lower()) and (botid in message.content.lower())):
    deleted = len(await client.purge_from(message.channel, limit=100, check=isme))
    await client.send_message(message.channel,"```" + str(deleted) + " messages deleted```")
if __name__ == '__main__':
  client.run(Token)
