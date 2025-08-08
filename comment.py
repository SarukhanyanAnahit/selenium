from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.youtube.com/")
time.sleep(3)

search_box = driver.find_element(By.NAME, 'search_query')
search_box.click()
search_box.send_keys('Adele')
search_button = driver.find_element(By.CLASS_NAME, 'ytSearchboxComponentSearchButton')

search_button.click()
time.sleep(5)

video = driver.find_element(By.XPATH, '(//ytd-video-renderer//a[@id="video-title"])[1]')
video.click()
time.sleep(5)

comments = driver.find_elements(By.XPATH, '//ytd-comment-thread-renderer')
time.sleep(5)

for comment in comments[:5]:
        author = comment.find_element(By.XPATH, './/a[@id="author-text"]').text
        content = comment.find_element(By.XPATH, './/yt-formatted-string[@id="content-text"]').text
        print(f"Author: {author}")
        print(f"Content: {content}")
time.sleep(5)
driver.quit()