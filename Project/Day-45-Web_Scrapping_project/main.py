import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(url=URL)
soup = BeautifulSoup(response.text,"html.parser")
movies = []

movies_title = soup.find_all(name="h3",class_="title")
for title in movies_title:
    movies.append(title.text)

movie_list = movies[::-1]

with open("movie_list.txt","w",encoding="utf8") as file:
    for movie in movie_list:
        file.write(f"{movie}" + "\n")

