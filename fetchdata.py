# Import the necessary methods from tweepy library
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream

# The twitter streaming api is used to download twitter messages in real time
# Variables that contain the user credentials to access twitter api
# API authorization is required to access Twitter streams.

# Using the stream api has 3 steps

access_token = "4811117574-Hmc2VgTR2toeXT4oypBRulueodBj7YzyBeNgZLB"
access_token_secret = "LVmlKaPUn5ya8KHIlPQX1hw4k9XFtyjv9IGZWK2fTKeRB"
consumer_secret = "8mtIwOUX2OPVaWKBfjlxuO8RSJhAIYBFoxuti4pXj8yeeNvtF2"
consumer_key = "PTPdsBsIsEDLcbdbpOvzcxDpq"

# 1.Create a class inheriting the StreamListener
# 2.Using that class create a Stream Object
class MyStreamListener(tweepy.StreamListener):
    def on_data(self, data):
        tweet_data = data.split('"text":"')[1].split('"source":')[0]
        if tweet_data[0:2] != 'RT' and "https:" not in tweet_data:
            # ie if it is not a re tweet (RT stands for re tweet)
            # some tweets may have sarcasm in the link , we don't need them
            print tweet_data
            # write in a csv (comma separated values) file.
            new_file = open('twitter_sarcasm.csv', 'a')
            new_file.write(tweet_data)
            new_file.write('\n')
            new_file.close()
            return True

    def on_error(self, status):
        print status


# twitter authentication  and connection to twitter streaming api
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# 3.Connect to twitter api using the stream
twitter_stream = Stream(auth, MyStreamListener())
# Filter all the streams containing #sarcasm or #sarcastic and only english tweets
twitter_stream.filter(track=["#sarcasm", "#sarcastic"])

