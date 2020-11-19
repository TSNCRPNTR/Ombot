#Just using this working version of the bot as a reference to work with

# Work with Python 3.9
import discord
import random
from discord.utils import get
import time
from time import sleep
import asyncio
import json
with open('config.json') as f:
    config = json.load(f)
prefix = config['prefix']
token = config['token']

TOKEN = token

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        # we do not want the bot to reply to itself
        return
    elif 'I\'m ' in message.content or 'i\'m ' in message.content:     
        #if there's an "I'm" in the function, makes a dad joke on it
        await message.channel.send(makeDadJoke(message.content))

    elif 'can they pass the turing test' in message.content: 
        #can't wait to forget that I put this here
        await message.channel.send('Idk, maybe')

    elif (message.content == '/react'):
        #just got it in for a test
        await message.add_reaction('🇳')
        await asyncio.sleep(0.1)
        await message.add_reaction('🇴')

    elif (message.content == 'f') or ' f ' in message.content:   
        #haha fbot go brrr  
        await message.add_reaction('🇫')

    elif (message.content == '/face'):
        #heh
	    await message.channel.send(random.choice(lenny))
    else:
        #Reads each message, if it lines up with any 'cases' in the 'switch' function, then it responds.
        await message.channel.send(messageGet(message.content))

lenny = ['( ͡° ͜ʖ ͡°)','¯\\_(ツ)_/¯','ʕ•ᴥ•ʔ','༼ つ ◕_◕ ༽つ','ಠ_ಠ','(◕‿◕✿)','ヾ(⌐■_■)ノ♪','ᕙ(⇀‸↼‶)ᕗ','ヽ༼ຈل͜ຈ༽ﾉ','(｡◕‿◕｡)','._.','^-^',':3']


####    GENERIC MESSAGE RESPONSES    ####

# yeah baby, switch functions
# (It's just dictionary mapping, but kinda worse ^-^ )
#   -> *INPUT*: *OUTPUT* <-
# Used for basic one-in one-out type interactions
def messageGet(argument):
    switcher = {
        '/hey ombot': 'hi!!',
        '/boop': 'beep',
        '/beep': 'boop',
        '/hi': "hewwo",
    }

    # Returns what matches up with the input
    return switcher.get(argument)



####    DAD JOKE    ####

# most complex function by far
# all for a stupid dad joke
def makeDadJoke(message):
    #Setting up base variables
    finalString = ""                            #The old message, from "I'm" to period
    newx = ""                                   #The final word in the message, without the period
    cont = 0                                    #Asking "Should I count this word?"

    msglist = message.split()                   #Splitting the message into a list, each word is seperate
    for x in msglist:                           #Goes through each word in the message
        if x == 'I\'m' or x == 'i\'m':          #Doesn't start 'counting' until it sees the "I'm" in the message (not case sensitive                   
                cont = 1
        elif bool(cont):                        #As soon as it passes the "I'm", it starts adding words to the new string.
            for y in x:                         #Checks to see if the word has a period, if it does, it ends the check and removes the period.
                if y == "." or y == ",":                    
                    cont = -1                   #Makes sure it can only read one I'm
                    newx = ""                   #Makes sure the string is empty before making it
                    for i in range(0, len(x)):  #Iterates through the word till it gets to the last letter, then 'forgets' to add the period.
                        if i != len(x)-1: 
                            newx = newx + x[i]
                    x = newx                    #Old word is new word
                    break
            finalString += " "+x                #Builds the final string with all the words combined (in the loop)
    return "Hi"+finalString+", I'm Dad!"        #Haha funee joke


####    DEBUG   ####

# debug stuff *o*
@client.event
async def on_ready():

    #not creepy at all
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='you... o_o'))

    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)

#Reference for me
#Formatting for messages:
    #   *italics*
    #   **bold**
    #   ***bold italics***
    #   __underline__
    #   __*underline italics*__
    #   __**underline bold**__
    #   __***underline bold italics***__
    #   ~~strikethrough~~
    #   `code box`
    #   '''multiline
    #      code box'''
    #   >be me (quote)
