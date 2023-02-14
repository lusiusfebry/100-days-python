from bs4 import BeautifulSoup
import requests

url = "https://news.ycombinator.com/news"

response = requests.get(url=url)
yc_web_page=response.text

soup = BeautifulSoup(yc_web_page,"html.parser")
article_tag = soup.find_all("span", {"class": "titleline"})

# print(article_tag)
article_text_list=[]
article_link_list=[]
for article in article_tag:


    article_text = article.get_text()
    article_text_list.append(article_text)

    article_link = article.find("a").get("href")
    article_link_list.append(article_link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all("span", {"class":"score"})]
# print(article_text_list)
# print(article_link_list)
# print(article_upvote)

largest_number = max(article_upvote)
largest_index=article_upvote.index(largest_number)
#
#
print (article_text_list[largest_index])
print(article_link_list[largest_index])
