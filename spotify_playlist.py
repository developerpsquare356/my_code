
#######################  Resources

# https://developer.spotify.com/dashboard/create
# https://www.billboard.com/charts/hot-100/2009-01-01/
# 


from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


client_id='enter your client id'
client_secret='enter your client id'



date="2025-08-09"
url=f"https://www.billboard.com/charts/hot-100/{date}/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

response=requests.get(url=url,headers=header)
data=response.text
soup=BeautifulSoup(data,"html.parser")
song_web=soup.select("li ul li h3")
songs=[song.getText().strip() for song in song_web]



sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://open.spotify.com/",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]
print(user_id)


song_uris = []
year = '2025'
for song in range(0,4):
    result = sp.search(q=f"track:{songs[song]} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
