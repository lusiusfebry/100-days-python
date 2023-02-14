# import requests
# from bs4 import BeautifulSoup
#
# url = "https://news.ycombinator.com/news"
# response = requests.get(url)
#
# soup = BeautifulSoup(response.content, "html.parser")
#
# first_article = soup.find("tr", {"class": "athing"})
# title = first_article.find("a", {"class": "storylink"}).text
# link = first_article.find("a", {"class": "storylink"})["href"]
#
# print(f"Title: {title}")
# print(f"Link: {link}")


import requests
from bs4 import BeautifulSoup

url = "https://www.billboard.com/charts/hot-100/2023-02-11/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# songs = soup.find_all("li", class_="chart-list__element display--flex")
# print(songs)

# for song in songs:
#     rank = song.find("span", class_="chart-element__rank__number").text
#     title = song.find("span", class_="chart-element__information__song text--truncate color--primary").text
#     artist = song.find("span", class_="chart-element__information__artist text--truncate color--secondary").text
#     print(rank, title, artist)
songs = soup.find("li", class_="lrv-u-width-100p")
title = songs.find("h3",class_="c-title").text.strip()
artist = songs.find("span",class_="c-label")
print(artist)

# print(songs)