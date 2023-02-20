from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)

URL = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(URL)
# number_of_articles = driver.find_element(By.XPATH,value='//*[@id="articlecount"]/a[1]')
number_of_articles = driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
#Click number of articles
# number_of_articles.click()

# Click by link
all_portals = driver.find_element(By.LINK_TEXT,value="Cyclone Gabrielle")
# all_portals.click()

#Click search, type in the search coloumn and enter
search = driver.find_element(By.NAME,value="search")
search.send_keys("python")
search.send_keys(Keys.ENTER)


