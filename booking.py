import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

serv_obj = Service("C://Users/Professional/PycharmProjects/22_09_version/venv/Chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.maximize_window()
driver.get("https://pre.bonp.me/member/")

driver.find_element(By.CSS_SELECTOR, "#email").send_keys("alexandra@evolany.com")
driver.find_element(By.CSS_SELECTOR, "#pass").send_keys("221373897qw")
driver.find_element(By.CSS_SELECTOR, ".show-mail-login").click()

time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(text(),'test_bot')]").click()

time.sleep(4)


#time.sleep(2)
#driver.find_element(By.XPATH, "//footer[@class='exps']/button[@class='icon save label']']").click()