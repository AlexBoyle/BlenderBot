import numpy as np
import requests

options = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789')

def urlgen(options):
    length = 5
    choice = np.random.permutation(options)
    urlend = ''.join(choice[0:length])
    candidate = ('http://i.imgur.com/%s' % (urlend))
    return candidate

def checkfunc(candidate):
    validurl = False
    page = requests.get(candidate)
    if page.status_code == 200:
        validurl = True
    return validurl

def imgrand(options):
    while True:
        candidate = urlgen(options)
        if checkfunc(candidate) == True:
            return candidate


def urlgendirty():
    urlend = (np.random.randint(1,int(2e6)))
    candidate = ('http://rule34.paheal.net/post/view/%s' % (urlend))
    return candidate


def dirtyimage():
    while True:
        candidate = urlgendirty()
        if checkfunc(candidate) == True:
            return candidate
    