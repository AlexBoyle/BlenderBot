from time import time

class ping:

    LeagueInitiator = ("",0)

    def league(a,message):
        a.LeagueInitiator = (message.author, time())
        return "League Ping Started"

    def leagueYes(a):
        output = ""
        if a.LeagueInitiator[0] == "":
            return 'There has not been a recent @League ping.'
        if time() > a.LeagueInitiator[1] + 1800:
            return 'There has not been a recent @League ping.'
        else:
            return '<@%s> Yes, I would very much enjoy playing League of Legends!' % (a.LeagueInitiator[0].id)

    def leagueNo(a):
        output = ""
        if a.LeagueInitiator[0] == "":
            return 'There has not been a recent @League ping.'
        if time() > a.LeagueInitiator[1] + 1800:
            return 'There has not been a recent @League ping.'
        else:
            return '<@%s> Unfortunately, I cannot play this round.' % (a.LeagueInitiator[0].id)
