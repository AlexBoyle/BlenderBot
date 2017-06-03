#Creates dictionary and list for t&c.txt for future reference.
import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class TermCommands:
    sheet = {}
    searchlist = []
    commandlist = [['!setup', 'steps to set up your terms file'],['!t', 'search term by number'],['!ts', 'search through terms using a keyword'],['!tr', 'get random term'],
        ['!r','recall the five most recent terms'],['!ref','shows terms referenced by \'^\' or \'see:\'']]
    isSetup = False
    def __init__(self, server_id):
        try:
            scope = ['https://spreadsheets.google.com/feeds']
            creds = ServiceAccountCredentials.from_json_keyfile_name('Files/client_secret.json', scope)
            client = gspread.authorize(creds)
            self.sheet = client.open(str(server_id + 'Terms')).sheet1
            self.sheet = self.sheet.col_values(1)
            temp = {}
            it = 1
            for term in self.sheet:
                temp[it] = {}
                temp[it][0] = int(term[:term.find(':')])
                temp[it][1] = term[term.find(':')+2:]
                it += 1
            self.sheet = temp
            self.isSetup = True
        except:
            self.isSetup = False
    def run(self, message):
        if(not self.isSetup):
            return "`Term sheet is not set up correctly`"
        message = message.content[1:]
        #displays how to set up a term sheet
        if message == 'setup':
            return self.setup()
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
    def term(self, msg):
        self.searchlist = []
        if (type(msg) is str and msg.isdigit()) or type(msg) is int:
            self.searchlist.append(int(msg))
            if int(msg) <= len(self.sheet):
                return ('Term number '+ str(self.sheet[int(msg)][0]) + ': ' + self.sheet[int(msg)][1])
    def termSearch(self, msg):
        self.searchlist = []
        output = ""
        for key in self.sheet:
            if msg.lower() in self.sheet[key][1].lower() :
                self.searchlist.append(key)
        if len(self.searchlist) > 10:
            return ('Be more specific.')
        if len(self.searchlist) == 0:
            return ('No terms found.')
        for query in self.searchlist :
            output +=  self.term(query) + "\n"
        return output
    def recent(self):
        i = 4
        output = ""
        while i >= 0 :
            output += self.term(len(self.sheet)- i)+ '\n'
            i -= 1
        return output
    def help(self):
        output = "```"
        for entry in self.commandlist:
            output += ('Use "%s" to %s! \n' % (entry[0],entry[1]))
        return output + "```"
    def setup(self):
        output = (
            "```\n1) create a google spreadsheet called 'terms'\n"
            "2) share the google sheet with ''\n"
            "3) make the sheet look similar to the image linked below\n"
            "Formating:\n"
            "ex: 231: ^if you don't have a license, you can still bike #legitroadtrip [See: rule 156]"
            " - start each term with '{number}:'\n"
            " - if this terms references the previos term start the term with '^'\n"
            " - the body of the term appeirs after the term number\n"
            " - if the term needs to refrence any other term the term can be ended with '[See: rule {number}]'\n```"
        )
        return output
    def reference(self):
        output = ""
        referencelist = []
        for query in self.searchlist:
            print(self.sheet[query][1])
            if self.sheet[query][1][0] == "^" :
                output += self.term(query-1) + '\n'
                referencelist.append(query-1)
            if "see: ".lower() in self.sheet[query][1].lower():
                refstring = ""
                reflocation = self.sheet[query][1].find("see: ")
                for i in self.sheet[query][(reflocation+4):]:
                    if i.isdigit():
                        refstring += i
                output += self.term(int(refstring)) + '\n'
        self.searchlist = referencelist[:]
        if output == "":
            return "There is nothing to reference."
        return output
