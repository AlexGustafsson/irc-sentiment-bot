#!/usr/bin/env bash

# Please see the README for more information
docker run \
  --env IRC_SERVER='irc.example.org' \
  --env IRC_PORT='6697' \
  --env IRC_CHANNEL='#random' \
  --env IRC_NICK='sentiment-bot' \
  --env IRC_USER='sentiment-bot' \
  --env IRC_GECOS='Sentiment Bot v0.2.1 (github.com/AlexGustafsson/irc-sentiment-bot)' \
  --name irc-sentiment-bot \
  --detach \
  --restart always \
  --cpus=0.05 \
  --memory=10MB \
  axgn/irc-sentiment-bot
