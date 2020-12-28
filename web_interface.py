import os

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
from spotipy.util import prompt_for_user_token
import setup


setup.setupEnv()

soa = SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    username=os.getenv("SPOTIPY_USER"),
    scope=setup.getScope(),
)

sp = spotipy.Spotify(auth_manager=soa)
pl = sp.current_user_playlists()
items = pl["items"]

import pandas as pd

## challenge here is unrolling the datatypes to work simply with what I want.
## TODO - find a structure for the data
pd.DataFrame(data=pl.items)
