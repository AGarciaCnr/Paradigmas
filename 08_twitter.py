# coding=utf-8

# Autenticación con Twitter y seguimiento con Twitter Streaming API
from rx import create, operators
import tweepy
from tweepy import Stream

from printer import Printer
from secret import consumer_key, access_token, consumer_secret, access_token_secret
import json

def mi_observable(keywords):
    def observe_tweets(o, s):
        class TweetStream (tweepy.Stream):
            def on_data(self, data):
                o.on_next(data)

            def on_error(self, status):
                o.on_error(status)


        stream = TweetStream(consumer_key, consumer_secret,access_token, access_token_secret)
        stream.filter(track=keywords)

    return create(observe_tweets)


keywords = ['rusia']

mi_observable(keywords).pipe(
    operators.map(lambda txt: json.loads(txt)),
    operators.map(lambda d: f'{d["user"]["name"]}: {d["text"]}')
).subscribe(Printer())

