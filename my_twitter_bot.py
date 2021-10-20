import tweepy
import config

CONSUME_KEY = config.CONSUME_KEY
CONSUME_SECRET = config.CONSUME_SECRET
ACCESS_KEY = config.ACCESS_KEY
ACCESS_SECRET = config.ACCESS_SECRET

auth = tweepy.OAuthHandler(CONSUME_KEY, CONSUME_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

for mention in mentions:
    print(str(mention.id) + '-' + mention.text)
