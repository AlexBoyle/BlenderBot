#!/usr/bin/python3

#All code written by Alex Boyle and Rishabh Ekbote
#With special assistance from Gary, Tyler, Otto, Pat and Nick <3

from Other.sqlUtility import *
from Commands.WeatherCommands import *
from Commands.TermCommands import *
from Commands.ImageRand import *
from Commands.BotCommands import *
from Commands.OtherCommands import *
from Global import *
from temp import *

import discord
import asyncio
import datetime
import sys
import traceback

commands = [
  {"sym":'-', "file":(ImageRandom()), "desc":'(NSFW)Generate Random image links',"exclusive":False,"help":True},
  {"sym":'!', "file":(TermCommands), "desc":'Commands to easily look up our Terms and Conditions',"exclusive":True,"help":True},
  {"sym":'+', "file":(WeatherCommands()), "desc":'Commands to quickly look up the weather in your area',"exclusive":False,"help":True},
  {"sym":'&', "file":(Other()), "desc":'Random utilitys people hae requested',"exclusive":False,"help":True},
  {"sym":'<@' + botid + '>', "file":(BotCommands()), "desc":'',"exclusive":False,"help":False}
]
exclusive = {}
start_time = datetime.datetime.now()

def isme(m):
  return m.author == client.user

client = discord.Client()

@client.event
async def on_ready():
  #sqll = sql()
  #print(sqll.query("select count(num) from terms;"))
  client.change_presence(game="Snappin Necks and Cashin Checks")
  util = Utility()
  server_ids = util.get_server_ids()
  for command in commands:
    if(command['exclusive']):
      arr = {}
      for server_id in server_ids:
        arr[server_id] = command['file'](server_id)
      exclusive[command['sym']] = arr

@client.event
async def on_server_join(server):
  for command in commands:
    if(command['exclusive']):
      exclusive[command['sym']][server.id] = command['file'](server.id)
@client.event
async def on_message(message):
  try:
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
    print(message.content.lower())
    if (('help' in message.content.lower()) and (botid in message.content.lower())):
      out = ''
      out += "```\n"
      out += "@BlenderBot info - Info about Blender Bot\n"
      for command in commands:
        if(command.help):
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
    if(('purge' in message.content.lower()) and (botid in message.content.lower())):
      deleted = len(await client.purge_from(message.channel, limit=100, check=isme))
      await client.send_message(message.channel,"```" + str(deleted) + " messages deleted```")
  except Exception as exception:
    print('-'*50)
    print(str(sys.exc_info()[0]) + '\n')
    traceback.print_exc(file=sys.stdout)

@client.event
async def on_error(event, args, somthing_else):
  print('there was an issue, good luck')



if __name__ == '__main__':
  client.run(Token)
