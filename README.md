# IRC Sentiment Bot
### A Dockerized IRC Bot written in Python 3 for performing sentiment analysis and responding with ASCII emojis
***

### Setting up

##### Quickstart

```shell
# Clone the repository
git clone https://github.com/AlexGustafsson/irc-sentiment-bot
# Enter the directory
cd irc-sentiment-bot
# Run
python3 -m bot.main --server irc.example.com
```

You can also run the container using Docker, like so:

```shell
# Build the image
docker build -t axgn/irc-sentiment-bot:latest .

# Run
docker run axgn/irc-sentiment-bot --server irc.example.com --channel "#random"
```

### Documentation

#### Running with Docker

```shell
docker run axgn/irc-emoji-bot --server irc.example.com --channel "#random"
```

The image is stateless and based on Alpine and is roughly 90MB in size. While running, the container usually uses 0% of the CPU and roughly 7MB of RAM. During load it uses about 0.20% CPU and while starting about 0.4% on a single core and an unchanged amount of RAM.

To prevent any unforseen events, one can therefore limit the container's resources by using the flags `--cpus=0.05` and `--memory=10MB` which should both leave some head room.

#### Invoking via IRC

To see help messages send `sentiment-bot: help` in the channel where the bot lives.

The bot reads all messages sent in the configured channels (or direct messages) and sends and appropriate emoji if a certain threshold is met for positivity or negativity.

### Contributing

Any contribution is welcome. If you're not able to code it yourself, perhaps someone else is - so post an issue if there's anything on your mind.

###### Development

Clone the repository:
```
git clone https://github.com/AlexGustafsson/irc-sentiment-bot && cd irc-sentiment-bot
```

### Disclaimer

_Although the project is very capable, it is not built with production in mind. Therefore there might be complications when trying to use the bot for large-scale projects meant for the public. The bot was created to easily send emojis in IRC channels and as such it might not promote best practices nor be performant._
