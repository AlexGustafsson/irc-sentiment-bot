FROM python:3-alpine

RUN addgroup -g 6697 -S irc-bot && \
    adduser -u 6697 -S irc-bot -G irc-bot

USER irc-bot
WORKDIR /irc-bot

COPY requirements.txt .
RUN python3 -m pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "-m", "bot.main"]
