import spotipy
from spotipy.oauth2 import SpotifyOAuth
import yaml


with open('spotify-client.yaml', 'r') as f:
    client = yaml.safe_load(f)

auth = SpotifyOAuth(client_id=client['client_id'],
                    client_secret=client['client_secret'],
                    scope='user-read-currently-playing',
                    redirect_uri='http://localhost:8080')

sp = spotipy.Spotify(auth_manager=auth)
results = sp.currently_playing()

print(results['item']['name'])
