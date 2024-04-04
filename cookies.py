         # cookies before login and after login
# saucedemo.com

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

print("cookies before login")
for cookies in driver.get_cookies():
    print(cookies)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

print(" cookies after login")
for cookies in driver.get_cookies():
    print(cookies)

time.sleep(30)
driver.quit()

