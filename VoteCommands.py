class Vote:
    currentVote = ""
    votes = []
    commandlist = [['%vote [topic]', 'set a vote for topic'],['%v [vote]', 'submit a vote'],
        ['%results', 'get results for current vote'],['%clear', 'clear all data for the current vote']]


    def callVote(message):
        global currentVote
        global votes
        if currentVote == "":
            currentVote = message.content[6:]
            votes= []
            return "Vote for '%s' started please vote yes  or no " % currentVote
        return "there is already a vote"

    def vote(message):
        global votes
        id = message.author.id
        i = 0
        indx = 0
        for e in votes:
            ind = 0
            for d in e[1]:
                if d == id:
                    del votes[indx][1][ind]
                ind += 1
            if len(votes[indx][1]) == 0:
                del votes[indx]
            indx += 1
        for e in  votes:
           if e[0] == message.content[3:].lower():
                votes[i][1].append(id)
                return None
           i += 1
        if i == len(votes):
            votes.append([message.content[3:].lower(),[id]])
        return None
    def results():
        if currentVote == "":
            return "There is no vote right now"
        out = currentVote
        for e in votes:
            out += "\n%s (%i):\n" % (e[0], len(e[1]))
            for d in e[1]:
                out += "<@%s>\n" % d
        return out
    def clear():
        global currentVote
        global votes
        global no
        currentVote = ""
        votes = []
    def help():
        output = ""
        for entry in commandlist:
              output += ('Use "%s" to %s! \n' % (entry[0],entry[1]))
        return output

