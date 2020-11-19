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
                        return self.client.send_message(message.channel, str(command['function'](message, self.client, args)))
                        break
                    else:
                        if len(args) >= command['args_num']:
                            return self.client.send_message(message.channel, str(command['function'](message, self.client, args)))
                            break
                        else:
                            return self.client.send_message(message.channel, 'command "{}" requires {} argument(s) "{}"'.format(command['trigger'], command['args_num'], ', '.join(command['args_name'])))
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
async def react_command(message, client, args):
    try:
        await message.add_reaction('🇳')
        await asyncio.sleep(0.1)
        await message.add_reaction('🇴')
    except Exception as e:
        print(e)
ch.add_command({
    'trigger': '/react',
    'function': react_command,
    'args_num': 0,
    'args_name': [],
    'description': 'Reacts to the message sent!'
})
## end react command

## start hello command
def hello_function(message, client, args):
    try:
        return 'Hello {}, Argument One: {}'.format(message.author, args[0])
    except Exception as e:
        return e
ch.add_command({
    'trigger': '!hello',
    'function': hello_function,
    'args_num': 1,
    'args_name': ['string'],
    'description': 'Will respond hello to the caller'
})
## end hello command

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
    else:
        # try to evaluate with the command handler
        try:
            await ch.command_handler(message)
        # message doesn't contain a command trigger
        except TypeError as e:
            #Returns what comes back from the generic responses
            await message.channel.send(genResponses.messageGet(message.content))

# start bot
client.run(token)