import time
import autoit
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
driver.find_element(By.XPATH, "//h2[@class='icon menu']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//h2[@class='icon menu']").click()
time.sleep(1)

action = ActionChains(driver)
action.click(driver.find_element(By.XPATH, "//button[@class='icon plus-circle']")).send_keys("rich-menu-1" + Keys.ENTER).perform()

driver.find_element(By.XPATH, "//button[@class='icon upload imagemap-upld-btn']").click()

time.sleep(1)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\rich-menu1.jpg")
time.sleep(3)
autoit.control_click("Открытие", "Button1")
time.sleep(6)

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(4)

########################## Area 1 ###############################

driver.find_element(By.XPATH, "//div[@class='image-pane']/div[@class='imagemap']").click()
time.sleep(1)

area1 = driver.find_element(By.XPATH, "//div[@class='image-pane']/div[@class='imagemap']/b")
action = ActionChains(driver)
action.drag_and_drop_by_offset(area1, -305, -240).perform()

resizeable = driver.find_element(By.XPATH, "//div[@class='image-pane']/div[@class='imagemap']/i")

action = ActionChains(driver)
action.click_and_hold(resizeable).move_by_offset(120, 165).release().perform()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@data-value='Area 1']").clear()
driver.find_element(By.XPATH, "//input[@data-value='Area 1']").send_keys("Store Reservation")

driver.find_element(By.XPATH, "(//div[@class='ui-dropdown'])[1]").click()

areasActions = driver.find_elements(By.XPATH, "//ul[@class='ui-dropdown-opts']/li")
for action in areasActions:
    if action.get_attribute("val") == "funcs_myrms":
        action.click()
        break

time.sleep(1)

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(2)

######################## Area 2 #############################

driver.find_element(By.XPATH, "//div[@class='image-pane']/div[@class='imagemap']").click()
time.sleep(1)

area2 = driver.find_element(By.XPATH, "(//div[@class='image-pane']/div[@class='imagemap']/b)[2]")
action = ActionChains(driver)
action.drag_and_drop_by_offset(area2, -65, -240).perform()

resizeable = driver.find_element(By.XPATH, "(//div[@class='image-pane']/div[@class='imagemap']/i)[2]")

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
    if actionOption.text == "1:textitem1":
        actionOption.click()
        break

time.sleep(1)

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(2)

#################### Area3 ########################
driver.find_element(By.XPATH, "//div[@class='image-pane']/div[@class='imagemap']").click()
time.sleep(1)

area3 = driver.find_element(By.XPATH, "(//div[@class='image-pane']/div[@class='imagemap']/b)[3]")
action = ActionChains(driver)
action.drag_and_drop_by_offset(area3, 180, -240).perform()

resizeable = driver.find_element(By.XPATH, "(//div[@class='image-pane']/div[@class='imagemap']/i)[3]")

action = ActionChains(driver)
action.click_and_hold(resizeable).move_by_offset(125, 165).release().perform()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@data-value='Area 1']").clear()
driver.find_element(By.XPATH, "//input[@data-value='Area 1']").send_keys("Text")

driver.find_element(By.XPATH, "(//div[@class='ui-dropdown'])[1]").click()

areasActions = driver.find_elements(By.XPATH, "//ul[@class='ui-dropdown-opts']/li")
for action in areasActions:
    if action.get_attribute("val") == "text":
        action.click()
        break

time.sleep(1)

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(2)

#################### Area4 ########################
driver.find_element(By.XPATH, "//div[@class='image-pane']/div[@class='imagemap']").click()
time.sleep(1)

area4 = driver.find_element(By.XPATH, "(//div[@class='image-pane']/div[@class='imagemap']/b)[4]")
action = ActionChains(driver)
action.drag_and_drop_by_offset(area4, -305, 40).perform()

resizeable = driver.find_element(By.XPATH, "(//div[@class='image-pane']/div[@class='imagemap']/i)[4]")

action = ActionChains(driver)
action.click_and_hold(resizeable).move_by_offset(120, 165).release().perform()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@data-value='Area 1']").clear()
driver.find_element(By.XPATH, "//input[@data-value='Area 1']").send_keys("URL")

driver.find_element(By.XPATH, "(//div[@class='ui-dropdown'])[1]").click()

areasActions = driver.find_elements(By.XPATH, "//ul[@class='ui-dropdown-opts']/li")
for action in areasActions:
    if action.get_attribute("val") == "url":
        action.click()
        break

time.sleep(1)
driver.find_element(By.XPATH, "//div[@class='form-type-text']/input").send_keys("https://anybot.me/")

driver.find_element(By.XPATH, "//label[@data-value='linkto']").click()

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(2)

#################### Area6 ########################
driver.find_element(By.XPATH, "//div[@class='image-pane']/div[@class='imagemap']").click()
time.sleep(1)

area5 = driver.find_element(By.XPATH, "(//div[@class='image-pane']/div[@class='imagemap']/b)[5]")
action = ActionChains(driver)
action.drag_and_drop_by_offset(area5, 180, 40).perform()

resizeable = driver.find_element(By.XPATH, "(//div[@class='image-pane']/div[@class='imagemap']/i)[5]")

action = ActionChains(driver)
action.click_and_hold(resizeable).move_by_offset(125, 165).release().perform()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@data-value='Area 1']").clear()
driver.find_element(By.XPATH, "//input[@data-value='Area 1']").send_keys("Swipe")

driver.find_element(By.XPATH, "(//div[@class='ui-dropdown'])[1]").click()

areasActions = driver.find_elements(By.XPATH, "//ul[@class='ui-dropdown-opts']/li")
for action in areasActions:
    if action.get_attribute("val") == "swipe":
        action.click()
        break

time.sleep(1)

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(2)

#################### Area5 ########################

driver.find_element(By.XPATH, "//div[@class='image-pane']/div[@class='imagemap']").click()
time.sleep(1)

area6 = driver.find_element(By.XPATH, "(//div[@class='image-pane']/div[@class='imagemap']/b)[6]")
action = ActionChains(driver)
action.drag_and_drop_by_offset(area6, -65, 40).perform()

resizeable = driver.find_element(By.XPATH, "(//div[@class='image-pane']/div[@class='imagemap']/i)[6]")

action = ActionChains(driver)
action.click_and_hold(resizeable).move_by_offset(125, 165).release().perform()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@data-value='Area 1']").clear()
driver.find_element(By.XPATH, "//input[@data-value='Area 1']").send_keys("Saved")

driver.find_element(By.XPATH, "(//div[@class='ui-dropdown'])[1]").click()

areasActions = driver.find_elements(By.XPATH, "//ul[@class='ui-dropdown-opts']/li")
for action in areasActions:
    if action.get_attribute("val") == "stocks":
        action.click()
        break

time.sleep(1)

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(2)


##### Rich menu 2 ########
action = ActionChains(driver)
action.click(driver.find_element(By.XPATH, "//button[@class='icon plus-circle']")).send_keys("rich-menu-2" + Keys.ENTER).perform()
driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//li[@title='rich-menu-2']").click()
driver.find_element(By.XPATH, "//button[@class='icon upload imagemap-upld-btn']").click()

time.sleep(1)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\rich-menu2.jpg")
time.sleep(3)
autoit.control_click("Открытие", "Button1")
time.sleep(8)

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













