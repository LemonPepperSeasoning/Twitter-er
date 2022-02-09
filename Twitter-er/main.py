import requests
import os
from config import BEARER_TOKEN, API_SECRET_KEY,CLIENT_SECRET,API_KEY,CLIENT_KEY,OPENAI_KEY
from core.client import TweepyClient, OpenaiClient

def bearer_oauth(r):
    # To set your environment variables in your terminal run the following line:
    # export 'BEARER_TOKEN'='<your_bearer_token>'
    # bearer_token = os.environ.get("BEARER_TOKEN")
    r.headers['Authorization'] =  "Bearer {}".format(BEARER_TOKEN)
    return r

def test():
    URL = 'https://api.twitter.com/2/compliance/jobs'
    headers = {}
    response = requests.get(f"{URL}/{id}", auth=bearer_oauth, headers=headers)
    print(response)

def make_one_tweet():
    tweeter_client = TweepyClient(
        API_KEY,
        API_SECRET_KEY,
        CLIENT_KEY,
        CLIENT_SECRET
        )
    
    openai_client = OpenaiClient(
        OPENAI_KEY
        )
    
    msg = openai_client.QnA()
    tweeter_client.make_a_tweet(msg)
    
def init_client():

    tweeter_client = TweepyClient(
        API_KEY,
        API_SECRET_KEY,
        CLIENT_KEY,
        CLIENT_SECRET
        )
    
    openai_client = OpenaiClient(
        OPENAI_KEY
        )
    
    # msg = openai_client.QnA()
    # tweeter_client.make_a_tweet(msg)
    
    # new_client.make_a_tweet("First tweet via bot")
 
def main():
    init_client()
    
    # test()
    
if __name__ == "__main__":
    main()