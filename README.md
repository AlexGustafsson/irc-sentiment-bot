# IRC Sentiment Bot
### A Dockerized IRC Bot written in Python 3 for performing sentiment analysis and responding with emojis via emoji-bot
***

### Setting up

##### Quickstart

```Bash
# Clone the repository
git clone https://github.com/AlexGustafsson/irc-sentiment-bot
# Enter the directory
cd irc-sentiment-bot
# Build the image
./build-docker.sh
# Start the image
docker run -d -e IRC_SERVER='irc.example.org' --restart always axgn/irc-sentiment-bot
```

### Documentation

#### Running with Docker

```Bash
docker run -d \
-e IRC_SERVER='irc.example.org' \
-e IRC_PORT='6697' \
-e IRC_CHANNEL='#random' \
-e IRC_NICK='sentiment-bot' \
-e IRC_USER='sentiment-bot' \
-e IRC_GECOS='Sentiment Bot v0.2.3 (github.com/AlexGustafsson/irc-sentiment-bot)' \
axgn/irc-sentiment-bot
```

#### Invoking via IRC

To see help messages send `sentiment-bot: help` in the channel where the bot lives.

The bot reads all messages sent in the configured channel and sends `emoji-bot: (happy)` if a certain threshold is met for positivity and `emoji-bot: (tableflip)` if a negative threshold is met.

### Contributing

Any contribution is welcome. If you're not able to code it yourself, perhaps someone else is - so post an issue if there's anything on your mind.

###### Development

Clone the repository:
```
git clone https://github.com/AlexGustafsson/irc-emoji-bot && cd irc-emoji-bot
```

### Disclaimer

_Although the project is very capable, it is not built with production in mind. Therefore there might be complications when trying to use the bot for large-scale projects meant for the public. The bot was created to easily send emojis in IRC channels and as such it might not promote best practices nor be performant._
