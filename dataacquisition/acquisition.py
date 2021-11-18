from dotenv import load_values
import os

load_dotenv()
#environment variables

#just use blah = os.getenv("WHATEVER_ENV_VARIABLE_IS")
import spotipy

sp = spotipy.Spotify()
from pprint import pprint
from time import sleep

import matplotlib.pyplot as plt
import pandas as pd
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

# setting up authorization
cid = ""
secret = ""

username = "your_account_number"
scope = "user-library-read,user-read-playback-state,user-modify-playback-state"  # check the documentation
authorization_url = "https://accounts.spotify.com/authorize"
token_url = "https://accounts.spotify.com/api/token"
redirect_uri = ""

token = util.prompt_for_user_token(
    username, scope, client_id="", client_secret="", redirect_uri=""
)

client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


analysis = sp.audio_analysis("")
features = sp.audio_features("")
features_df = pd.DataFrame(data=features, columns=features[0].keys())
beats_df = pd.DataFrame(data=analysis["beats"])
segments_df = pd.DataFrame(data=analysis["segments"])
bars_df = pd.DataFrame(data=analysis["bars"])
tatums_df = pd.DataFrame(data=analysis["tatums"])

blahblahblah = dotenv_values("CLIENT_ID")
plt.figure(figsize=(20, 30))
plt.xticks(rotation=90)

print(segments_df)
print(blahblahblah)
