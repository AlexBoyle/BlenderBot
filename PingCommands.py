from time import time

LeagueInitiator = ("",0)

def league(message):
    global LeagueInitiator
    LeagueInitiator = (message.author, time())
    return "League Ping Started"

def leagueYes():
    global LeagueInitiator
    output = ""
    if LeagueInitiator[0] == "":
        return 'There has not been a recent @League ping.'
    if time() > LeagueInitiator[1] + 1800:
        return 'There has not been a recent @League ping.'
    else:
        return '<@%s> Yes, I would very much enjoy playing League of Legends!' % (LeagueInitiator[0].id)

def leagueNo():
    global LeagueInitiator
    output = ""
    if LeagueInitiator[0] == "":
        return 'There has not been a recent @League ping.'
    if time() > LeagueInitiator[1] + 1800:
        return 'There has not been a recent @League ping.'
    else:
        return '<@%s> Unfortunately, I cannot play this round.' % (LeagueInitiator[0].id)
