import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/news"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

first_article = soup.find("tr", {"class": "athing"})
title = first_article.find("a", {"class": "storylink"}).text
link = first_article.find("a", {"class": "storylink"})["href"]

print(f"Title: {title}")
print(f"Link: {link}")