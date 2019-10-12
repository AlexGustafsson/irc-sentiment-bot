#!/usr/bin/env python3
import time
import os
import csv
import re
import random
import sys

from connector import IRC

dirname = os.path.dirname(__file__)

server = os.getenv('IRC_SERVER', None)
port = os.getenv('IRC_PORT', 6697)
channel = os.getenv('IRC_CHANNEL', '#random')
nick = os.getenv('IRC_NICK', 'sentiment-bot')
user = os.getenv('IRC_USER', 'sentiment-bot')
gecos = os.getenv('IRC_GECOS', 'Sentiment Bot v0.1.1 (github.com/AlexGustafsson/irc-sentiment-bot)')

if server == None:
    print('Cannot start the bot without a given server')
    sys.exit()

afinn = {}
with open(os.path.join(dirname, './afinn.csv'), 'r') as file:
    for lineNumber, line in enumerate(file):
       values = line.split(' ')
       word = ' '.join(values[0:-1])
       value = int(values[-1])
       afinn[word] = value

def handle_help():
    irc.send(channel, 'I perform a simple sentiment analysis on your messages and respond with emojis')

def analyze_message(sender, body):
    words = [''.join(y for y in x if y.isalnum()) for x in body.split(' ')]
    points = sum([afinn[word.lower()] if word.lower() in afinn else 0 for word in words])
    if points >= 5:
        irc.send('emoji-bot', '(happy)')
    elif points <= -5:
        irc.send('emoji-bot', '(tableflip)')

def handle_message(message):
    sender, type, target, body = message
    if type == 'PRIVMSG':
        print(body)
        if body == '{0}: help'.format(nick):
            handle_help()
        else:
            analyze_message(sender, body)


irc = IRC()

print('Bot: Connecting to {0}:{1} as {2} ({3})'.format(server, port, user, nick))
irc.connect(server, port, user, nick, gecos)
print('Bot: Connected to {0}'.format(server))

print('Bot: Joining channel {0}'.format(channel))
irc.join(channel)

print('Bot: Starting event loop')
while True:
    message = irc.retrieveMessage()
    handle_message(message)
