import main as spotipy
from utility.utility_spotipy import UtilitySpotiPy
import json
from utility.csv_generator import CsvFileGenerator
from utility.json_file_generator import JsonFileGenerator

user_auth_token = "BQCyHTGm3Xoup23Oq5y66q48xbu3a8xc4W1OIfYHSnWhQQa1v7jRivtNdIOlvIqffYpvl0_l3n4YZa-BWKSoRk3kniOVq7zV5rJVvyE5tanH90dUZY--kP3y-2rcl8cjVLLMOcusZkCTVmVzBCDTwOZqScGY_-lIyA1NQoRFIzBmXWydQO4HBgVe"

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
