"""analyzes given spotify song"""
import os
import spotipy
from dotenv import load_dotenv
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials

def authentication(cid: str,secret: str) -> any:
    """Sets up the client authentication"""
    client_credentials_manager = SpotifyClientCredentials(client_id=cid,
            client_secret=secret)
    spot_auth = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return spot_auth

def analysis_func(track: str,spot_auth) -> any:
    """analyses the trck useing the spotify api"""
    analysis = spot_auth.audio_analysis(track)
    # features = spot_auth.audio_features(track)
    # features_df = pd.DataFrame(data=features, columns=features[0].keys())
    beats_df = pd.DataFrame(data=analysis["beats"])
    # segments_df = pd.DataFrame(data=analysis["segments"])
    # bars_df = pd.DataFrame(data=analysis["bars"])
    # tatums_df = pd.DataFrame(data=analysis["tatums"])
    return beats_df

def beatmaker(beats):
    """appends the osu file with data"""
    beat_start = beats["start"]
    with open("osutesting.osu", 'a', encoding="utf-8") as beatmap:
        for index, _ in beats.iterrows():
            print("256,192,",beat_start[index]*1000,",5,4,0:0:0:0:\n", sep='')
            beatmap.write("256,192,"+ str(beat_start[index]*1000) +",5,4,0:0:0:0:\n")

def main():
    """declared variables and calls other funvtions"""
    load_dotenv()
    cid: str = os.environ.get("CLIENT_ID")
    secret: str = os.environ.get("CLIENT_SECRET")

    spot_auth = authentication(cid,secret)

    track = "spotify:track:6yIjtVtnOBeC8SwdVHzAuF"
    beats = analysis_func(track,spot_auth)
    beatmaker(beats)

if __name__ == "__main__":
    main()
