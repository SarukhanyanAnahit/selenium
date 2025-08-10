from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://news.google.com/")
time.sleep(2)

title = driver.find_element(By.XPATH, "//article[@class='IBr9hb']//a[@class='gPFEn']").text
when=driver.find_element(By.CLASS_NAME, 'hvbAAd').text

print(f"Title: {title}")
print(f"When: {when}")

driver.quit()