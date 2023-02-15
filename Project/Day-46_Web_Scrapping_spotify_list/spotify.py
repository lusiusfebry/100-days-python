import spotipy
from spotipy.oauth2 import SpotifyOAuth

Client_ID = "56bd7272ff1b4e11ae38dbf963424e22"
Client_Secret = "ef18534ce9594119bf98f7e17ec2db1a"
redirect_url = "http://example.com"
playlist = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=Client_ID,
                                               client_secret=Client_Secret,
                                               redirect_uri=redirect_url,
                                               scope=playlist,
                                               cache_path="token.txt",
                                               show_dialog=True
                                               ))


test = sp.current_user()["id"]
print(test)