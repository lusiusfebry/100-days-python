from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


URL = "https://orteil.dashnet.org/cookieclicker/"

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)
driver.get(URL)

time.sleep(20)
language = driver.find_element(By.XPATH,value='//*[@id="langSelect-EN"]')
language.click()

# big_cookie = driver.find_element(By.XPATH,value='//*[@id="bigCookie"]')
time.sleep(10)
# big_cookie = driver.find_element(By.CSS_SELECTOR,value="#bigCookie")
# # time.sleep(20)
# big_cookie.click()
# big_cookie.click()

def click_big_cookie(num):
    # time.sleep(10)

    big_cookie = driver.find_element(By.CSS_SELECTOR,value="#bigCookie")
    for i in range (num):
        big_cookie.click()


while True:
    click_big_cookie(100)
    try:
        items = driver.find_element(By.CLASS_NAME,value="enabled")
        for item in items[::-1]:
            items.click()
    except:
        print("Not enough cookies")


