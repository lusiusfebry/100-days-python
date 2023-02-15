from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

date = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{date}"
# url = f"https://www.billboard.com/charts/hot-100/2023-02-11"


response = requests.get(url=url)

soup = BeautifulSoup(response.text,"html.parser")
song_names= []
# song_dict = {}

box = soup.find_all("div",{"class":"o-chart-results-list-row-container"})



for music_chart in box:
    # song_dict={}
    # song_dict["rank"] = music_chart.find("span",{"class":"c-label a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet"}).text.strip()
    #
    # song_dict["title"] = music_chart.find("h3",{"class":"c-title"}).text.strip()
    #
    # artist_list = music_chart.find("li", class_="lrv-u-width-100p")
    # song_dict["artist"] = artist_list.find("span",class_="c-label").text.strip()

    # song_list.append(song_dict)
    title = music_chart.find("h3", {"class": "c-title"}).text.strip()
    song_names.append(title)
    # print(title)

# spotify auth
Client_ID = os.getenv("spotify_id")
Client_Secret = os.getenv("spotify_secret")
redirect_url = "http://example.com"
playlist = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=Client_ID,
        client_secret=Client_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
# print(user_id)



#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

