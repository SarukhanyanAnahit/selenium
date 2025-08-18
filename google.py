from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service, options=options)
driver.get('https://google.com')
field=driver.find_element(By.XPATH, '//textarea[@jsname="yZiJbe"]')
field.send_keys("Selenium Python")
field.send_keys(Keys.ENTER)
time.sleep(5)
# check=driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border')
# check.click()
titles = driver.find_elements(By.TAG_NAME, "h3")
for title in titles[:5]:
    print(f'title: {title.text}')
time.sleep(5)
