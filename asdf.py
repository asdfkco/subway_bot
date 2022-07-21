import discord
import json
from discord.ext import commands


with open ("./token/token.json", "r") as f:
    token = json.load(f)
    
    
    client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('Loggend in Bot: ', client.user.name)
    print('Bot id: ', client.user.id)
    print('connection was succesful!')
    print('=' * 30)
    
    
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # elif message.content.startswith("."):
        # await message.channel.send(message.content)
    elif message.author.id == 524523017620160523:
        await message.channel.send(message.content)
        
        
    
    
client.run(token["token"])