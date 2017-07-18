#Creates dictionary and list for t&c.txt for future reference.
from Utility.TermService import *
import random

class TermCommands:
  searchlist = []
  commandlist = [
    ['!t', 'search term by number'],
    ['!ts', 'search through terms using a keyword'],
    ['!tr', 'get random term'],
    ['!r','recall the five most recent terms'],
    ['!ref','shows terms referenced by \'^\' or \'see:\'']
  ]
  isSetup = False
  def __init__(self, server_id):
    try:
      self.service = TermService(server_id)
      self.length = self.service.getLen()
      if(self.length == None):
        self.length = 0
      self.isSetup = True
    except Exception as inst:
      print(inst)
      self.isSetup = False
  def run(self, message):
    msg = message.content[1:]

    #Admin commands
    if message.channel.permissions_for(message.author).administrator:
      if msg.startswith('add '):
        return self.add(msg[4:])
      if msg.startswith('rm '):
        return self.rm(msg[3:])
      if msg.startswith('edit '):
        return self.edit(msg[5:])

    #reference term by number
    if msg.startswith('t '):
      return self.term(msg[2:])

    #search through terms
    if msg.startswith('ts '):
      return self.termSearch(msg[3:])

    #recall 5 most recent terms
    if msg == 'r' :
      return self.recent()

    #pull up list of TermCommands
    if msg == 'help' :
      return self.help()

    #Finds and prints all terms referenced in the last !ts or !t command
    if msg == 'ref':
      return self.reference()

    #Random term
    if msg == 'tr':
      return self.term(str(random.randint(1,self.length)))
  def add(self, msg):
    self.service.newTerm(msg)
    self.length = self.service.getLen()
    if(self.length == None):
      self.length = 0
  def rm(self, msg):
    self.service.rmTerm(msg)
    self.length = self.service.getLen()
    if(self.length == None):
      self.length = 0
  def edit(self, msg):
    return self.service.editTerm(1,msg)
  def getTerm(self, num):
    if (type(num) is str and num.isdigit()) or type(num) is int:
      if int(num) <= self.length:
        term = self.service.getTerm(num)
        self.searchlist.append(term)
        return ('Term number '+ str(term['num']) + ': ' + term['content'])
  def term(self, msg):
    self.searchlist = []
    return self.getTerm(msg)
  def termSearch(self, msg):
    searchlist = self.service.getSearch(msg)
    output = ""
    
    if len(searchlist) > 10:
      return ('Be more specific.')
    if len(searchlist) == 0:
      return ('No terms found.')
    for query in searchlist :
      output +=  self.getTerm(query['num']) + "\n"
    self.searchlist = searchlist
    return output
  def recent(self):
    i = 4
    output = ""
    while i >= 0 :
      output += self.getTerm(self.length- i)+ '\n'
      i -= 1
    return output
  def help(self):
    output = "```"
    for entry in self.commandlist:
      output += ('Use "%s" to %s! \n' % (entry[0],entry[1]))
    return output + "```"
  def reference(self):
    output = ""
    referencelist = []
    for query in self.searchlist:
      if query['content'][0] == "^" :
        output += self.getTerm(query['num'] - 1) + '\n'
        referencelist.append(query['num']-1)
      if "see: ".lower() in query['content'].lower():
        refstring = ""
        reflocation = query['content'].find("see: ")
        for i in query['content'][(reflocation+4):]:
          if i.isdigit():
            refstring += i
        output += self.getTerm(int(refstring)) + '\n'
    self.searchlist = referencelist[:]
    if output == "":
      return "There is nothing to reference."
    return output
