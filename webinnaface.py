# import requests

# r = requests.get()

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id="id",
        client_secret="secret",
        redirect_uri="http://127.0.0.1:9090",
        scope="user-library-read",
    )
)
