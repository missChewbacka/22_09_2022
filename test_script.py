import time
import autoit
import self as self
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

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

######################################
driver.find_element(By.XPATH, "//h2[@class='icon menu']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//h2[@class='icon menu']").click()
time.sleep(1)

#################### Area1 ########################

#################### Area2 ########################

#################### Area3 ########################

#################### Area4 ########################



action = ActionChains(driver)
action.click(driver.find_element(By.XPATH, "//button[@class='icon plus-circle']")).send_keys("rich-menu-2" + Keys.ENTER).perform()

driver.find_element(By.XPATH, "//button[@class='icon upload imagemap-upld-btn']").click()

time.sleep(1)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\rich-menu2.jpg")
time.sleep(4)
autoit.control_click("Открытие", "Button1")
time.sleep(4)

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(4)

driver.find_element(By.XPATH, "//div[@class='image-pane']/div[@class='imagemap']").click()
time.sleep(1)

area1 = driver.find_element(By.XPATH, "//div[@class='image-pane']/div[@class='imagemap']/b")
action = ActionChains(driver)
action.drag_and_drop_by_offset(area1, -65, -240).perform()

resizeable = driver.find_element(By.XPATH, "//div[@class='image-pane']/div[@class='imagemap']/i")

action = ActionChains(driver)
action.click_and_hold(resizeable).move_by_offset(125, 165).release().perform()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@data-value='Area 1']").clear()
driver.find_element(By.XPATH, "//input[@data-value='Area 1']").send_keys("Action")

driver.find_element(By.XPATH, "(//div[@class='ui-dropdown'])[1]").click()

areasActions = driver.find_elements(By.XPATH, "//ul[@class='ui-dropdown-opts']/li")
for action in areasActions:
    if action.get_attribute("val") == "act":
        action.click()
        break

time.sleep(1)

driver.find_element(By.XPATH, "(//input[@target_name='act'])[1]").click()

actionOptions = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")
for actionOption in actionOptions:
    if actionOption.text == "1:swipe_start":
        actionOption.click()
        break

time.sleep(1)

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(2)