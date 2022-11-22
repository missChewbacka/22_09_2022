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
driver.find_element(By.CSS_SELECTOR, "#pass").send_keys("221373897")
driver.find_element(By.CSS_SELECTOR, ".show-mail-login").click()

time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(text(),'test-br-v2')]").click()

time.sleep(4)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[6]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[6]")).perform()

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()

action.click(driver.find_element(By.XPATH, "//dd[@rt='card']")).send_keys("events"+Keys.ENTER).perform()

driver.find_element(By.XPATH, "//div[@class='edit-panel']/dl/dd/b[@class='icon double-right']").click()

time.sleep(1)
driver.find_element(By.XPATH, "//p[@class='srcs src-content']/button").click()

time.sleep(1)
contentItems = driver.find_elements(By.XPATH, "//ul[@class='ui-dropdown-opts']/li")

for item in contentItems:
    if item.text == "Events" or item.text == "イベント":
        item.click()
        break

time.sleep(1)

driver.find_element(By.XPATH, "//ol[@class='card imagecard seq-0']/li[@class='item new']").click()

time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@name='label']").send_keys("Book event")

driver.find_element(By.XPATH, "//label[@data-value='manual']").click()

driver.find_element(By.XPATH, "//input[@target_name='act']").click()

manualOptions = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")

for option in manualOptions:
    if option.get_attribute("val") == "FUNCS_EVENTRESERVE":
        option.click()
        break

driver.find_element(By.XPATH, "//button[@class='icon save label']").click()

driver.refresh()

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[6]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[6]")).perform()

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//dd[@rt='text']")).send_keys("qr_book"+Keys.ENTER).perform()

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//dd[@rt='text']")).send_keys("qr_checkin"+Keys.ENTER).perform()

driver.refresh()

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[6]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[6]")).perform()

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[2]").click()

time.sleep(0.5)
driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[2]").send_keys("qr_book"+Keys.ENTER)

driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li[@class='item new'])[2]").click()

time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@name='label']").send_keys("Book")

driver.find_element(By.XPATH, "//label[@data-value='manual']").click()

time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@target_name='act']").click()

manualOptions = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")

for option in manualOptions:
    if option.get_attribute("val") == "FUNCS_EVENTRESERVE":
        option.click()
        break

driver.find_element(By.XPATH, "//button[@class='icon save label']").click()

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[3]").click()

driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[3]").send_keys("qr_checkin"+Keys.ENTER)

driver.refresh()

navItems = driver.find_elements(By.XPATH, "//div[@class='settings']/dl/dd")

for item in navItems:
    if item.get_attribute("msg") == "navi-bot":
        item.click()
        break

time.sleep(1)

driver.find_element(By.XPATH, "//input[@target_name='events_aid']").click()

reservationOptions = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")

for option in reservationOptions:
    if option.text == "2:qr_book":
        option.click()
        break

driver.find_element(By.XPATH, "//input[@target_name='events_ck_aid']").click()

checkinOptions = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")

for option in checkinOptions:
    if option.text == "3:qr_checkin":
        option.click()
        break

driver.find_element(By.XPATH, "//button[@class='icon save label']").click()

















