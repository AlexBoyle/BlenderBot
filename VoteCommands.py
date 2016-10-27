class Vote():
    currentVote = ""
    votes = []
    commandlist = [['%vote [topic]', 'set a vote for topic'],['%v [vote]', 'submit a vote'],
        ['%results', 'get results for current vote'],['%clear', 'clear all data for the current vote']]


    def callVote(a, message):

        if a.currentVote == "":
            a.currentVote = message.content[6:]
            a.votes= []
            return "Vote for '%s' started please vote yes  or no " % a.currentVote
        return "there is already a vote"

    def vote(a, message):
        id = message.author.id
        i = 0
        indx = 0
        for e in a.votes:
            ind = 0
            for d in e[1]:
                if d == id:
                    del a.votes[indx][1][ind]
                ind += 1
            if len(a.votes[indx][1]) == 0:
                del a.votes[indx]
            indx += 1
        for e in  a.votes:
           if e[0] == message.content[3:].lower():
                a.votes[i][1].append(id)
                return None
           i += 1
        if i == len(a.votes):
            a.votes.append([message.content[3:].lower(),[id]])
        return None
    def results(a):
        if a.currentVote == "":
            return "There is no vote right now"
        out = a.currentVote
        for e in a.votes:
            out += "\n%s (%i):\n" % (e[0], len(e[1]))
            for d in e[1]:
                out += "<@%s>\n" % d
        return out
    def clear(a):
        a.currentVote = ""
        a.votes = []
    def help(a):
        output = ""
        for entry in a.commandlist:
              output += ('Use "%s" to %s! \n' % (entry[0],entry[1]))
        return output

