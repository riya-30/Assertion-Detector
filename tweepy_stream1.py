import tweepy
import json
import time

# Authentication details. To  obtain these visit dev.twitter.com
consumer_key="mALNtyLb6i94DvZ6TAvsG6NM0"
consumer_secret="ycD9XAKd5m9fIVHjBksZKffvVJlTYqX43JZLybnCDEM1TF6zm6"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="994812906-FgoPvF7EwFOB0Mv4y058f4IBgBpLJI41tkNUDF1v"
access_token_secret="n6Umf0UsNlV76Y2HBntSwwptfCAcuguZq1ZRpdAtMn3Xh"
# This is the listener, resposible for receiving data
def check(status):
    datafile = file('C:\Users\User\Desktop\Growth Handles.txt', 'r')
    found = False
    for line in datafile:
        if status.user.screen_name in line:
            found = True
            break
    return found
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        print ('@%s: %s' % (decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore')))
        print ('')
        return True

    def on_status(self,status):
        if check(status) :
            pass
        else:
            api = tweepy.API(auth)
            Reply='@' +status.user.screen_name +' Check out Tomorrowland 2014 Setlist'
            api.update_status(status=Reply)
            time.sleep(15*60)
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
    stream.filter(track=['hi'])
