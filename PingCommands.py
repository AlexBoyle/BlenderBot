from time import time
 
LeagueInitiator = ""
 
def leagueCheck():
    if message.content.strip() == "@Does anyone want to play League?".strip() :
        LeagueInitiator = (message.author, time())
   
def leagueYes():
    output = ""
    if time() > LeagueInitiator[1] + 1800:
        output += 'There has not been a recent @League ping.'
    if LeagueInitiator == "":
        output += 'There has not been a recent @League ping.'
    else:
        output += '@%s Yes, I would very much enjoy playing League of Legends!' % (LeagueInitiator[0])
    return output
       
def leagueNo():
    output = ""
    if time() > LeagueInitiator[1] + 1800:
        output += 'There has not been a recent @League ping.'
    if LeagueInitiator == "":
        output += 'There has not been a recent @League ping.'
    else:
        output += '@%s Unfortunately, I cannot play this round.' % (LeagueInitiator[0])
    return output