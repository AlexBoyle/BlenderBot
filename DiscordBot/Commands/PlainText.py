from Global import *
import Commands.ImgRand as ImgRand

def run(message):

    out = ''
    #help
    if (('help' in message.content.lower()) and (botid in message.content.lower())):
        out += "```\n"
        for command in commands:
            out += command['sym'] + "help -" + command['desc'] + "\n"
        out += "```"
        return out
    #Greeting
    if (('hello' in message.content.lower()) or ('hi' in message.content.lower())) and botid in message.content.lower():
        return 'Hello, <@!%s>!' % (message.author.id)
    #Random Image from imgur
    if ('random' in message.content.lower() and ('image' in message.content.lower() or 'pic' in message.content.lower()) and ('please' in message.content.lower())):
        return ImgRand.genLink()
    #Random NSFW Image
    if message.content.lower() == "i am a filthy boy who needs an nsfw image" or message.content.lower() == "i am a filthy girl who needs an nsfw image":
        return ImgRand.dirtyimage()
