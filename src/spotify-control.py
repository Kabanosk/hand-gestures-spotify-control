import spotipy
from spotipy.oauth2 import SpotifyOAuth
import yaml


class SpotifyUser:
    def __init__(self, is_playing = False, volume = 50):
        with open('spotify-client.yaml', 'r') as f:
            client = yaml.safe_load(f)

        auth = SpotifyOAuth(client_id=client['client_id'],
                            client_secret=client['client_secret'],
                            scope='streaming',
                            redirect_uri='http://localhost:8080')
        self.api = spotipy.Spotify(auth_manager=auth)

        self.volume = volume
        self.is_playing = is_playing
        self.api.volume(self.volume)



    def change_playback(self):
        if self.is_playing:
            self.api.pause_playback()
        else :
            self.api.start_playback()
        self.is_playing = not self.is_playing

    
    def next_track(self):
        self.api.next_track()
        self.is_playing = True

    def previous_track(self):
        self.api.previous_track()
        self.is_playing = True


    def volume_up(self):
        self.volume = min(volume+10, 100)
        self.api.volume(self.volume)

    def volume_down(self):
        self.volume = max(volume-10, 0)
        self.api.volume(self.volume)
