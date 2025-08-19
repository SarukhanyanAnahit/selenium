import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://www.amazon.com/")
time.sleep(2)
input = driver.find_element(By.ID, "twotabsearchtextbox")
input.send_keys('laptop')
input.send_keys(Keys.ENTER)
time.sleep(3)

add_to_cart = driver.find_element("xpath", "//button[@name='submit.addToCart']").click()

saved = driver.get_cookies()
print('saced:', saved)
time.sleep(3)

driver.delete_all_cookies()
print('deleted:', driver.get_cookies())
driver.refresh()
time.sleep(3)

for cookie in saved:
    driver.add_cookie(cookie)
print('recovered:', driver.get_cookies())

driver.refresh()
driver.quit()