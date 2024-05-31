from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
url = "https://www.instagram.com/"
browser = webdriver.Chrome()

browser.get(url)

time.sleep(5)

file = open('/* FILE THAT CONTAINS YOUR PASSWORD */', 'r')
password = file.readlines()[0]

browser.find_element(By.NAME, 'username').send_keys('/* USERNAME */')
browser.find_element(By.NAME, 'password').send_keys(password)
WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div')))

# so that the website remains on for some time
time.sleep(2000)
browser.close()
