import spotipy

sp = spotipy.Spotify()
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import pandas as pd
import matplotlib.pyplot as plt
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep

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


plt.figure(figsize=(20, 30))
plt.xticks(rotation=90)

print(segments_df)
