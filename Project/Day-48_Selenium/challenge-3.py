from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=option)

URL = "http://secure-retreat-92358.herokuapp.com/"
driver.get(URL)

fname = driver.find_element(By.NAME,value="fname")
fname.send_keys("Febry")
lname = driver.find_element(By.NAME,value="lname")
lname.send_keys("maro")
email = driver.find_element(By.NAME,value="email")
email.send_keys("test@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR,value="form button")
submit.send_keys(Keys.ENTER)

