import tweepy
import json
# Authentication details. To  obtain these visit dev.twitter.com
consumer_key='IULTiP66SFv65iOR6i6QrjakS'
consumer_secret='s0MIwgVumwf3nA5aqRzl4CfvyyQLGShu1jfcqEVl4T6RYoL6oW'
access_token='3134102994-ts3sxIWkMPv9heG6VYaGYSfQebq87D9Sd3OlAQa'
access_token_secret='0ZfCukuYUowK6PJJRimkFGT9eAqZK0tNhNcM4iCqTGfeB'
# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print ('@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))
        print ('')
        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print ("Showing all new tweets for #programming:")

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['bowl'])
