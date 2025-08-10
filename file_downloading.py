import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}\\downloads"
}
chrome_options.add_experimental_option("prefs", prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("http://the-internet.herokuapp.com/download")
time.sleep(3)
files = driver.find_elements("xpath", "//div[@id='content']//a")
for file in files:
    file.click()
    time.sleep(3)