import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\Professional\AppData\Local\Google\Chrome\User Data\Default")

serv_obj = Service("C://Users/Professional/PycharmProjects/22_09_version/venv/Chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj, options=options)
driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://pre.bonp.me/member/")

#driver.find_element(By.CSS_SELECTOR, "#email").send_keys("alexandra@evolany.com")
#driver.find_element(By.CSS_SELECTOR, "#pass").send_keys("221373897")
#driver.find_element(By.CSS_SELECTOR, ".show-mail-login").click()



############ Create bot Api1.0
driver.find_element(By.XPATH, "//button[@hint='Create a new app']").click()
driver.find_element(By.XPATH, "//input[@name='name']").clear()
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Sasha_1011_Api2.0")

modules = driver.find_elements(By.XPATH, "//li[@name='opts']/div/label/input[@type='checkbox']")
for module in modules[1:]:
    module.click()

plans = driver.find_elements(By.XPATH, "//label[@class='sel-option radio ']")
for plan in plans:
    if plan.get_attribute("value") == "pro":
        plan.click()
        break

apis = driver.find_elements(By.XPATH, "//li[@name='apiver']/div/label")
for api in apis:
    if api.get_attribute("data-value") == "2":
        api.click()
        break

driver.find_element(By.XPATH, "//input[@target_name='com_id']").send_keys("Ev")
time.sleep(2)
companies = driver.find_elements(By.XPATH, "//ul[@id='form-item-autocomplete']/li")
for company in companies:
    if company.text == "Evolany Co., Ltd.":
        company.click()
        break

driver.find_element(By.XPATH, "//button[@class='icon save']").click()

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

