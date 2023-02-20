from selenium import webdriver
from selenium.webdriver.common.by import By

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)

url = "https://www.python.org/"


driver.get(url)
event_time = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")

event = {}

for n in range(len(event_time)):
    event[n] = {
        "time" : event_time[n].text,
        "name" : event_name[n].text
    }

print(event)




driver.quit()

