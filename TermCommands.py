class Terms:

    #Creates dictionary and list for t&c.txt for future reference.
    temp = open('t&c.txt')
    data = temp.readlines()
    temp.close()
    termlist = []
    for line in data:
        if not line[0].isdigit() :
            continue
        line = line.strip().split('. ',1)
        termlist.append(line)
    termdict = {}
    for entry in termlist:
        termdict[int(entry[0])] = entry[1]

    commandlist = [['!t', 'search term by number'],['!ts', 'search through terms using a keyword'],['!tr', 'get random term'],
        ['!r','recall the five most recent terms'],['!link','see the entire list'],['!ref','shows terms referenced by previously by me'],
        ['!code','this bots sorce code']]

    searchlist = []

    def term(a,msg):
        a.searchlist = []
        if msg.isdigit():
            a.searchlist.append(int(msg))
            if int(msg) <= len(a.termlist):
                return ('Term number %i: %s' % (int(msg),a.termdict[int(msg)]))

    def termSearch(a,msg):
        a.searchlist = []
        output = ""
        for entry in a.termlist:
            if msg.lower() in entry[1].lower() :
                a.searchlist.append(int(entry[0]))
        if len(a.searchlist) > 10:
            return ('Be more specific.')
        if len(a.searchlist) == 0:
            return ('No terms found.')
        for query in a.searchlist :
            output += ('Term number %i: %s \n' % (query,a.termdict[query]))
        return output

    def recent(a):
        i = 5
        output = ""
        while i >= 0 :
            output += ('Term number %i: %s \n' % ((len(a.termlist)-i),a.termdict[len(a.termlist)-i]))
            i -= 1
        return output

    def help(a):
        output = ""
        for entry in a.commandlist:
              output += ('Use "%s" to %s! \n' % (entry[0],entry[1]))
        return output

    def reference(a):
        output = ""
        referencelist = []
        for query in a.searchlist:
            if a.termdict[query][0] == "^" :
                output += ('Term number %i: %s \n' % ((query-1),a.termdict[query-1]))
                referencelist.append(query-1)
            if "see: ".lower() in a.termdict[query].lower():
                refstring = ""
                reflocation = a.termdict[query].find("see: ")
                for i in a.termdict[query][(reflocation+4):]:
                    if i.isdigit():
                        refstring += i
                output += ('Term number %i: %s \n' % ((int(refstring),a.termdict[int(refstring)])))       
        a.searchlist = referencelist[:]
        if output == "":
            return "There is nothing to reference."
        return output
