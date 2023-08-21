import discord
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == '?regras':
            await message.channel.send(f"{message.author.name} as regras do servidor são: {os.linesep} 1 - Não desrespeitar os membros {os.linesep} 2 - A regra 1 não se aplica ao Mateus Carlos Dudley Cruz nem ao Pedro Henrique")

client = MyClient()
client.run('MTEzODE0OTY2NjQ0NjM4NTM1NQ.GHuUjn.tAjuEGKP1Fv7rK46YkyFRIFkNziS2iye75fEX4')