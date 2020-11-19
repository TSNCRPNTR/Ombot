import discord
from discord.ext import commands
import time
import asyncio
import json
with open('config.json') as f:
    config = json.load(f)
prefix = config['prefix']
token = config['token']

#functions
import dadJoke
import genResponses

bot = commands.Bot(command_prefix=prefix, description='bruh.')
#Defines a bot's prefix and description. There is one predefined command in the bot, the help command. This command shows you the full list of commands you have created.
client = discord.Client()

@bot.event
async def on_ready():
    print("Logged in as Ombot")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif 'I\'m ' in message.content or 'i\'m ' in message.content:
        await message.channel.send(dadJoke.makeDadJoke(message.content))
    else:
        #Reads each message, if it lines up with any 'cases' in the 'switch' function, then it responds.
        await message.channel.send(genResponses.messageGet(message.content))

bot.run(token)
#Replace bot_token with your actual bot token. Do not post it publically, your bot token will be stealed.