#!/usr/bin/env python3
import os
import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from connector import IRC

dirname = os.path.dirname(__file__)

server = os.getenv('IRC_SERVER', None)
port = os.getenv('IRC_PORT', 6697)
channel = os.getenv('IRC_CHANNEL', '#random')
nick = os.getenv('IRC_NICK', 'sentiment-bot')
user = os.getenv('IRC_USER', 'sentiment-bot')
gecos = os.getenv('IRC_GECOS', 'Sentiment Bot v0.2.3 (github.com/AlexGustafsson/irc-sentiment-bot)')

lastMessageValence = None

if server is None:
    print('Cannot start the bot without a given server')
    sys.exit()


def handle_help():
    irc.send(channel, 'I perform a simple sentiment analysis on your messages and respond with emojis')


def analyze_message(sender, body):
    global lastMessageValence

    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(body)
    if vs["compound"] >= 0.6:
        irc.send('emoji-bot', '(happy)')
        lastMessageValence = vs
    elif vs["compound"] <= -0.6:
        irc.send('emoji-bot', '(tableflip)')
        lastMessageValence = vs


def handle_debug():
    if lastMessageValence is not None:
        compound = 'compound: {}'.format(lastMessageValence['compound'])
        debug = ', '.join(['"{}": {}'.format(text, valence) for text, valence in lastMessageValence['debug']])
        irc.send(channel, '{}. {}'.format(compound, debug))


def handle_message(message):
    sender, type, target, body = message
    if type == 'PRIVMSG':
        if body == '{0}: help'.format(nick):
            handle_help()
        elif body == '{0}: debug'.format(nick):
            handle_debug()
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
