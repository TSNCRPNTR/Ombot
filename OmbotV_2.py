import discord
from discord.ext import commands
import time
import asyncio
import json
import random
from random import shuffle
from random import randint
with open('config.json') as f:
    config = json.load(f)
prefix = config['prefix']
token = config['token']

#functions
import dadJoke
import genResponses
import tarotDeck
import maze
import ticTacToe

lenny = ['( ͡° ͜ʖ ͡°)','¯\\_(ツ)_/¯','ʕ•ᴥ•ʔ','༼ つ ◕_◕ ༽つ','ಠ_ಠ','(◕‿◕✿)','ヾ(⌐■_■)ノ♪','ᕙ(⇀‸↼‶)ᕗ','ヽ༼ຈل͜ຈ༽ﾉ','(｡◕‿◕｡)','._.','^-^',':3','\'u\'']

# create discord client
client = discord.Client()

class CommandHandler:

    # constructor
    def __init__(self, client):
        self.client = client
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def command_handler(self, message):
        for command in self.commands:
            if message.content.startswith(command['trigger']):
                args = message.content.split(' ')
                if args[0] == command['trigger']:
                    args.pop(0)
                    if command['args_num'] == 0:
                        return message.channel.send(str(command['function'](message, self.client, args)))
                        break
                    else:
                        if len(args) >= command['args_num']:
                            return message.channel.send(str(command['function'](message, self.client, args)))
                            break
                        else:
                            return message.channel.send('command "{}" requires {} argument(s) "{}"'.format(command['trigger'], command['args_num'], ', '.join(command['args_name'])))
                            break
                else:
                    break

# create the CommandHandler object and pass it the client
ch = CommandHandler(client)

## start commands command
def commands_command(message, client, args):
    try:
        count = 1
        coms = '**Commands List**\n'
        for command in ch.commands:
            coms += '{}.) {} : {}\n'.format(count, command['trigger'], command['description'])
            count += 1
        return coms
    except Exception as e:
        print(e)
ch.add_command({
    'trigger': '/commands',
    'function': commands_command,
    'args_num': 0,
    'args_name': [],
    'description': 'Prints a list of all the commands!'
})
## end commands command

## start react command
async def react_function(message, client, args):
    try:
        print('nope')
        #haha gotem
        #Doesn't work in ch, so put it down in an if-else with the dad jokes + easter eggs
    except Exception as e:
        print(e)
ch.add_command({
    'trigger': '/react',
    'function': react_function,
    'args_num': 0,
    'args_name': [],
    'description': 'Reacts to the message sent!'
})
## end react command

## start hello command
def hello_function(message, client, args):
    try:
        return 'Hey {}'.format(message.author)
    except Exception as e:
        return e
ch.add_command({
    'trigger': '/hello',
    'function': hello_function,
    'args_num': 0,
    'args_name': [],
    'description': 'Will respond hello to the caller'
})
## end hello command

## start lenny command
def lenny_function(message, client, args):
    try:
        return random.choice(lenny)
    except Exception as e:
        return e
ch.add_command({
    'trigger': '/face',
    'function': lenny_function,
    'args_num': 0,
    'args_name': [],
    'description': 'Replies with a random face'
})
## end face command

## start tarot command
def tarot_function(message, client, args):
    try:
        count = 0
        reading = 'Your cards: '
        shuffle(tarotDeck.deck)
        while count < 3:
            card = tarotDeck.deck[count]
            inverse = randint(0,1)
            if inverse:
                reading += card + ' inverted, '
            else:
                if count == 2:
                    reading += card
                else:
                    reading += card +', '
            count += 1
        return reading
    except Exception as e:
        return e
ch.add_command({
    'trigger': '/tarot',
    'function': tarot_function,
    'args_num': 0,
    'args_name': [],
    'description': 'Gives you a three-card tarot reading'
})
## end tarot command

## start maze command
def maze_function(message, client, args):
    try:
        print('ha gotem')
    except Exception as e:
        return e
ch.add_command({
    'trigger': '/maze',
    'function': maze_function,
    'args_num': 0,
    'args_name': [],
    'description': 'Solve a maze'
})
## end maze command
'''
## start tic tac toe command
def tic_function(message, client, args):
    try:
        if message.content == '/tic':
            return ticTacToe.buildBoard(ticTacToe.baseBoard)
        else:
            return ticTacToe.playerMove(args[0],args[1])
    except Exception as e:
        return e
ch.add_command({
    'trigger': '/tic',
    'function': tic_function,
    'args_num': 2,
    'args_name': ['x', 'y'],
    'description': 'Play tic tac toe against the bot'
})
## end tic tac toe command
'''
# bot is ready
@client.event
async def on_ready():
    try:
        print(client.user.name)
        print(client.user.id)
    except Exception as e:
        print(e)

# on new message
@client.event
async def on_message(message):
    # if the message is from the bot itself ignore it
    if message.author == client.user:
        pass
    elif 'I\'m ' in message.content or 'i\'m ' in message.content:
        await message.channel.send(dadJoke.makeDadJoke(message.content))
    elif '/react' in message.content:
        await message.add_reaction('🇳')
        await asyncio.sleep(0.01)
        await message.add_reaction('🇴')
    elif '/maze' in message.content:
        #had to put it here, doesn't work in ch, since the return function ends the command
        mazeMsg = await message.channel.send(maze.buildMaze(maze.baseMaze))
        for x in mazeEmoji:
            await mazeMsg.add_reaction(x)
            await asyncio.sleep(0.01)
    elif '/tic' in message.content:
        #had to put it here, doesn't work in ch, since the return function ends the command
        ticTacToe.reset(ticTacToe.progressBoard)
        ticMsg = await message.channel.send(ticTacToe.buildBoard(ticTacToe.baseBoard))
        for x in ticEmoji:
            await ticMsg.add_reaction(x)
            await asyncio.sleep(0.01)
    else:
        # try to evaluate with the command handler
        try:
            await ch.command_handler(message)
        # message doesn't contain a command trigger
        except TypeError as e:
            #Returns what comes back from the generic responses
            await message.channel.send(genResponses.messageGet(message.content))

'''
    
    '''

mazeEmoji = ['⬅','⬆','⬇','➡','🔄']
ticEmoji = ['1️⃣','2️⃣','3️⃣','4️⃣','5️⃣','6️⃣','7️⃣','8️⃣','9️⃣']

#'⬅','⬆','⬇','➡','🔄'
@client.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    emoji = reaction.emoji

    if user.bot:
        return

    if emoji in mazeEmoji:
        await message.edit(content=maze.arraySwap(emoji))
    elif emoji in ticEmoji:
        await message.edit(content=ticTacToe.playerMove(emoji))
        await asyncio.sleep(0.5)
        await message.edit(content=ticTacToe.botMove())
    else:
        return

# start bot
client.run(token)