from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.com/")
button = driver.find_element('xpath', '//div[@class="a-row"]//button[@type="submit"]')
button.click()
time.sleep(2)

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)
time.sleep(3)

laptops = driver.find_elements(By.XPATH, '//div[@role="listitem"]')
count = 0

for laptop in laptops:
    try:
        name = laptop.find_element(By.XPATH, './/h2').text
        rating = laptop.find_element(By.XPATH, ".//span[@class='a-icon-alt']").text
        print(f"Name: {name}")
        print(f"Rating: {rating}")
        count += 1
        if count == 10:
            break
    except:
        continue

driver.quit()
