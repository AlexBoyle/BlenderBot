#Creates dictionary and list for t&c.txt for future reference.
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class TermCommands:

    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('Files/client_secret.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open('test').sheet1
    sheet = sheet.col_values(1)

    commandlist = [['!t', 'search term by number'],['!ts', 'search through terms using a keyword'],['!tr', 'get random term'],
        ['!r','recall the five most recent terms'],['!link','see the entire list'],['!ref','shows terms referenced by previously by me']]

    searchlist = []

    def run(self, message):
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

        #link to t&c
        if message == 'link' :
            return 'http://bit.do/termcon'

        #pull up list of TermCommands
        if message == 'help' :
            return self.help()

        #Finds and prints all terms referenced in the last !ts or !t command
        if message == 'ref':
            return self.reference()

        #Random term
        if message == 'tr':
            return self.term(str(random.randint(1,len(self.sheet))))
    def term(self, msg):
        self.searchlist = []
        if msg.isdigit():
            self.searchlist.append(int(msg))
            if int(msg) <= len(self.sheet):
                return ('Term number '+ (self.sheet[int(msg) - 1 ]))

    def termSearch(self, msg):
        self.searchlist = []
        output = ""
        for entry in self.sheet:
            if msg.lower() in entry[1].lower() :
                self.ssearchlist.append(int(entry[0]))
        if len(self.searchlist) > 10:
            return ('Be more specific.')
        if len(self.searchlist) == 0:
            return ('No terms found.')
        for query in self.searchlist :
            output += ('Term number ' + (self.sheet[query]))
        return output

    def recent(self):
        i = 5
        output = ""
        while i >= 0 :
            output += 'Term number ' + self.sheet[len(self.sheet)-i] + '\n'
            i -= 1
        return output

    def help(self):
        output = ""
        for entry in self.commandlist:
            output += ('Use "%s" to %s! \n' % (entry[0],entry[1]))
        return output

    def reference(self):
        output = ""
        referencelist = []
        for query in self.searchlist:
            query = query - 1
            if self.sheet[query][self.sheet[query].index(' ')+1] == "^" :
                output += ('Term number ' + (self.sheet[query-1]) + '\n')
                referencelist.append(query-1)
            if "see: ".lower() in self.sheet[query].lower():
                refstring = ""
                reflocation = self.sheet[query].find("see: ")
                for i in self.sheet[query][(reflocation+4):]:
                    if i.isdigit():
                        refstring += i
                output += ('Term number ' + (self.sheet[int(refstring)]) + '\n')
        self.searchlist = referencelist[:]
        if output == "":
            return "There is nothing to reference."
        return output
