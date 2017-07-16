import numpy as np
import requests


class ImageRandom:
  options = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789')
  commandlist = [
    ['-imgur', 'Generate a random imgur picture']
  ]

  def run(self, message):
    message = message.content[1:]
    if message.startswith('imgur'):
      return self.genLink()
    if message.startswith('help'):
      return self.help()

  def urlgen(self):
    length = 5
    choice = np.random.permutation(self.options)
    urlend = ''.join(choice[0:length])
    candidate = ('http://i.imgur.com/%s' % (urlend))
    return candidate

  def checkLink(self, candidate):
    validurl = False
    page = requests.get(candidate)
    if page.status_code == 200:
      validurl = True
    return validurl

  def genLink(self):
    attempts = 30
    while attempts > 0:
      candidate = self.urlgen()
      if self.checkLink(candidate) == True:
        return candidate
      attempts -= 1
    return 'I failed to get an image :('
  def help(self):
    output = "```"
    for entry in self.commandlist:
      output += ('Use "%s" to %s! \n' % (entry[0],entry[1]))
    return output + "```"