# SpotiPie References and Usage
Project Content
- `main.py`: This file contains all the required api calls to fetch details from Spotify
- `.env`: Add your Client ID and Client Secret in this file.
    - Create an app to get the above details: https://developer.spotify.com/dashboard/applications
- `user_auth_token.py`: This is used to generate token(Implicit Grant Flow)
- `utility/utility_spotipy.py`: This contains useful utility funtions to perform repetitive tasks and some other important funtions like `playlist_genres()`

Spotify Client Credential Flow
- https://developer.spotify.com/documentation/general/guides/authorization/client-credentials/

Spotify Implicit Grant Flow
- https://developer.spotify.com/documentation/general/guides/authorization/implicit-grant/
- This method was used to generate user authorization token. This is necessary if we need to perform User specific actions, like getting User Playlists.
- `user_auth_token.py` script generates the required token.
- Checkout `Authorization Scopes`
    - https://developer.spotify.com/documentation/general/guides/authorization/scopes/

Ideas
- Flow to get track, artist and genres details.
    - Get Saved/Liked Tracks or Playlist' tracks
    - The playlist item will have `track`, `artist`, `popularity`, `duration`, `added_at`
    - Get genres of each `artist`
    - Prepare a `dict` of all the above captured details.