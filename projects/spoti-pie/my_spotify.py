import core.main as spotipie
from utility.utility_spotipy import UtilitySpotiPy
from utility.json_file_generator import JsonFileGenerator
import os
from dotenv import load_dotenv

load_dotenv()
spotipie_utils = UtilitySpotiPy()
json_utils = JsonFileGenerator()

user_auth_token = "" # user_auth_token.py

top10_tracks_items = spotipie.get_my_top_tracks(token=user_auth_token, term="long_term")
top10_tracks_items = spotipie_utils.get_tracks_artists_genres(playlist_items=top10_tracks_items)
top10_tracks_items = spotipie_utils.enrichment_audio_feature(song_items=top10_tracks_items)

file = os.getenv("JSON_FILE_NAME")
json_utils.json_generator(items=top10_tracks_items, file_name=file)
