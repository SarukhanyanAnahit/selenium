from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service=Service(executable_path=ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

driver.get('https://demoqa.com/text-box')
name_field=driver.find_element('id', 'userName')
name_field.clear()
name_field.send_keys('Vard')
time.sleep(3)
assert name_field.get_attribute("value") == 'Vard'
email=driver.find_element('id', 'userEmail')
email.clear()
email.send_keys('some@gmail.com')
time.sleep(3)
assert email.get_attribute('value')=='some@gmail.com'
current=driver.find_element('id', 'currentAddress')
current.clear()
current.send_keys('somewhere')
time.sleep(3)
assert current.get_attribute('value')=='somewhere'
permanent=driver.find_element('id', 'permanentAddress')
permanent.clear()
permanent.send_keys('in mountains')
time.sleep(3)
assert permanent.get_attribute('value')=='in mountains'
button=driver.find_element('id', 'submit')
button.click()
time.sleep(3)

