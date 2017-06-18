import asyncio

class BotCommands:
    async def run(self, message):
        message = message.content[22:]
        print(message)
        #displays how to set up a term sheet
        if message == 'purge':
            deleted = len(await client.purge_from(message.channel, limit=100, check=isme))
            await client.send_message(message.channel,"```" + str(deleted) + " messages deleted```")
