from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait

service=Service(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
wait=WebDriverWait(driver, 12)

driver.get('https://demoqa.com/selectable')
grid=driver.find_element(By.ID, "demo-tab-grid").click()

one=driver.find_element(By.XPATH, '//li[text()="One"]')
one.click()
two=driver.find_element(By.XPATH, '//li[text()="Two"]')
two.click()

assert 'active' in one.get_attribute('class')
assert 'active' in two.get_attribute('class')

one.click()
two.click()
assert one.is_enabled() is True
assert two.is_enabled() is True