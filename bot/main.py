import csv
import logging
import random
from argparse import ArgumentParser

from irc import IRC
from irc.messages import IRCMessage

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

positives = [
    "(˶‾᷄ ⁻̫ ‾᷅˵)",
    "(っˆڡˆς)",
    "♥‿♥",
    "(づ｡◕‿‿◕｡)づ",
    "٩( ๑╹ ꇴ╹)۶",
    "ᕕ( ᐛ )ᕗ",
    "٩(^‿^)۶",
    "＼(＾O＾)／"
]

negatives = [
    "(ノ ゜Д゜)ノ ︵ ┻━┻",
    "(;´༎ຶД༎ຶ`)",
    "( ͡° ʖ̯ ͡°)",
    "(ノಠ益ಠ)ノ彡┻━┻",
    "t(ಠ益ಠt)",
    "༼ ༎ຶ ෴ ༎ຶ༽",
    "┻━┻ ︵ヽ(`Д´)ﾉ︵ ┻━┻"
]

def main() -> None:
    """Main entrypoint of the bot."""
    # Configure the default logging format
    logging.basicConfig(
        format="[%(asctime)s] [%(levelname)-5s] %(message)s",
        level=logging.INFO,
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Create an argument parser for parsing CLI arguments
    parser = ArgumentParser(description="An IRC bot providing sentiment analysis and reactions using ASCII emojis")

    # Add parameters for the server connection
    parser.add_argument("-s", "--server", required=True, type=str, help="The server to connect to")
    # Add optional parameters for the server connection
    parser.add_argument("-p", "--port", default=6697, type=int, help="The port to connect to")
    parser.add_argument("--use-tls", default=True, type=bool, help="Whether or not to use TLS")
    parser.add_argument("-t", "--timeout", default=300, type=float, help="Connection timeout in seconds")

    # Add optional parameters for authentication etc.
    parser.add_argument("-u", "--user", default="sentiment-bot", help="Username to use when connecting to the IRC server")
    parser.add_argument("-n", "--nick", default="sentiment-bot", help="Nick to use when connecting to the IRC server")
    parser.add_argument("-g", "--gecos", default="Sentiment Bot v1.0.1 (github.com/AlexGustafsson/irc-sentiment-bot)")
    parser.add_argument("-c", "--channel", required=True, action='append', help="Channel to join. May be used more than once")

    # Parse the arguments
    options = parser.parse_args()

    # Create an IRC connection
    irc = IRC(
        options.server,
        options.port,
        options.user,
        options.nick,
        timeout=options.timeout,
        use_tls=options.use_tls
    )

    irc.connect()

    # Connect to specified channels
    for channel in options.channel:
        irc.join(channel)

    # The last analyzed result
    lastMessageValence = None

    # Handle all messages
    for message in irc.messages:
        if not isinstance(message, IRCMessage):
            continue

        target = message.author if message.target == options.nick else message.target

        if message.message == "{}: help".format(options.nick):
            irc.send_message(target, "I perform a simple sentiment analysis on your messages and respond with emojis")
            irc.send_message(target, "You can debug the sentiment analysis of the last message like so:")
            irc.send_message(target, "{}: debug".format(options.nick))
        elif message.message == "{}: debug".format(options.nick):
            if lastMessageValence is not None:
                compound = "compound: {}".format(lastMessageValence["compound"])
                debug = ", ".join(["'{}': {}".format(text, valence) for text, valence in lastMessageValence["debug"]])
                irc.send_message(target, "{}. {}".format(compound, debug))
        else:
            analyzer = SentimentIntensityAnalyzer()
            scores = analyzer.polarity_scores(message.message)
            if scores["compound"] >= 0.6:
                irc.send_message(target, random.choice(positives))
                lastMessageValence = scores
            elif scores["compound"] <= -0.6:
                irc.send_message(target, random.choice(negatives))
                lastMessageValence = scores


if __name__ == "__main__":
    main()
