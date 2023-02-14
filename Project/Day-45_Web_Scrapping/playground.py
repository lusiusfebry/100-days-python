from bs4 import BeautifulSoup
import lxml

with open("website.html",encoding="utf8") as file:

    contents = file.read()

# print(contents)
soup = BeautifulSoup(contents,"html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())
# print(soup.a)
# print(soup.li)

achor_tags = soup.find_all(name="a")
print(achor_tags)

for tag in achor_tags:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1",id="name")
print(heading)

section_heading = soup.find(name="h3",class_="heading")
print(section_heading)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)


headings=soup.select(".heading")
print(headings)

