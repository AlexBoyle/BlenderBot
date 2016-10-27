currentVote = ""
yes = []
no = []
commandlist = [['%vote [topic]', 'set a vote for topic'],['%y[es]', 'submit a yes vote'],
    ['%n[0]', 'submit a no vote'],['%results', 'get results for current vote'],['%clear', 'clear all data for the current vote']]


def callVote(message):
    global currentVote
    global yes
    global no
    if currentVote == "":
        currentVote = message.content[6:]
        yes = []
        no = []
        return "Vote for '%s' started please vote yes  or no " % currentVote
    return "there is already a vote"

def yesVote(message):
    global yes
    global no
    id = message.author.id
    if id in no:
        no.remove(id)
    if id not in yes:
        yes.append(id)
    return  None
def noVote(message):
    global yes
    global no
    id = message.author.id
    if id in yes:
        yes.remove(id)
    if id not in no:
        no.append(id)
    return None
def results():
    if currentVote == "":
        return "There is no vote right now"
    out = "%s \nYes votes(%i):\n" % (currentVote,len(yes))
    for e in yes:
        out += "<@" + e + ">\n"
    out += "No votes(%i):\n" % len(no)
    for e in no:
        out += "<" + e + ">\n"
    return out
def clear():
    global currentVote
    global yes
    global no
    currentVote = ""
    yes = []
    no = []
def help():
    output = ""
    for entry in commandlist:
          output += ('Use "%s" to %s! \n' % (entry[0],entry[1]))
    return output

