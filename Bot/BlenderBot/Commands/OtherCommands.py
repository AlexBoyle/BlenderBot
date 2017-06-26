class Other:
  def run(self, message):
    message = message.content[1:]
    if message.startswith('google '):
       return self.googleLink(message[7:])
    if message == 'help' :
       return self.help()

  def help(self):
    output = "```"
    #for entry in self.commandlist:
    #  output += ('Use "%s" to %s! \n' % (entry[0],entry[1]))
    return output + "```"

  def googleLink(self, search):
    return ('https://www.google.com/search?q=' + search).replace(' ','+')
