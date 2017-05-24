#Creates dictionary and list for t&c.txt for future reference.
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('Files/client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('test').sheet1
sheet = sheet.col_values(1)

commandlist = [['!t', 'search term by number'],['!ts', 'search through terms using a keyword'],['!tr', 'get random term'],
    ['!r','recall the five most recent terms'],['!link','see the entire list'],['!ref','shows terms referenced by previously by me']]

searchlist = []

def run(message):
    #reference term by number
    if message.startswith('t '):
        return term(message[2:])

    #search through terms
    if message.startswith('ts '):
        return termSearch(message[3:])

    #recall 5 most recent terms
    if message == 'r' :
        return recent()

    #link to t&c
    if message == 'link' :
        return 'http://bit.do/termcon'

    #pull up list of TermCommands
    if message == 'help' :
        return help()

    #Finds and prints all terms referenced in the last !ts or !t command
    if message == 'ref':
        return reference()

    #Random term
    if message == 'tr':
         return term(str(random.randint(1,len(sheet))))
def term(msg):
    global searchlist
    searchlist = []
    if msg.isdigit():
        searchlist.append(int(msg))
        if int(msg) <= len(sheet):
            return ('Term number '+ (sheet[int(msg) - 1 ]))

def termSearch(msg):
    global searchlist
    searchlist = []
    output = ""
    for entry in sheet:
        if msg.lower() in entry[1].lower() :
            searchlist.append(int(entry[0]))
    if len(searchlist) > 10:
        return ('Be more specific.')
    if len(searchlist) == 0:
        return ('No terms found.')
    for query in searchlist :
        output += ('Term number ' + (sheet[query]))
    return output

def recent():
    i = 5
    output = ""
    while i >= 0 :
        output += 'Term number ' + sheet[len(termlist)-i] + '\n'
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
        query = query - 1
        if sheet[query][sheet[query].index(' ')+1] == "^" :
            output += ('Term number ' + (sheet[query-1]) + '\n')
            referencelist.append(query-1)
        if "see: ".lower() in sheet[query].lower():
            refstring = ""
            reflocation = sheet[query].find("see: ")
            for i in sheet[query][(reflocation+4):]:
                if i.isdigit():
                    refstring += i
            output += ('Term number ' + (sheet[int(refstring)]) + '\n')
    searchlist = referencelist[:]
    if output == "":
        return "There is nothing to reference."
    return output
