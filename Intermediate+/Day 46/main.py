import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

date = input("What date would you like to travel to? (YYYY-MM-DD)\n")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
data = response.text
soup = BeautifulSoup(data,"html.parser")
all_songs = soup.select("li ul li h3")
titles = [song.getText().strip() for song in all_songs]

sp = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=config("CLIENT_ID"),
        client_secret=config("CLIENT_SECRET"),
        show_dialog=True,
        cache_path="Day 46\\token.txt",
        username="rynlkl"
      )
    )

user_id = sp.current_user()["id"]

year = date.split("-")[0]
song_uris = []

for t in titles:
    value = sp.search(q=f"track:{t} year:{year}",type="track")
    try:
       uri = value["tracks"]["items"][0]["uri"]
       song_uris.append(uri)
    except IndexError:
        print(f"{t} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id,name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print("Done")
