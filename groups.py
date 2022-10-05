import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#from var_main import anybot

serv_obj = Service("C://Users/Professional/PycharmProjects/22_09_version/venv/Chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.maximize_window()
driver.get("https://pre.bonp.me/member/")

driver.find_element(By.CSS_SELECTOR, "#email").send_keys("alexandra@evolany.com")
driver.find_element(By.CSS_SELECTOR, "#pass").send_keys("221373897qw")
driver.find_element(By.CSS_SELECTOR, ".show-mail-login").click()


driver.find_element(By.XPATH, "//*[contains(text(),'test_bot')]").click()
time.sleep(2)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Group']")).perform()

action.click(driver.find_element(By.XPATH, "//label[normalize-space()='Group']")).send_keys("group1"+Keys.ENTER).perform()

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Group']")).perform()
action.click(driver.find_element(By.XPATH, "//label[normalize-space()='Group']")).send_keys("miniapps"+Keys.ENTER).perform()

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Group']")).perform()
action.click(driver.find_element(By.XPATH, "//label[normalize-space()='Group']")).send_keys("booking"+Keys.ENTER).perform()

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Group']")).perform()
action.click(driver.find_element(By.XPATH, "//label[normalize-space()='Group']")).send_keys("events"+Keys.ENTER).perform()

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Group']")).perform()
action.click(driver.find_element(By.XPATH, "//label[normalize-space()='Group']")).send_keys("webhook_test"+Keys.ENTER).perform()

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Group']")).perform()
action.click(driver.find_element(By.XPATH, "//label[normalize-space()='Group']")).send_keys("saved"+Keys.ENTER).perform()

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Group']")).perform()
action.click(driver.find_element(By.XPATH, "//label[normalize-space()='Group']")).send_keys("swipe"+Keys.ENTER).perform()

driver.refresh()

driver.quit()
driver.close()














