import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('bicchu'):
        await message.channel.send('Bol re')
    if message.content.startswith('marja'):
        await message.channel.send('tu marja')
     if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)
        
client.run(os.getenv('TOKEN'))
