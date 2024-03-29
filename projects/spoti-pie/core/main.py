from dotenv import load_dotenv
import os
import base64
import requests
import json
from core.logging import Logger
import sys

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_pwd = os.getenv("CLIENT_SECRET")

logging = Logger().logger

def get_token():
    """
    Generate server-to-server authentication token `(Client Credential Flow)`.

    Returns:
        :access_token (str)
    """
    url = "https://accounts.spotify.com/api/token"

    auth_string = client_id + ":" + client_pwd
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes)

    headers = {
        "Authorization" : "Basic " + str(auth_base64, "utf-8"),
        "Content-Type" : "application/x-www-form-urlencoded"
    }

    body = {
        "grant_type" : "client_credentials"
    }

    authorization_response = requests.post(url, headers=headers, data=body)
    if authorization_response.status_code >=200 and authorization_response.status_code <=299:
        access_token = json.loads(authorization_response.content)["access_token"]
        return access_token
    else:
        logging.error("%s: %s", get_token.__name__, authorization_response.content)
        sys.exit()

def get_auth_header(token):
    """
    Returns the headers required to make request calls.

    Parameters:
        :token (str)

    Returns:
        :headers (dict)
    """
    return {"Authorization": "Bearer "+ token, "Content-Type": "application/json"}

def search_artist(artist_name):
    """
    Search and get the top 1 artist's info that matches the given `artist_name`.

    Parameters:
        :artist_name (str) 

    Returns:
        :artist info (dict)
    """
    url = "https://api.spotify.com/v1/search"
    token = get_token() 
    headers = get_auth_header(token=token)
    query = f"?q={artist_name}&type=artist&limit=1"
    query_url = url + query

    response = requests.get(url=query_url, headers=headers)
    if response.status_code >=200 and response.status_code <=299:
        return json.loads(response.content)["artists"]["items"][0]
    else:
        logging.error("%s: %s", search_artist.__name__, response.content)
        sys.exit()

def get_artist(artist_id):
    """
    Get the artist info.

    Parameters:
        :artist_id (str)

    Returns:
        :artist info (dict)
    """
    token = get_token()
    url = f"https://api.spotify.com/v1/artists/{artist_id}"
    headers = get_auth_header(token=token)

    response = requests.get(url=url, headers=headers)
    if response.status_code >=200 and response.status_code <=299:
        logging.debug("Fetched details of %s (artist)", response.json()['name'])
        return response.json()
    else:
        logging.error("%s: %s", get_artist.__name__, response.content)
        sys.exit()

def get_artist_top_tracks(artist_id, country_code):
    """
    Get top 10 tracks of an artist in a given country.

    Parameters:
        :artist_id (str)
        :country_code (str): Country code in uppercase. `Example: India = IN, USA = US`

    Returns:
        :tracks (dict): key=track id, value={track_name, track_popularity}
    """
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country={country_code}"
    token = get_token()
    headers = get_auth_header(token=token)
    tracks = dict()
    response = requests.get(url=url, headers=headers)
    if response.status_code >=200 and response.status_code <=299:
        for i in response.json()["tracks"]:
            tracks[i["id"]] = {"track":i["name"], "popularity":i["popularity"]}
        return tracks
    else:
        logging.error("%s: %s", get_artist_top_tracks.__name__, response.content)
        sys.exit()

def get_track(track_id):
    """
    Get track info.

    Parameters:
        :track_id (str)

    Returns:
        :track info (dict)
    """
    token = get_token()
    url = f"https://api.spotify.com/v1/tracks/{track_id}"
    headers = get_auth_header(token=token)

    response = requests.get(url=url, headers=headers)
    if response.status_code >=200 and response.status_code <=299:
        return response.json()
    else:
        logging.error("%s: %s", get_track.__name__, response.content)
        sys.exit()

def get_track_audio_features(track_id):
    """
    Get the track audio features.

    Parameters:
        :track_id (str)

    Returns:
        :audio features (dict)
    """
    token = get_token()
    url = f"https://api.spotify.com/v1/audio-features/{track_id}"
    headers = get_auth_header(token=token)

    response = requests.get(url=url, headers=headers)
    if response.status_code >=200 and response.status_code <=299:
        return response.json()
    else:
        logging.error("%s: %s", get_track_audio_features.__name__, response.content)
        sys.exit()

def get_track_audio_analysis(track_id):
    """
    Get the track audio analysis.

    Parameters:
        :track_id (str)

    Returns:
        :audio analysis (dict)
    """
    url = f"https://api.spotify.com/v1/audio-analysis/{track_id}"
    token = get_token()
    headers = get_auth_header(token=token)

    response = requests.get(url=url, headers=headers)
    if response.status_code >=200 and response.status_code <=299:
        return response.json()
    else:
        logging.error("%s: %s", get_track_audio_analysis.__name__, response.content)
        sys.exit()

