"""analyzes given spotify song"""
import os

import matplotlib.pyplot as plt
import pandas as pd
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyClientCredentials

# environment variables
load_dotenv()

sp = spotipy.Spotify()

cid = os.environ.get("CLIENT_ID")
secret = os.environ.get("CLIENT_SECRET")

SCOPE = "user-library-read,user-read-playback-state,user-modify-playback-state"
AUTHORIZATION_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token" # nosec

client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# in quotes should be track uri, i.e. spotify:track:6yIjtVtnOBeC8SwdVHzAuF
analysis = sp.audio_analysis("")
features = sp.audio_features("")
features_df = pd.DataFrame(data=features, columns=features[0].keys())
beats_df = pd.DataFrame(data=analysis["beats"])
segments_df = pd.DataFrame(data=analysis["segments"])
bars_df = pd.DataFrame(data=analysis["bars"])
tatums_df = pd.DataFrame(data=analysis["tatums"])

plt.figure(figsize=(20, 30))
plt.xticks(rotation=90)

print(segments_df)
