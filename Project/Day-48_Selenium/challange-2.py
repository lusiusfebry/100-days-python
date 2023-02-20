from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)

URL = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(URL)
# number_of_articles = driver.find_element(By.XPATH,value='//*[@id="articlecount"]/a[1]')
number_of_articles = driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
print(number_of_articles.text)
driver.quit()