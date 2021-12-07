"""analyzes given spotify song"""
mport spotipy

sp = spotipy.Spotify()
from pprint import pprint
from time import sleep


import pandas as pd
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

def authentication(cid,secret,username):    
    scope = "user-library-read,user-read-playback-state,user-modify-playback-state"
    authorization_url = "https://accounts.spotify.com/authorize"
    token_url = "https://accounts.spotify.com/api/token"
    redirect_uri = uri
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
                    
    return sp

def analysis(track,sp):
    analysis = sp.audio_analysis(track)
    features = sp.audio_features(track)
    features_df = pd.DataFrame(data=features, columns=features[0].keys())
    beats_df = pd.DataFrame(data=analysis["beats"])
    segments_df = pd.DataFrame(data=analysis["segments"])
    bars_df = pd.DataFrame(data=analysis["bars"])
    tatums_df = pd.DataFrame(data=analysis["tatums"])
    
    return beats_df

if __name__ == "__main__":
    username =  CLIENT_USERNAME
    cid = CLIENT_ID
    secret = CLIENT_ID
    track = "spotify:track:6yIjtVtnOBeC8SwdVHzAuF"
    sp = authentication(cid,secret,uri,username)
    beats = analysis(track,sp)
    beatStart = beats["start"]

    F = open("osutesting.osu", 'a')
    for index, j in beats.iterrows():
        print("256,192,",beatStart[index]*1000,",5,4,0:0:0:0:\n", sep='')
        F.write("256,192,"+ str(beatStart[index]*1000) +",5,4,0:0:0:0:\n")
    F.close()
