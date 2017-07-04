#Creates dictionary and list for t&c.txt for future reference.
from Utility.sqlUtility import *
import random

class TermCommands:
  sheet = {}
  searchlist = []
  commandlist = [['!t', 'search term by number'],['!ts', 'search through terms using a keyword'],['!tr', 'get random term'],
    ['!r','recall the five most recent terms'],['!ref','shows terms referenced by \'^\' or \'see:\'']]
  isSetup = False
  def __init__(self, server_id):
    try:
      self.server_id = str(server_id)
      self.sql = sql()
      self.length = self.sql.query("SELECT COUNT(num) AS length FROM terms WHERE " + str(server_id))[0]['length']
      self.isSetup = True
    except Exception as inst:
      print(inst)
      self.isSetup = False
  def run(self, message):
    if(not self.isSetup):
      return "`Something went wrong`"

    message = message.content[1:]
    #reference term by number
    if message.startswith('t '):
      return self.term(message[2:])

    #search through terms
    if message.startswith('ts '):
      return self.termSearch(message[3:])

    #recall 5 most recent terms
    if message == 'r' :
      return self.recent()

    #pull up list of TermCommands
    if message == 'help' :
      return self.help()

    #Finds and prints all terms referenced in the last !ts or !t command
    if message == 'ref':
      return self.reference()

    #Random term
    if message == 'tr':
      return self.term(str(random.randint(1,len(self.sheet))))

  def getTerm(self, num):
    if (type(num) is str and num.isdigit()) or type(num) is int:
      if int(num) <= self.length:
        term = self.sql.query("SELECT * FROM terms WHERE server_id=" + str(self.server_id) + " AND num=" + str(num))[0]
        return ('Term number '+ str(term['num']) + ': ' + term['content'])
  def term(self, msg):
    self.searchlist = []
    return self.getTerm(msg)
  def termSearch(self, msg):
    searchlist = self.sql.query("SELECT num, content FROM terms WHERE server_id=" + self.server_id + " AND content LIKE " + '"%' + msg + '%"')
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
