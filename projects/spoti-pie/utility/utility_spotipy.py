import main as spotipy

class UtilitySpotiPy:

    def enrichment_genres(tracks_and_artists):
        """
        Utility function to add `genres` to the track info.

        Parameters:
            :tracks_and_artists (list): List structure same as what is returned from `get_tracks_artists_genres()` 
        
        Returns:
            :tracks_and_artists (list): For now enriching the track_and_artist dict by adding `genres` info.
        """
        all_artist_genre = {}
        for i in tracks_and_artists:
            genres = []
            for j in i["artists"]:
                if j["artist_id"] not in all_artist_genre:
                    # Creating this dict(artist_id, genre) to avoid duplicate request calls to the spotify server
                    all_artist_genre[j["artist_id"]] = spotipy.get_genres(artist_id=j["artist_id"])
                genres.extend([genre for genre in all_artist_genre[j["artist_id"]] if genre not in genres])
            i["genres"] = genres
        return tracks_and_artists

    def get_tracks_artists_genres(playlist_items):
        """
        Utility funtion to get relevant info of a Playlist.

        Parameters:
            :playlist_items (list): List of track details (can be fetched by using `get_user_playlist_items()` or `get_users_saved_tracks()`)

        Returns:
            :tracks_artists_genres (list): List of Dict - track_id, track_name, added_at, duration_sec, popularity, artists(artist, artist_id), genres
        """
        tracks_and_artists = []
        for count, i in enumerate(playlist_items):
            track = {}
            track["track_number"] = count
            track["id"] = i["track"]["id"]
            track["name"] = i["track"]["name"]
            if "added_at" in i:
                track["added_at"] = i["added_at"]
            track["duration_sec"] = i["track"]["duration_ms"] * 0.001
            track["popularity"] = i["track"]["popularity"]
            track["artists"] = [{"artist":i["name"], "artist_id":i["id"]} for i in i["track"]["artists"]]
            if len(i["track"]["album"]["images"]) >= 2:
                track["image"] = i["track"]["album"]["images"][1]["url"]
            else:
                track["image"] = ""
            track["preview_url"] = i["track"]["preview_url"]
            tracks_and_artists.append(track)
        tracks_artists_genres = UtilitySpotiPy.enrichment_genres(tracks_and_artists=tracks_and_artists)
        return tracks_artists_genres

    def get_unique_trackids(tracks_and_artists):
        """
        Utility funtion to get the Unique track ids from the user's track and artist dict.
        
        Parameters:
            :tracks_and_artists (dict): Get this using `get_playlist_tracks_artists()`

        Returns:
            :unique_track_ids (list)
        """
        unique_track_ids = []
        for i in tracks_and_artists:
            if tracks_and_artists[i]["id"] not in unique_track_ids:
                unique_track_ids.append(tracks_and_artists[i]["id"])
        return unique_track_ids


    def get_unique_artistids(tracks_and_artists):
        """
        Utility funtion to get the Unique artist ids from the user's track and artist dict.
        
        Parameters:
            :tracks_and_artists (dict): Get this from `get_playlist_tracks_artists()`

        Returns:
            :unique_artist_ids (list)
        """
        unique_artist_ids = []
        for i in tracks_and_artists:
            for j in tracks_and_artists[i]["artists"]:
                if j["artist_id"] not in unique_artist_ids:
                    unique_artist_ids.append(j["artist_id"])
        return unique_artist_ids

    def playlist_genres(self, playlist_details, user_auth_token):
        """
        Utility funtion to get the playlist's genre details.

        Parameters:
            :playlist_details (list): Get this from `get_user_playlists()`
            :user_auth_token (str)

        Returns:
            :Playlist Genre (dict): Dictionary containing Playlist's name, id, num_of_songs, genres(name & count)
        """
        playlist_id = playlist_details[1]
        all_artist_ids = []
        genres = []
        
        playlist_items = spotipy.get_user_playlist_items(user_auth_token=user_auth_token, playlist_id=playlist_id)
        tracks_and_artists = self.get_playlist_tracks_artists(playlist_items=playlist_items)
        tracks_artists = UtilitySpotiPy.get_playlist_tracks_artists(playlist_item=playlist_items)
        track_ids = UtilitySpotiPy.get_unique_trackids(tracks_and_artists=tracks_artists)
        for i in track_ids:
            track_artistis = spotipy.get_songs_artist(track_id=i)
            for id in track_artistis:
                all_artist_ids.append(id)

        # Creating an artist dict(artist_id, count) to avoid duplicate request calls to spotify server
        artists_dict = dict([(i,all_artist_ids.count(i)) for i in all_artist_ids])

        for i in artists_dict:
            for genre in spotipy.get_genres(artist_id=i):
                for count in range(int(artists_dict[i])):
                    genres.append(genre)
        genre_count = dict([(genre, genres.count(genre)) for genre in genres])
        return {"name":playlist_details[0], "id":playlist_details[1], "num_of_songs":playlist_details[2], "genres":genre_count}
