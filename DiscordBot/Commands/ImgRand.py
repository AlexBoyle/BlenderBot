import numpy as np
import requests

options = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789')


def run(message):
    #reference term by number
    if message.startswith('ir '):
        return genLink()

def getLink():
    length = 5
    choice = np.random.permutation(options)
    urlend = ''.join(choice[0:length])
    candidate = ('http://i.imgur.com/%s' % (urlend))
    return candidate

def checkLink(candidate):
    validurl = False
    page = requests.get(candidate)
    if page.status_code == 200:
        validurl = True
    return validurl

def genLink(options):
    attempts = 30
    while attempts > 0:
        candidate = urlgen(options)
        if checkfunc(candidate) == True:
            return candidate
        attempt -= 1
    return 'I failed to get an image :('


def urlgendirty():
    urlend = (np.random.randint(1,int(2e6)))
    candidate = ('http://rule34.paheal.net/post/view/%s' % (urlend))
    return candidate


def dirtyimage():
    attempts = 30
    while attempts > 0:
        candidate = urlgendirty()
        if checkfunc(candidate) == True:
            return candidate
        attempts -= 1
    return 'I failed to get an image :('
