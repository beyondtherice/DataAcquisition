"""analyzes given spotify song"""
import os
import spotipy
from dotenv import load_dotenv
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

def authentication(cid: str,secret: str,username: str) -> any:
    """Sets up the client authentication"""
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return spot_auth

def analysis(track: str,spot_auth) -> any:
    """analyses the trck useing the spotify api"""
    # analysis = sp.audio_analysis(track)
    features = sp.audio_features(track)
    # features_df = pd.DataFrame(data=features, columns=features[0].keys())
    beats_df = pd.DataFrame(data=analysis["beats"])
    # segments_df = pd.DataFrame(data=analysis["segments"])
    # bars_df = pd.DataFrame(data=analysis["bars"])
    # tatums_df = pd.DataFrame(data=analysis["tatums"])
    return beats_df

def beatmaker(beats):
    """appends the osu file with data"""
    beat_start = beats["start"]
    with open("osutesting.osu", 'a') as beatmap:
        for index, _ in beats.iterrows():
            print("256,192,",beatStart[index]*1000,",5,4,0:0:0:0:\n", sep='')
            beatmap.write("256,192,"+ str(beatStart[index]*1000) +",5,4,0:0:0:0:\n")

def main():
    """declared variables and calls other funvtions"""
    load_dotenv()
    username: str = os.environ.get("CLIENT_USERNAME")
    cid: str = os.environ.get("CLIENT_ID")
    secret: str = os.environ.get("CLIENT_SECRET")

    spot_auth = authentication(cid,secret,username)

    track = "spotify:track:6yIjtVtnOBeC8SwdVHzAuF"
    beats = analysis(track,spot_auth)
    beatmaker(beats)

if __name__ == "__main__":
    main()