def get_songs_artist(track_id):
    """
    Get the artist id(s) of a track.

    Parameters:
        :track_id (str)

    Returns:
        :artist_ids (list): List of all the artists of a given track.
    """
    token = get_token()
    artist_ids = []
    track_info = get_track(token=token, track_id=track_id)
    for i in track_info["artists"]:
        if i["id"] not in artist_ids:
            artist_ids.append(i["id"])
    return artist_ids

def get_genres(artist_id):
    """
    Returns the genre of the artist.

    Parameters:
        :artist_id (str)

    Returns:
        :genres (list)
    """
    token = get_token()
    artist_details = get_artist(artist_id=artist_id)
    genres = artist_details["genres"]
    logging.debug("Fetched Genres of %s: %s", artist_details['name'], genres)
    return genres

def get_user_playlists(user_auth_token):
    """
    Get the User's Playlist details (Public Playlists).

    Parameters:
        :user_auth_token (str): Generated using `user_auth_token.py`. For more details check <https://developer.spotify.com/documentation/general/guides/authorization/implicit-grant/>
    
    Returns:
        :playlist_details (list): Playlist Name, Playlist ID & Number of Songs
    """
    url = "https://api.spotify.com/v1/me/playlists"
    headers = get_auth_header(token=user_auth_token)
    response = requests.get(url=url, headers=headers)
    playlists_details = []
    if response.status_code >=200 and response.status_code <=299:
        for i in response.json()["items"]:
            playlists_details.append([i["name"], i["id"], i["tracks"]["total"]])
        return playlists_details
    else:
        logging.error("%s: %s", get_user_playlists.__name__, response.content)
        sys.exit()

def get_user_playlist_items(user_auth_token, playlist_id):
    """
    Get the User's playlist info.

    Parameters:
        :user_auth_token (str): Token generated using `user_auth_token.py`. For more details check <https://developer.spotify.com/documentation/general/guides/authorization/implicit-grant/>.
        :playlist_id (str): Get this using `get_user_playlists`

    Returns:
        :User Playlist details (list[dict])
    """
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = get_auth_header(token=user_auth_token)
    response = requests.get(url=url, headers=headers)
    if response.status_code >=200 and response.status_code <=299:
        return response.json()["items"]
    else:
        logging.error("%s: %s", get_user_playlist_items.__name__, response.content)
        sys.exit()

def get_users_saved_tracks(token):
    """
    Get the User's Liked Songs

    Parameters:
        :token (str): User authorization token, having `user-library-read` scope.

    Returns:
        :liked_tracks (list)
    """
    def request_saved_track(url, headers):
        response = requests.get(url=url, headers=headers)
        if response.status_code >=200 and response.status_code <=299:
            logging.debug("Getting saved tracks. url: %s", response.json()["next"])
            return response.json()
        else:
            logging.error("%s: %s", get_users_saved_tracks.__name__, response.content)
            sys.exit()

    liked_tracks = []
    url = "https://api.spotify.com/v1/me/tracks"
    headers = get_auth_header(token=token)
    url_query = f"{url}?offset=0&limit=50"
    response = request_saved_track(url=url_query, headers=headers)
    for track in response["items"]:
        liked_tracks.append(track)
    while response["next"] != None:
        response =request_saved_track(url=response["next"], headers=headers)
        for track in response["items"]:
            liked_tracks.append(track)
        logging.debug("Fetched %s tracks.", len(liked_tracks))
    return liked_tracks

def get_my_top_tracks(token, term="short_term"):
    """
    
    """
    url = f"https://api.spotify.com/v1/me/top/tracks"
    url_query = f"{url}?time_range={term}&offset=0&limit=10"
    headers = get_auth_header(token=token)
    response = requests.get(url=url_query, headers=headers)
    if response.status_code >=200 and response.status_code <=299:
        top10_tracks = []
        for i in response.json()["items"]:
            top10_tracks.append({"track":i})
        return top10_tracks
    else:
        logging.error("%s: %s", get_my_top_tracks.__name__, response.content)
        sys.exit()

def get_my_top_artists(token, term="short_term"):
    """
    
    """
    url = f"https://api.spotify.com/v1/me/top/artists"
    url_query = f"{url}?time_range={term}&offset=0&limit=10"
    headers = get_auth_header(token=token)
    response = requests.get(url=url_query, headers=headers)
    top10_artists = []
    if response.status_code >=200 and response.status_code <=299:
        for count, i in enumerate(response.json()["items"]):
            artist = {}
            artist["artist_rank"] = count+1
            artist["id"] = i["id"]
            artist["name"] = i["name"]
            artist["popularity"] = i["popularity"]
            artist["artist_url"] = i["external_urls"]["spotify"]
            artist["genres"] = i["genres"]
            if len(i["images"]) >= 2:
                artist["image"] = i["images"][1]["url"]
            top10_artists.append(artist)
        return top10_artists
    else:
        logging.error("%s: %s", get_my_top_artists.__name__, response.content)
        sys.exit()

