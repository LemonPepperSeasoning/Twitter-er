import requests
import os
from config import BEARER_TOKEN
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
    new_client = TweepyClient(BEARER_TOKEN)
 
def main():
    init_client()
    # test()
    
if __name__ == "__main__":
    main()