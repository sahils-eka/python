# SpotiPie References and Usage
Project Structure
- core
    - `main.py`: This module contains all the api calls required to fetch the details from Spotify.
    - `logging.py`: This module is for implementing logging in the project.
- files
    -   `golden`: This directory contains all the final output files (will change with the development of more features)
- utility
    - `user_auth_token.py`: This is used to generate the token(Implicit Grant Flow)
    - `utility_spotipy.py`: This contains useful utility funtions to perform repetitive tasks and some other important actions (ex:`playlist_genres()`)
    - `json_file_generator.py`: As the name suggests, used to create the json files.
- `.env`: 
    - Add your Client ID and Secret in this file.
    - Create an app to get the above details: https://developer.spotify.com/dashboard/applications

Spotify Client Credential Flow
- https://developer.spotify.com/documentation/general/guides/authorization/client-credentials/

Spotify Implicit Grant Flow
- https://developer.spotify.com/documentation/general/guides/authorization/implicit-grant/
- This method ise used to generate the user authorization token. This is necessary if we need to perform the User specific actions, like getting User Playlists.
- `user_auth_token.py` script generates the required token.
- Checkout `Authorization Scopes`
    - https://developer.spotify.com/documentation/general/guides/authorization/scopes/

Ideas
- Flow to get track, artist and genres details.
    - Get Saved/Liked Tracks or Playlist' tracks
    - The playlist item will have `track`, `artist`, `popularity`, `duration`, `added_at`
    - Get genres of each `artist`
    - Prepare a `dict` of all the above captured details.
