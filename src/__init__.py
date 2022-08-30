import spotipy
from spotipy.oauth2 import SpotifyOAuth
import yaml


with open('spotify-client.yaml', 'r') as f:
    client = yaml.safe_load(f)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=client['client_id'],
                              client_secret=client['client_secret'],
                              scope='app-remote-control',
                              redirect_uri='https://127.0.0.1'))
results = sp.currently_playing()

print(results)
