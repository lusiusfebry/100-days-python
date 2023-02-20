from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("detach", True)

# service = ChromeService(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com")

