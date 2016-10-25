#Creates dictionary and list for t&c.txt for future reference.
temp = open('t&c.txt')
data = temp.readlines()
temp.close()
termlist = []
for line in data:
    if not line[0].isdigit() :
        continue
    line = line.strip().split('. ')
    termlist.append(line)
termdict = {}
for entry in termlist:
    termdict[int(entry[0])] = entry[1]

commandlist = [['!t', 'search term by number'],['!ts', 'search through terms using a keyword'],['!tr', 'get random term'],
    ['!r','recall the five most recent terms'],['!link','see the entire list'],['!ref','shows terms referenced by previously by me'],
    ['!code','this bots sorce code']]

searchlist = []

def term(msg):
    global searchlist
    searchlist = []
    if msg.isdigit():
        searchlist.append(int(msg))
        if int(msg) <= len(termlist):
            return ('Term number %i: %s' % (int(msg),termdict[int(msg)]))

def termSearch(msg):
    global searchlist
    searchlist = []
    output = ""
    for entry in termlist:
        if msg.lower() in entry[1].lower() :
            searchlist.append(int(entry[0]))
    if len(searchlist) > 10:
        return ('Be more specific.')
    if len(searchlist) == 0:
        return ('No terms found.')
    for query in searchlist :
        output += ('Term number %i: %s \n' % (query,termdict[query]))
    return output

def recent():
    i = 5
    output = ""
    while i >= 0 :
        output += ('Term number %i: %s \n' % ((len(termlist)-i),termdict[len(termlist)-i]))
        i -= 1
    return output

def help():
    output = ""
    for entry in commandlist:
          output += ('Use "%s" to %s! \n' % (entry[0],entry[1]))
    return output

def reference():
    global searchlist
    output = ""
    referencelist = []
    for query in searchlist:
        if termdict[query][0] == "^" :
            output += ('Term number %i: %s \n' % ((query-1),termdict[query-1]))
            referencelist.append(query-1)
        if "see: ".lower() in termdict[query].lower():
            refstring = ""
            reflocation = termdict[query].find("see: ")
            for i in termdict[query][(reflocation+4):]:
                if i.isdigit():
                    refstring += i
            output += ('Term number %i: %s \n' % ((int(refstring),termdict[int(refstring)])))       
    searchlist = referencelist[:]
    if output == "":
        return "There is nothing to reference."
    return output
