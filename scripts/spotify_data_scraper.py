import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import os
from datetime import datetime
import time

#get env variables
SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID", "your_client_id")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET", "your_client_secret")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI", "http://localhost:8888/callback")

#set scope to recent tracks
scope = "user-read-recently-played user-top-read"

#authenticate and create client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI,
    scope=scope
))

#extract data from recent tracks
def get_recent_tracks(limit=50):
    results = sp.current_user_recently_played(limit=limit)
    data = []

    for item in results['items']:
        track = item['track']
        played_at = item['played_at']
        artist = track['artists'][0]
        artist_id = artist['id']
        try:
            artist_info = sp.artist(artist_id)
            genres = artist_info.get('genres', [])
        except:
            genres = []
        data.append({
            'track_name': track['name'],
            'artist_name': track['artists'][0]['name'],
            'album': track['album']['name'],
            'played_at': played_at,
            'duration_ms': track['duration_ms'],
            'track_id': track['id'],
            'release_date': track['album']['release_date'],
            'genres': ', '.join(genres)
        })
        time.sleep(.1)

    df = pd.DataFrame(data)
    df['played_at'] = pd.to_datetime(df['played_at'])
    df['duration_min'] = df['duration_ms'] / 60000
    return df

#save to csv
if __name__ == "__main__":
    df_recent = get_recent_tracks()
    today = datetime.today().strftime('%Y-%m-%d')
    output_file = f"raw_data/recent_tracks_{today}.csv"
    os.makedirs("data", exist_ok=True)
    df_recent.to_csv(output_file, index=False)
    print(f"Saved {len(df_recent)} records to {output_file}")
