import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from spotipy.util import prompt_for_user_token
from setup import setupEnv

setupEnv()

soa = SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    username=os.getenv("SPOTIPY_USER"),
    scope="user-library-read",
)

sp = spotipy.Spotify(auth_manager=soa)
results = sp.search(q="weezer", limit=20)
for idx, track in enumerate(results["tracks"]["items"]):
    print(idx, track["name"])
