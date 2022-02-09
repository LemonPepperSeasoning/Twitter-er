import os
import tweepy
import openai

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
        
        
class OpenaiClient:
    def __init__(self,openai_key):
        openai.organization = "org-Ap7v6umG9OoBxoHFmUONp6ie"
        openai.api_key = openai_key
        # print( openai.Engine.list() )
        
    def QnA(self):
        response = openai.Completion.create(
            engine="text-davinci-001",
            prompt="I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is human life expectancy in the United States?\nA: Human life expectancy in the United States is 78 years.\n\nQ: Who was president of the United States in 1955?\nA: Dwight D. Eisenhower was president of the United States in 1955.\n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ: Where is the Valley of Kings?\nA:",
            temperature=0,
            max_tokens=100,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\n"]
        )
        print(response)