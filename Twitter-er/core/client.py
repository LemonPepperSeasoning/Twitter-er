import tweepy

class TweepyClient:
    def __init__(self,consumer_key,consumer_secret,access_token,access_token_secret):
        # auth = tweepy.OAuth2BearerHandler(BEARER_TOKEN)
        # self.api = tweepy.API(auth)
        # self.client = tweepy.Client(bearer_token=BEARER_TOKEN)
        self.client = tweepy.Client(
            consumer_key=consumer_key, consumer_secret=consumer_secret,
            access_token=access_token, access_token_secret=access_token_secret
        )
        
    def make_a_tweet(self,msg):
        # response = self.client.get_me()
        # print(response)
        response = self.client.create_tweet(text=msg)
        print(f"https://twitter.com/user/status/{response.data['id']}")
