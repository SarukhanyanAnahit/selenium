from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get('https://www.youtube.com/')
time.sleep(3)

search = driver.find_element(By.NAME, 'search_query')
search.click()
search.send_keys('Lana Del Rey')

button = driver.find_element(By.CLASS_NAME, 'ytSearchboxComponentSearchButton')
button.click()
time.sleep(10)

videos = driver.find_elements(By.XPATH, '//ytd-video-renderer')

for video in videos[:5]:
    title = video.find_element(By.ID, 'video-title').get_attribute('title')
    duration= video.find_element(By.XPATH,  './/span[contains(@class, "ytd-thumbnail-overlay-time-status-renderer") and contains(text(), ":")]')
    print(title, duration)

