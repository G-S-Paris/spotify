import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv("TestifyClientID"),
        client_secret=os.getenv("TestifyClientSecret"),
        redirect_uri="http://127.0.0.1:9090",
        scope="user-library-read",
    )
)
results = sp.search(q="weezer", limit=20)
for idx, track in enumerate(results["tracks"]["items"]):
    print(idx, track["name"])
