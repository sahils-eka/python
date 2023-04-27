from dotenv import load_dotenv
from core.logging import Logger
import os
import random
import string
import requests
import sys

# To get User's profile details we need to use Implicit Grant Flow

load_dotenv()

client_id = os.getenv("CLIENT_ID")

logging = Logger().logger

def user_authorization():
    url = "https://accounts.spotify.com/authorize"
    redirect_uri = "http://localhost:8000/callback"
    state = "".join(random.choice(string.ascii_lowercase) for i in range(11))
    scope = "user-follow-modify user-library-read user-top-read user-read-playback-position user-follow-read playlist-read-private"
    query = f"?client_id={client_id}&response_type=token&redirect_uri={redirect_uri}&state={state}&scope={scope}"
    if len(client_id) <=2:
        logging.error("%s: cliend_id not defined.", user_authorization.__name__)
        sys.exit()    
    response = requests.get(url=url+query)
    if response.status_code >=200 and response.status_code <=299:
        print(response.url)
    else:
        logging.error("%s: %s", user_authorization.__name__, response.content)
        sys.exit()

# user_authorization()