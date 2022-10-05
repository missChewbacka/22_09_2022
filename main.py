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
driver.implicitly_wait(5)

driver.get("https://pre.bonp.me/member/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "#email").send_keys("alexandra@evolany.com")
driver.find_element(By.CSS_SELECTOR, "#pass").send_keys("221373897qw")
driver.find_element(By.CSS_SELECTOR, ".show-mail-login").click()

driver.find_element(By.XPATH, "//button[@hint='Create a new app']").click()
driver.find_element(By.XPATH, "//input[@name='name']").clear()
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("test_bot")

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
    if api.get_attribute("data-value") == "1":
        api.click()
        break

driver.find_element(By.XPATH, "//input[@target_name='com_id']").send_keys("e")
time.sleep(2)
companies = driver.find_elements(By.XPATH, "//ul[@id='form-item-autocomplete']/li")
for company in companies:
    if company.text == "Evolany Co., Ltd.":
        company.click()
        break

driver.find_element(By.XPATH, "//button[@class='icon save']").click()

driver.find_element(By.CSS_SELECTOR, ".logo").click()


























