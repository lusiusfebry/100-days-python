from selenium import webdriver
from selenium.webdriver.common.by import By
# Chrome setup
option = webdriver.ChromeOptions()
# driver = webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=option)

URL = "https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=sr_1_1?crid=1VL8U25B9X3TF"



# Locating element
driver.get("https://www.python.org/")

# price = driver.find_element(By.CLASS_NAME,value="a-price-whole")
# print(price.text)

name = driver.find_element(By.NAME,value="q")
print(name.get_attribute("placeholder"))

logo = driver.find_element(By.CLASS_NAME,value="python-logo")
print(logo.size)

css_selector = driver.find_element(By.CSS_SELECTOR,value=".documentation-widget a")
print(css_selector.text)

x_path = driver.find_element(By.XPATH,value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(x_path.text)
driver.quit()


