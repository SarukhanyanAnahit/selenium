import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.youtube.com/")
time.sleep(2)

driver.add_cookie({
    "name": "username",
    "value": "user123"
})
driver.refresh()
time.sleep(2)

cookie = driver.get_cookie("username")
assert cookie["value"] == "user123"
print(cookie)
driver.quit()
