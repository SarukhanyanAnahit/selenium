import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 30, poll_frequency=1)

driver.get('https://omayo.blogspot.com/')

wait.until(EC.invisibility_of_element_located((By.ID, "deletesuccess")))
button=driver.find_element(By.ID, 'alert2').click()
time.sleep(3)

wait.until(EC.visibility_of_element_located((By.ID, "delayedText")))
time.sleep(3)

wait.until(EC.element_to_be_clickable((By.ID, "myBtn")))
time.sleep(3)

try_button = driver.find_element(By.CSS_SELECTOR, "button:nth-child(3)")
try_button.click()
wait.until(EC.element_attribute_to_include((By.CSS_SELECTOR, "#myBtn"), "disabled"))
time.sleep(3)






