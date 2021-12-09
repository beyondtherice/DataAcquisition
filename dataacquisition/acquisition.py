"""analyzes given spotify song"""
import spotipy

sp = spotipy.Spotify()
from pprint import pprint
from time import sleep
from dotenv import load_dotenv
import pandas as pd
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

load_dotenv()

def authentication(cid: str,secret: str,username: str):    
    scope = "user-library-read,user-read-playback-state,user-modify-playback-state"
    authorization_url = "https://accounts.spotify.com/authorize"
    token_url = "https://accounts.spotify.com/api/token"
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
                    
    return sp

def analysis(track: str,sp):
    analysis = sp.audio_analysis(track)
    features = sp.audio_features(track)
    features_df = pd.DataFrame(data=features, columns=features[0].keys())
    beats_df = pd.DataFrame(data=analysis["beats"])
    segments_df = pd.DataFrame(data=analysis["segments"])
    bars_df = pd.DataFrame(data=analysis["bars"])
    tatums_df = pd.DataFrame(data=analysis["tatums"])
    
    return beats_df

if __name__ == "__main__":
    username = os.environ.get("CLIENT_USERNAME")
    cid = os.environ.get("CLIENT_ID")
    secret = os.environ.get("CLIENT_SECRET")
    track = "spotify:track:6yIjtVtnOBeC8SwdVHzAuF"
    sp = authentication(cid,secret,username)
    beats = analysis(track,sp)
    beatStart = beats["start"]

    F = open("osutesting.osu", 'a')
    for index, j in beats.iterrows():
        print("256,192,",beatStart[index]*1000,",5,4,0:0:0:0:\n", sep='')
        F.write("256,192,"+ str(beatStart[index]*1000) +",5,4,0:0:0:0:\n")
    F.close()
