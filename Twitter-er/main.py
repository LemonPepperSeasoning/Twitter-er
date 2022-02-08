import requests
import os
from config import BEARER_TOKEN, API_SECRET_KEY,CLIENT_SECRET,API_KEY,CLIENT_KEY
from core.client import TweepyClient

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

def init_client():

    new_client = TweepyClient(
        API_KEY,
        API_SECRET_KEY,
        CLIENT_KEY,
        CLIENT_SECRET
        )
    
    # new_client.make_a_tweet("First tweet via bot")
 
def main():
    init_client()
    # test()
    
if __name__ == "__main__":
    main()