from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get('https://hyperskill.org/courses')

all_courses = driver.find_elements(By.XPATH, "//a[contains(@class, 'btn-category')]")
most_popular = driver.find_elements(By.XPATH, "//a[contains(@class, 'btn-category')]")
python = driver.find_elements(By.XPATH, "//button[contains(., 'Python')]")
ai = driver.find_elements(By.XPATH, "//button[contains(., 'AI & AI Coding Tools')]")
sql_title=driver.find_elements(By.XPATH, '//h5[contains (text(), "Introduction to SQL")]')
sql_block=driver.find_elements(By.XPATH, '//DIV[2]/DIV[1]/A[1]/DIV[1]')
data_analyst_title = driver.find_elements(By.XPATH, '//h5[contains(text(), "Data Analyst")]')
load_more=driver.find_elements(By.XPATH, '//button[.//span[contains(text(), "Load more")]]')

hyperskill=driver.find_elements(By.XPATH, '//a[contains(@class, "nav-link")]')
catalog=driver.find_element(By.XPATH, '//a[contains(text(), "Catalog")]')
full_catalog=driver.find_element(By.XPATH,'//a[@class="active-route router-link-exact-active btn btn-outline-secondary btn-sm !text-white-100"]')
about=driver.find_element(By.XPATH, '//a[contains(text(), "About")]')
linkedin_icon=driver.find_element(By.XPATH, '//a[@ title="Hyperskill on Linkedin"]')
app_store=driver.find_element(By.XPATH, '//img[@alt="Download on the App Store"]')
sign_in=driver.find_element(By.XPATH, 'id("header")/nav[1]/div[1]/div[2]/button[1]')
