from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service=Service(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get('https://the-internet.herokuapp.com/status_codes')
links = driver.find_elements(By.XPATH, "//ul/li/a")
for i in range(len(links)):
    links[i].click()
    time.sleep(2)
    driver.back()
    time.sleep(2)