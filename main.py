import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('bicchu'):
        await message.channel.send('Bol re')
    if message.content.startswith('marja'):
        await message.channel.send('tu marja')
client.run(os.getenv('TOKEN'))
