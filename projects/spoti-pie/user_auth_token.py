from dotenv import load_dotenv
import os
import random
import string
import requests

# To get User's profile details we need to use Implicit Grant Flow

load_dotenv()

client_id = os.getenv("CLIENT_ID")

def user_authorization():
    url = "https://accounts.spotify.com/authorize"
    redirect_uri = "http://localhost:8000/callback"
    state = "".join(random.choice(string.ascii_lowercase) for i in range(11))
    scope = "user-follow-modify user-library-read user-top-read user-read-playback-position user-follow-read playlist-read-private"
    query = f"?client_id={client_id}&response_type=token&redirect_uri={redirect_uri}&state={state}&scope={scope}"
    response = requests.get(url=url+query)
    print(response.url)

user_authorization()