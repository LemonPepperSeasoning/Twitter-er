import tweepy

class TweepyClient:
    def __init__(self,BEARER_TOKEN):
        auth = tweepy.OAuth2BearerHandler(BEARER_TOKEN)
        api = tweepy.API(auth)