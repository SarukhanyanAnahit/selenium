import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://hyperskill.org/login")

driver.switch_to.new_window('tab')
driver.get("https://www.avito.ru/")

driver.switch_to.new_window('tab')
driver.get("https://www.ozon.ru/")

tabs = driver.window_handles

for tab in tabs:
    driver.switch_to.window(tab)
    print(driver.title)

driver.switch_to.window(tabs[0])
driver.find_element(By.XPATH, '//fieldset[@id="__BVID__152"]').click()
time.sleep(2)

driver.switch_to.window(tabs[1])
driver.find_element(By.XPATH, "//span[text()='Скидки']").click()
time.sleep(2)

driver.switch_to.window(tabs[2])
driver.find_element(By.XPATH, "//div[@class='uw_ha6']").click()
time.sleep(2)

driver.quit()