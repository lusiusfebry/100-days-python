from bs4 import BeautifulSoup
import requests

song = input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{song}"
# url = f"https://www.billboard.com/charts/hot-100/2023-02-11"


response = requests.get(url=url)

soup = BeautifulSoup(response.text,"html.parser")
song_list= []
# song_dict = {}

box = soup.find_all("div",{"class":"o-chart-results-list-row-container"})

for music_chart in box:
    song_dict={}
    song_dict["rank"] = music_chart.find("span",{"class":"c-label a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet"}).text.strip()

    song_dict["title"] = music_chart.find("h3",{"class":"c-title"}).text.strip()

    artist_list = music_chart.find("li", class_="lrv-u-width-100p")
    song_dict["artist"] = artist_list.find("span",class_="c-label").text.strip()
    song_list.append(song_dict)

print(song_list)
