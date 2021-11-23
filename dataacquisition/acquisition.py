'''Gets information for the beats of a song from spotify'''
#from pprint import pprint
#from time import sleep
import matplotlib.pyplot as plt
import pandas as pd
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials#, SpotifyOAuth
sp = spotipy.Spotify()

# setting up authorization
CID = ""
SECRET = ""

USERNAME = "your_account_number"
SCOPE = "user-library-read,user-read-playback-state,user-modify-playback-state"
# check the documentation
AUTHORIZATION_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
REDIRECT_URI = ""

token = util.prompt_for_user_token(
    USERNAME, SCOPE, client_id="", client_secret="", redirect_uri=""
)

client_credentials_manager = SpotifyClientCredentials(
    client_id=CID, client_secret=SECRET
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
