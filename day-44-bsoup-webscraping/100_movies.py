from bs4 import BeautifulSoup
import requests

URL = 'https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")

title_tag = soup.find_all(name="h3", class_="title")
# Without list comprehension
list_of_movies = []
for title in title_tag:
    movie_title = title.getText()
    encoded_mt = str(movie_title.encode("utf-8"))
    encoded_mt = encoded_mt.replace("b", "")
    encoded_mt = encoded_mt.replace("'", "")
    encoded_mt = encoded_mt.replace('"', "")
    list_of_movies.append(encoded_mt)
#Using list comprehension
#list_of_movies = [movie.getText() for movie in title_tag]
list_of_movies.reverse()
print(list_of_movies)



with open("./files/100movies.txt", mode="w", encoding="ISO-8859-1") as file:
    file.write("List of Movies")

for movie in list_of_movies:
    with open("./files/100movies.txt", mode="a") as file:
        file.write(f"\n{movie}")