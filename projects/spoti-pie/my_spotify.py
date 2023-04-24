import main as spotipy
from utility.utility_spotipy import UtilitySpotiPy
import json
from utility.csv_generator import CsvFileGenerator
from utility.json_file_generator import JsonFileGenerator

user_auth_token = ""  # Generate this using `user_auth_token.py`

# liked_songs = spotipy.get_users_saved_tracks(token=user_auth_token)

# playlist_id = spotipy.get_user_playlists(user_auth_token=user_auth_token)[0][1]

# playlist_items = spotipy.get_user_playlist_items(user_auth_token=user_auth_token, playlist_id=playlist_id)

# print(playlist_items[0])

liked_items = spotipy.get_users_saved_tracks(token=user_auth_token)

items = UtilitySpotiPy.get_tracks_artists_genres(playlist_items=liked_items)
print(json.dumps(items))

fileds = ["id", "name", "added_at", "duration_sec", "popularity", "artists", "genres"]

file = CsvFileGenerator(fileds=fileds, items=items)

file2 = JsonFileGenerator(items=items)
file2.json_generator()
file.csv_generator()
