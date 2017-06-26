class BotCommands:
  def run(self, message):
    message = message.content[22:]
    print(message)
    #displays how to set up a term sheet
    if message == 'purge':
      ''
      #deleted = len(await client.purge_from(message.channel, limit=100, check=isme))
      #await client.send_message(message.channel,"```" + str(deleted) + " messages deleted```")
  def info():
    if (('info' in message.content.lower()) and (botid in message.content.lower())):
      out = (
        "```\n"
        "Blender Bot:\n  This Bot was written by Alex Boyle and Rishabh Ekbote\nwith special "
        "assistance from Gary, Tyler, Otto, Pat and Nick <3\n\n  This bot is open source "
        "(github linked below). If you choose to use any files or major code blocks from this "
        "project, accreditation is appreciated."
        "``` https://github.com/AlexBoyle/Spicier_Bot (link to be updated)"
      )
      return out
