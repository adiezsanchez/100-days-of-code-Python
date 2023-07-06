from bs4 import BeautifulSoup
import requests

# Date and URL for the Billboard TOP100
DATE = "2014-05-31"
URL = f"https://www.billboard.com/charts/hot-100/{DATE}/"
# Spotify auth credentials
CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

list_of_songs = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")

song_titles = [song.getText().strip() for song in list_of_songs]

print(song_titles)


