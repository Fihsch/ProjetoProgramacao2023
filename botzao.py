# import discord
# import os

# class MyClient(discord.Client):
#     async def onready(self):
#         print('logged as {0}!'. format(self.user))

#     async def on_message(self, message):
#         print('message from {0 author}: {0 content}'.format(message))
#         if message.content == '?regras':
#             await message.channel.send(f'{message.author.name} as regras do servidor são: {os.linesep} 1 - Não desreipeitar os membros {os.linesep} 2 - regra importante 2')
#         elif message.content == '?nivel':
#             await message.send('Nível 1')
    
#     async def on_member_join(self, member):
#         guild = member.guild
#         if guild.system_channel is not None:
#             mensagem = f'{member.mention} acabou de entrar no {guild.name}'
#             await guild.system_channel.send(mensagem)

# intents = discord.intents.default()
# intents.member = True
        
# client = MyClient()
# client.run('MTEzODE0OTY2NjQ0NjM4NTM1NQ.GHuUjn.tAjuEGKP1Fv7rK46YkyFRIFkNziS2iye75fEX4')

import discord
import os

# class MyClient(discord.Client):
#     async def on_ready(self):
#         print('logged as {0}!'.format(self.user))

#     async def on_message(self, message):
#         print('message from {0.author}: {0.content}'.format(message))
#         if message.content == '?regras':
#             await message.channel.send(f'{message.author.name} as regras do servidor são: {os.linesep} 1 - Não desrespeitar os membros {os.linesep} 2 - regra importante 2')
#         elif message.content == '?nivel':
#             await message.channel.send('Nível 1')
    
#     async def on_member_join(self, member):
#         guild = member.guild
#         if guild.system_channel is not None:
#             mensagem = f'{member.mention} acabou de entrar no {guild.name}'
#             await guild.system_channel.send(mensagem)

# intents = discord.Intents.default()
# intents.members = True
        
# client = MyClient(intents=intents)
# client.run('MTEzODE0OTY2NjQ0NjM4NTM1NQ.GHuUjn.tAjuEGKP1Fv7rK46YkyFRIFkNziS2iye75fEX4')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient()
client.run('MTEzODE0OTY2NjQ0NjM4NTM1NQ.GHuUjn.tAjuEGKP1Fv7rK46YkyFRIFkNziS2iye75fEX4')