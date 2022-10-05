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

############ Create bot Api1.0
driver.find_element(By.XPATH, "//button[@hint='Create a new app']").click()
driver.find_element(By.XPATH, "//input[@name='name']").clear()
driver.find_element(By.XPATH, "//input[@name='name']").send_keys("Webdriwer_BabyBot_Api2.0")

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

###################### events ################################

navItems = driver.find_elements(By.XPATH, "//nav[@class='btns app-menus']/a")

for item in navItems:
    if item.get_attribute("name") == "event_list_view":
        item.click()
        break

driver.find_element(By.XPATH, "//button[@class='new icon plus-square']").click()

driver.find_element(By.XPATH, "//input[@name='linkto']").send_keys("https://www.netflix.com/")

driver.find_element(By.XPATH, "//div[@class='form-item-file']").click()
time.sleep(1)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\event_img1.jpg")
time.sleep(3)
autoit.control_click("Открытие", "Button1")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='title']").send_keys("testevent1")
driver.find_element(By.XPATH, "//textarea[@name='desc']").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sed.")
driver.find_element(By.XPATH, "//input[@name='seats']").clear()
driver.find_element(By.XPATH, "//input[@name='seats']").send_keys("1")

driver.find_element(By.XPATH, "//button[@class='icon save']").click()

#comment for the demo for popup handling
driver.find_element(By.XPATH, "//div[@class='content']/footer/button").click()

driver.find_element(By.XPATH, "//button[@class='new icon plus-square']").click()

driver.find_element(By.XPATH, "//input[@name='linkto']").send_keys("https://www.udemy.com/")

driver.find_element(By.XPATH, "//div[@class='form-item-file']").click()
time.sleep(1)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\event_img2.jpg")
time.sleep(3)
autoit.control_click("Открытие", "Button1")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='title']").send_keys("testevent2")
driver.find_element(By.XPATH, "//textarea[@name='desc']").send_keys(
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sed.")
driver.find_element(By.XPATH, "//input[@name='seats']").clear()
driver.find_element(By.XPATH, "//input[@name='seats']").send_keys("1")

driver.find_element(By.XPATH, "//button[@class='icon save']").click()

# comment for the demo for popup handling
driver.find_element(By.XPATH, "//div[@class='content']/footer/button").click()

driver.find_element(By.XPATH, "//button[@class='new icon plus-square']").click()

driver.find_element(By.XPATH, "//input[@name='linkto']").send_keys("https://www.freecodecamp.org/")

driver.find_element(By.XPATH, "//div[@class='form-item-file']").click()
time.sleep(1)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\event_img3.jpg")
time.sleep(3)
autoit.control_click("Открытие", "Button1")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='title']").send_keys("testevent3")
driver.find_element(By.XPATH, "//textarea[@name='desc']").send_keys(
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sed.")
driver.find_element(By.XPATH, "//input[@name='seats']").clear()
driver.find_element(By.XPATH, "//input[@name='seats']").send_keys("1")

driver.find_element(By.XPATH, "//button[@class='icon save']").click()

driver.find_element(By.XPATH, "//div[@class='content']/footer/button").click()

navItems = driver.find_elements(By.XPATH, "//nav[@class='btns app-menus']/a")

for item in navItems:
    if item.get_attribute("name") == "bot_edit_view":
        item.click()
        break

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[6]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[6]")).perform()

time.sleep(1)
action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()

action.click(driver.find_element(By.XPATH, "//dd[@rt='card']")).send_keys("events"+Keys.ENTER).perform()

time.sleep(1)
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

driver.refresh()

###################### group1 ################################

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()
action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//label[normalize-space()='Text']")).send_keys("textitem1"+Keys.ENTER).perform()
action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//label[normalize-space()='Text']")).send_keys("textitem2"+Keys.ENTER).perform()
action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//label[normalize-space()='Text']")).send_keys("textitem3"+Keys.ENTER).perform()
action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//label[normalize-space()='Text']")).send_keys("textitem4"+Keys.ENTER).perform()

driver.refresh()

action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[1]").click()
driver.find_element(By.XPATH, "(//textarea[@col='msg'])[1]").send_keys("textitem1"+Keys.ENTER)
driver.find_element(By.XPATH, "(//li[@tp='items'])[1]").click()
driver.find_element(By.XPATH, "//input[@name='label']").send_keys("text1 button")
driver.find_element(By.XPATH, "//button[@class='icon save label']").click()

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[2]").click()
driver.find_element(By.XPATH, "(//textarea[@col='msg'])[2]").send_keys("textitem2"+Keys.ENTER)

time.sleep(1)
driver.find_element(By.XPATH, "(//div[@class='react-btns empty']/label)[2]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//footer[@class='exps']/label").click()
time.sleep(1)
driver.find_element(By.XPATH, "//div[@class='form-type-text']/input[@name='label']").send_keys("choice1")
time.sleep(1)
driver.find_element(By.XPATH, "//label[@data-value='manual']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//div[@class='form-type-autocomplete']/div").click()

actions = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")
for action in actions:
    if action.text == "3:textitem3":
        action.click()
        break

driver.find_element(By.XPATH, "//input[@name='ukey']").send_keys("choice")

driver.find_element(By.XPATH, "//footer[@class='exps']/button[@class='icon save label']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//div[@class='react-btns']/label[@class='new']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//footer[@class='exps']/label").click()
time.sleep(1)

driver.find_element(By.XPATH, "//div[@class='form-type-text']/input[@name='label']").send_keys("choice2")
time.sleep(1)
driver.find_element(By.XPATH, "//label[@data-value='manual']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//div[@class='form-type-autocomplete']/div").click()

actions = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")
for action in actions:
    if action.text == "3:textitem3":
        action.click()
        break

driver.find_element(By.XPATH, "//input[@name='ukey']").send_keys("choice")

driver.find_element(By.XPATH, "//footer[@class='exps']/button[@class='icon save label']").click()

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[3]").click()
driver.find_element(By.XPATH, "(//textarea[@col='msg'])[3]").send_keys("textitem3"+Keys.ENTER)
time.sleep(1)

driver.find_element(By.XPATH, "(//div[@class='react-ipts-new']/span)[3]").click()
time.sleep(1)

driver.find_element(By.XPATH, "(//div[@class='ui-dropdown form-item'])[1]").click()
time.sleep(1)

options = driver.find_elements(By.XPATH, "//ul[@class='ui-dropdown-opts']/li")
for option in options:
    if option.text == "Match pattern of":
        option.click()
        break
time.sleep(1)

patterns = driver.find_elements(By.XPATH, "//article[@id='mask']/ul/li")
for pattern in patterns:
    if pattern.text == "match all patterns":
        pattern.click()
        break
time.sleep(1)

driver.find_element(By.XPATH, "//label[@data-value='manual']").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "//div[@class='form-type-autocomplete']/div/input[@class='autocomplete']").click()
actions = driver.find_elements(By.XPATH, "//ul[@id='form-item-autocomplete']/li")
for action in actions:
    if action.text == "4:textitem4":
        action.click()
        break
time.sleep(0.5)
driver.find_element(By.XPATH, "//button[@class='icon save label']").click()

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[4]").click()
driver.find_element(By.XPATH, "(//textarea[@col='msg'])[4]").send_keys("textitem4"+Keys.ENTER)
time.sleep(1)
driver.find_element(By.XPATH, "(//div[@class='react-fhs-new']/span)[4]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[@class='icon save label']").click()

driver.refresh()
time.sleep(1)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
time.sleep(0.5)
action.click(driver.find_element(By.XPATH, "//dd[@rt='card']")).send_keys("carousel1"+Keys.ENTER).perform()
time.sleep(0.5)

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[5]").click()
driver.find_element(By.XPATH, "(//b[@class='icon coding'])[5]").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "(//p[@class='srcs src-api'])[5]/input").send_keys("https://pre.bonp.me/api/service/recipes/?format=list"+Keys.ENTER)
time.sleep(0.5)
driver.find_element(By.XPATH, "(//li[contains(text(),'Add new button')])[10]").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "//div[@class='form-type-text']/input[@name='label']").send_keys("Button")
driver.find_element(By.XPATH, "//button[@class='icon save label']").click()
time.sleep(0.5)

driver.refresh()

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
time.sleep(0.5)
action.click(driver.find_element(By.XPATH, "//dd[@rt='card']")).send_keys("carousel2"+Keys.ENTER).perform()
time.sleep(0.5)

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[6]").click()
driver.find_element(By.XPATH, "(//b[@class='icon double-right'])[2]").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "(//button[@class='ui-menu'])[12]").click()

contentItems = driver.find_elements(By.XPATH, "//article[@id='mask']/ul/li")

for item in contentItems:
    if item.text == "Events" or item.text == "イベント":
        item.click()
        break

driver.find_element(By.XPATH, "(//div[@class='react-btns empty']/label)[5]").click()

driver.find_element(By.XPATH, "//input[@name='label']").send_keys("Next")

driver.find_element(By.XPATH, "//button[@class='icon save label']").click()

driver.refresh()
time.sleep(1)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()

action.click(driver.find_element(By.XPATH, "(//nav[@class='navi']/dl/dd)[5]")).send_keys("image_carousel"+Keys.ENTER).perform()
time.sleep(1)
driver.find_element(By.XPATH, "(//b[@class='icon double-right'])[3]").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//p[@class='srcs src-content']/button)[7]").click()
time.sleep(1)
contentItems = driver.find_elements(By.XPATH, "//article[@id='mask']/ul/li")

for item in contentItems:
    if item.text == "Events" or item.text == "イベント":
        item.click()
        break

driver.find_element(By.XPATH, "(//li[contains(text(),'Add new button')])[21]").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@name='label']").send_keys("Next")
driver.find_element(By.XPATH, "//button[@class='icon save label']").click()

driver.refresh()
time.sleep(1)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()

action.click(driver.find_element(By.XPATH, "(//nav[@class='navi']/dl/dd)[6]")).send_keys("image_map"+Keys.ENTER).perform()

driver.find_element(By.XPATH, "(//ol[@class='card imagecard seq-0']/i[@class='icon camera large upload-btn'])[17]").click()

time.sleep(3)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\image_map.jpg")
time.sleep(3)
autoit.control_click("Открытие", "Button1")
time.sleep(3)

#add a drag and drop

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[8]").click()

### Area 1 ###

driver.find_element(By.XPATH, "(//i[@class='icon brush large upload-btn'])[17]").click()
time.sleep(1)

driver.find_element(By.XPATH, "//div[@class='imagemap']").click()
time.sleep(0.5)

element1 = driver.find_element(By.XPATH, "//div[@class='imagemap']/b")
action = ActionChains(driver)
action.drag_and_drop_by_offset(element1, -240, -240).perform()
resizeable = driver.find_element(By.XPATH, "//div[@class='imagemap']/i")

action = ActionChains(driver)
action.click_and_hold(resizeable).move_by_offset(110, 400).release().perform()
time.sleep(1)

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(1)
### Area2 ###

driver.find_element(By.XPATH, "(//i[@class='icon brush large upload-btn'])[17]").click()
time.sleep(1)

driver.find_element(By.XPATH, "//div[@class='imagemap']").click()
time.sleep(0.5)

element2 = driver.find_element(By.XPATH, "(//div[@class='imagemap']/b)[2]")
action = ActionChains(driver)
action.drag_and_drop_by_offset(element2, 10, -240).perform()
time.sleep(0.5)
resizeable = driver.find_element(By.XPATH, "(//div[@class='imagemap']/i)[2]")
action = ActionChains(driver)
action.click_and_hold(resizeable).move_by_offset(207, 160).release().perform()
time.sleep(0.5)

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(1)

### Area 3 ###

driver.find_element(By.XPATH, "(//i[@class='icon brush large upload-btn'])[17]").click()
time.sleep(1)

driver.find_element(By.XPATH, "//div[@class='imagemap']").click()
time.sleep(0.5)

element3 = driver.find_element(By.XPATH, "(//div[@class='imagemap']/b)[3]")
action = ActionChains(driver)
action.drag_and_drop_by_offset(element3, 10, 0).perform()
time.sleep(0.5)
resizeable = driver.find_element(By.XPATH, "(//div[@class='imagemap']/i)[3]")
action = ActionChains(driver)
action.click_and_hold(resizeable).move_by_offset(207, 160).release().perform()
time.sleep(0.5)

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(1)

### Area 1 settings ###

driver.find_element(By.XPATH, "(//div[@class='react-btns']/label[@tp='btns'])[6]").click()
time.sleep(0.4)

driver.find_element(By.XPATH, "//input[@data-value='manual']").click()
time.sleep(0.4)
driver.find_element(By.XPATH, "//input[@target_name='act']").click()
time.sleep(1)

area1Options = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")
for area1Option in area1Options:
    if area1Option.text == "1:textitem1":
        area1Option.click()
        break

driver.find_element(By.XPATH, "//button[@class='icon save label']").click()
time.sleep(1)

### Area 2 settings ###

driver.find_element(By.XPATH, "(//div[@class='react-btns']/label[@tp='btns'])[7]").click()
time.sleep(0.4)

driver.find_element(By.XPATH, "//input[@data-value='manual']").click()
time.sleep(0.4)
driver.find_element(By.XPATH, "//input[@target_name='act']").click()
time.sleep(1)

area2Options = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")
for area2Option in area2Options:
    if area2Option.text == "5:carousel1":
        area2Option.click()
        break

driver.find_element(By.XPATH, "//button[@class='icon save label']").click()
time.sleep(1)

driver.refresh()
time.sleep(1)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()

action.click(driver.find_element(By.XPATH, "(//nav[@class='navi']/dl/dd)[7]")).send_keys("image1"+Keys.ENTER).perform()
time.sleep(2)
driver.find_element(By.XPATH, "(//i[@class='icon camera large upload-btn'])[18]").click()
time.sleep(1)
autoit.win_activate("Открытие")
time.sleep(2)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\1040px.jpg")
time.sleep(3)
autoit.control_click("Открытие", "Button1")
time.sleep(2)

driver.find_element(By.XPATH, "(//div[@class='react-btns empty']/label)[6]").click()

driver.find_element(By.XPATH, "//input[@name='label']").send_keys("Next")

driver.find_element(By.XPATH, "//button[@class='icon save label']").click()

driver.refresh()
time.sleep(1)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()

action.click(driver.find_element(By.XPATH, "(//nav[@class='navi']/dl/dd)[8]")).send_keys("video1"+Keys.ENTER).perform()

driver.find_element(By.XPATH, "//i[@class='icon camera large upload-btn left_t']").click()

time.sleep(3)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\flamingo.jpg")
time.sleep(3)
autoit.control_click("Открытие", "Button1")
time.sleep(4)

driver.find_element(By.XPATH, "//i[@class='icon video large upload-btn left_b']").click()

time.sleep(2)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\Flamingo1.mp4")
time.sleep(3)
autoit.control_click("Открытие", "Button1")
## implement wait
time.sleep(8)

driver.find_element(By.XPATH, "(//div[@class='react-btns empty']/label)[6]").click()

driver.find_element(By.XPATH, "//input[@name='label']").send_keys("Next")

driver.find_element(By.XPATH, "//button[@class='icon save label']").click()

driver.refresh()
time.sleep(1)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[3]")).perform()

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()

action.click(driver.find_element(By.XPATH, "(//nav[@class='navi']/dl/dd)[9]")).send_keys("conditional"+Keys.ENTER).perform()

driver.find_element(By.XPATH, "//div[@class='fbox']/div[@class='ui-dropdown']").click()

dropdownOptions = driver.find_elements(By.XPATH, "//ul[@class='ui-dropdown-opts']/li")

for option in dropdownOptions:
    if option.get_attribute("val") == "ukey":
        option.click()
        break

driver.find_element(By.XPATH, "//input[@name='condition']").send_keys("{{user.choice}}=choice1")

driver.find_element(By.XPATH, "//input[@target_name='then']").click()

choice1Options = driver.find_elements(By.XPATH, "//ul[@id='form-item-autocomplete']/li")

for choice1 in choice1Options:
    if choice1.text == "1:textitem1":
        choice1.click()
        break

driver.find_element(By.XPATH, "//input[@target_name='else']").click()

choice2Options = driver.find_elements(By.XPATH, "//ul[@id='form-item-autocomplete']/li")

for choice2 in choice2Options:
    if choice2.text == "6:carousel2":
        choice2.click()
        break

##########################miniapps
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[4]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[4]")).perform()

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//dd[@rt='text']")).send_keys("form_trigger" + Keys.ENTER).perform()

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//dd[@rt='text']")).send_keys("form_finish" + Keys.ENTER).perform()

time.sleep(1)
navItems = driver.find_elements(By.XPATH, "//div[@class='settings']/dl/dd")

for item in navItems:
    if item.get_attribute("msg") == "navi-miniapp":
        item.click()
        break

time.sleep(1)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//nav[@class='navi']/div)[7]")).perform()
action.click(driver.find_element(By.XPATH, "//dd[@act='group']/b[@class='icon group']")).perform()

driver.find_element(By.XPATH, "//input[@name='title']").clear()
driver.find_element(By.XPATH, "//input[@name='title']").send_keys("form1")

driver.find_element(By.XPATH, "//button[@class='icon save']").click()

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//nav[@class='navi']/div)[7]")).perform()
action.click(driver.find_element(By.XPATH, "//dd[@act='group']/b[@class='icon group']")).perform()

driver.find_element(By.XPATH, "(//input[@name='title'])[3]").clear()
driver.find_element(By.XPATH, "(//input[@name='title'])[3]").send_keys("form2")

driver.find_element(By.XPATH, "//button[@class='icon save']").click()

driver.refresh()

navItems = driver.find_elements(By.XPATH, "//div[@class='settings']/dl/dd")

for item in navItems:
    if item.get_attribute("msg") == "navi-miniapp":
        item.click()
        break

time.sleep(1)

driver.find_element(By.XPATH, "(//section[@class='left-pane group-pane']/ul/li)[1]").click()

driver.find_element(By.XPATH, "(//section[@class='comp-mask'])[2]").click()
driver.find_element(By.XPATH, "(//i[@class='ico trash'])[2]").click()

driver.find_element(By.XPATH, "(//section[@class='comp-mask'])[2]").click()
driver.find_element(By.XPATH, "(//i[@class='ico trash'])[2]").click()

driver.find_element(By.XPATH, "(//section[@class='left-pane group-pane']/ul/li)[2]").click()

driver.find_element(By.XPATH, "(//section[@class='comp-mask'])[2]").click()
driver.find_element(By.XPATH, "(//i[@class='ico trash'])[2]").click()

driver.find_element(By.XPATH, "(//section[@class='comp-mask'])[2]").click()
driver.find_element(By.XPATH, "(//i[@class='ico trash'])[2]").click()

driver.find_element(By.XPATH, "(//section[@class='left-pane group-pane']/ul/li)[1]").click()

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//div[@class='edit-bar'])[1]")).perform()
action.move_to_element(driver.find_element(By.XPATH, "(//dd[@tp='formitems'])[1]")).perform()

formItems = driver.find_elements(By.XPATH, "(//dl[@class='sub formitems'])[1]/dd")

for input in formItems:
    if input.get_attribute("tp") == "input":
        time.sleep(0.5)
        input.click()
        break

driver.find_element(By.XPATH, "(//input[@name='title'])[1]").send_keys("Enter your name:")

driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys("ukey1")

driver.find_element(By.XPATH, "(//i[@class='ico save'])[2]").click()
time.sleep(1)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//div[@class='edit-bar'])[2]")).perform()
action.move_to_element(driver.find_element(By.XPATH, "(//dd[@tp='formitems'])[2]")).perform()

formItems = driver.find_elements(By.XPATH, "(//dl[@class='sub formitems'])[2]/dd")

for checkbox in formItems:
    if checkbox.get_attribute("tp") == "checkbox":
        time.sleep(0.5)
        checkbox.click()
        break

driver.find_element(By.XPATH, "(//input[@name='title'])[2]").send_keys("Select a checkbox option:")

driver.find_element(By.XPATH, "//textarea[@name='options']").send_keys(
    "checkbox1" + Keys.ENTER + "checkbox2" + Keys.ENTER + "checkbox3" + Keys.ENTER + "checkbox4" + Keys.ENTER)

driver.find_element(By.XPATH, "(//input[@name='name'])[3]").send_keys("ukey2")

driver.find_element(By.XPATH, "(//i[@class='ico save'])[3]").click()
time.sleep(1)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//div[@class='edit-bar'])[3]")).perform()
action.move_to_element(driver.find_element(By.XPATH, "(//dd[@tp='formitems'])[3]")).perform()

formItems = driver.find_elements(By.XPATH, "(//dl[@class='sub formitems'])[3]/dd")

for dropdown in formItems:
    if dropdown.get_attribute("tp") == "dropdown":
        time.sleep(0.5)
        dropdown.click()
        break

driver.find_element(By.XPATH, "(//input[@name='title'])[3]").send_keys("Select a dropdown option:")

driver.find_element(By.XPATH, "(//textarea[@name='options'])[2]").send_keys(
    "dropdown1" + Keys.ENTER + "dropdown2" + Keys.ENTER + "dropdown3" + Keys.ENTER + "dropdown4" + Keys.ENTER)

driver.find_element(By.XPATH, "(//input[@name='name'])[4]").send_keys("ukey3")

driver.find_element(By.XPATH, "(//i[@class='ico save'])[4]").click()
time.sleep(1)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//div[@class='edit-bar'])[4]")).perform()
action.move_to_element(driver.find_element(By.XPATH, "(//dd[@tp='formitems'])[4]")).perform()

formItems = driver.find_elements(By.XPATH, "(//dl[@class='sub formitems'])[4]/dd")

for tab in formItems:
    if tab.get_attribute("tp") == "tabmenu":
        time.sleep(0.5)
        tab.click()
        break

driver.find_element(By.XPATH, "(//input[@name='title'])[4]").send_keys("Select a tab option:")

driver.find_element(By.XPATH, "(//textarea[@name='options'])[3]").send_keys(
    "tab1" + Keys.ENTER + "tab2" + Keys.ENTER + "tab3" + Keys.ENTER + "tab4" + Keys.ENTER + "tab5" + Keys.ENTER)

driver.find_element(By.XPATH, "(//input[@name='name'])[5]").send_keys("ukey4")

driver.find_element(By.XPATH, "(//i[@class='ico save'])[5]").click()
time.sleep(1)

driver.find_element(By.XPATH, "(//section[@class='left-pane group-pane']/ul/li)[2]").click()

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//div[@class='edit-bar'])[1]")).perform()
action.move_to_element(driver.find_element(By.XPATH, "(//dd[@tp='formitems'])[1]")).perform()

formItems = driver.find_elements(By.XPATH, "(//dl[@class='sub formitems'])[1]/dd")

for radio in formItems:
    if radio.get_attribute("tp") == "radio":
        time.sleep(0.5)
        radio.click()
        break

driver.find_element(By.XPATH, "(//input[@name='title'])[1]").send_keys("Select a radio option:")

driver.find_element(By.XPATH, "//textarea[@name='options']").send_keys(
    "radio1" + Keys.ENTER + "radio2" + Keys.ENTER + "radio3" + Keys.ENTER + "radio4" + Keys.ENTER + "radio5")

driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys("ukey5")

driver.find_element(By.XPATH, "(//i[@class='ico save'])[2]").click()
time.sleep(1)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//div[@class='edit-bar'])[2]")).perform()
action.move_to_element(driver.find_element(By.XPATH, "(//dd[@tp='formitems'])[2]")).perform()

formItems = driver.find_elements(By.XPATH, "(//dl[@class='sub formitems'])[2]/dd")

for switch in formItems:
    if switch.get_attribute("tp") == "switch":
        time.sleep(0.5)
        switch.click()
        break

driver.find_element(By.XPATH, "(//input[@name='title'])[2]").send_keys("Switch ON/OFF:")

driver.find_element(By.XPATH, "(//input[@name='name'])[3]").send_keys("ukey6")

driver.find_element(By.XPATH, "(//i[@class='ico save'])[3]").click()
time.sleep(1.5)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//div[@class='edit-bar'])[3]")).perform()
action.move_to_element(driver.find_element(By.XPATH, "(//dd[@tp='formitems'])[3]")).perform()
action.move_to_element(driver.find_element(By.XPATH, "(//dd[@tp='input'])[3]")).perform()
action.move_to_element(driver.find_element(By.XPATH, "(//dd[@tp='yymmdd'])[3]")).click().perform()
time.sleep(1)

driver.find_element(By.XPATH, "(//input[@name='title'])[3]").send_keys("Select date:")

driver.find_element(By.XPATH, "(//input[@name='name'])[4]").send_keys("ukey7")

driver.find_element(By.XPATH, "(//i[@class='ico save'])[4]").click()
time.sleep(1)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//div[@class='edit-bar'])[4]")).perform()
action.move_to_element(driver.find_element(By.XPATH, "(//dd[@tp='formitems'])[4]")).perform()
action.move_to_element(driver.find_element(By.XPATH, "(//dd[@tp='input'])[4]")).perform()
action.move_to_element(driver.find_element(By.XPATH, "(//dd[@tp='file'])[4]")).click().perform()
time.sleep(1)

driver.find_element(By.XPATH, "(//input[@name='title'])[4]").send_keys("Upload your file:")

driver.find_element(By.XPATH, "(//input[@name='name'])[5]").send_keys("ukey8")

driver.find_element(By.XPATH, "(//i[@class='ico save'])[5]").click()
time.sleep(1)

################# form1 button set up

driver.find_element(By.XPATH, "(//section[@class='left-pane group-pane']/ul/li)[1]").click()

driver.find_element(By.XPATH, "(//section[@class='comp-mask'])[6]").click()

driver.find_element(By.XPATH, "//button[@type='button']").click()

driver.find_element(By.XPATH, "(//input[@name='title'])[5]").clear()
driver.find_element(By.XPATH, "(//input[@name='title'])[5]").send_keys("form2")

radioTrans = driver.find_elements(By.XPATH, "//div[@class='form-type-radio']/label/input[@name='trans']")

for radioItem in radioTrans:
    if radioItem.get_attribute("data-value") == "view":
        radioItem.click()
        break
time.sleep(0.5)

driver.find_element(By.XPATH, "//input[@target_name='view']").click()

chatItems = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")

for viewItem in chatItems:
    if viewItem.text == "form2":
        viewItem.click()
        break
time.sleep(1)

driver.find_element(By.XPATH, "//button[@class='icon save']").click()

driver.find_element(By.XPATH, "(//i[@class='ico save'])[6]").click()

time.sleep(0.5)

################# form2 button set up

driver.find_element(By.XPATH, "(//section[@class='left-pane group-pane']/ul/li)[2]").click()

driver.find_element(By.XPATH, "(//section[@class='comp-mask'])[6]").click()

driver.find_element(By.XPATH, "//button[@type='button']").click()

driver.find_element(By.XPATH, "//input[@target_name='chat']").click()

chatItems = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")

for chatItem in chatItems:
    if chatItem.text == "2:form_finish":
        chatItem.click()
        break
time.sleep(1)

driver.find_element(By.XPATH, "//button[@class='icon save']").click()

driver.find_element(By.XPATH, "(//i[@class='ico save'])[6]").click()
time.sleep(0.5)

navItems = driver.find_elements(By.XPATH, "//div[@class='settings']/dl/dd")

for item in navItems:
    if item.get_attribute("msg") == "navi-flow":
        item.click()
        break
time.sleep(0.5)

################# Chatflow settings #################

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[4]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[4]")).perform()

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[1]").click()

driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[1]").send_keys("form_trigger"+Keys.ENTER)

driver.find_element(By.XPATH, "(//li[@tp='items'])[1]").click()
driver.find_element(By.XPATH, "//input[@name='label']").send_keys("form1")

driver.find_element(By.XPATH, "(//li[@class='buttons']/span)[3]").click()
time.sleep(0.5)

driver.find_element(By.XPATH, "(//div[@class='form-type-select']/div/label)[1]").click()
time.sleep(0.5)

miniappOptions = driver.find_elements(By.XPATH, "//ul[@class='ui-dropdown-opts']/li")

for miniappOption in miniappOptions:
    if miniappOption.text == "form1":
        miniappOption.click()
        break
time.sleep(1)

driver.find_element(By.XPATH, "//button[@class='icon save label']").click()

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[4]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[4]")).perform()

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[2]").click()

driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[2]").send_keys("{{user.ukey1}}", Keys.ALT+Keys.ENTER)
driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[2]").send_keys("{{user.ukey2}}", Keys.ALT+Keys.ENTER)
driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[2]").send_keys("{{user.ukey3}}", Keys.ALT+Keys.ENTER)
driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[2]").send_keys("{{user.ukey4}}", Keys.ALT+Keys.ENTER)
driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[2]").send_keys("{{user.ukey5}}", Keys.ALT+Keys.ENTER)
driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[2]").send_keys("{{user.ukey6}}", Keys.ALT+Keys.ENTER)
driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[2]").send_keys("{{user.ukey7}}", Keys.ALT+Keys.ENTER)
driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[2]").send_keys("{{user.ukey8}}", Keys.ENTER)

driver.refresh()

########booking
navItems = driver.find_elements(By.XPATH, "//nav[@class='btns app-menus']/a")
time.sleep(0.5)
for item in navItems:
    if item.get_attribute("name") == "rms_view":
        item.click()
        break
time.sleep(0.5)

driver.find_element(By.XPATH, "//li[@fid='store_list']").click()

driver.find_element(By.XPATH, "//div[@class='buttons']/button[@class='new icon plus-square']").click()
time.sleep(0.8)

driver.find_element(By.XPATH, "//div[@class='form-type-text']/input[@name='uri']").send_keys("https://anybot.me/")

driver.find_element(By.XPATH, "//div[@class='form-type-text']/input[@name='title']").send_keys("store1")

driver.find_element(By.XPATH, "//div[@class='form-item-file']").click()
time.sleep(1)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\flamingo.jpg")
time.sleep(3)
autoit.control_click("Открытие", "Button1")
time.sleep(1)

driver.find_element(By.XPATH, "//textarea[@name='desc']").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla pellentesque fringilla dolor. Vestibulum felis massa, vestibulum eget.")

driver.find_element(By.XPATH, "//div[@class='form-type-text']/input[@name='address']").send_keys("15-1 Udagawacho, Shibuya City, Tokyo 150-0042")

driver.find_element(By.XPATH, "//div[@class='form-type-time']/div/select[@name='open_time.hour']").click()

weekendHours = driver.find_elements(By.XPATH, "//select[@name='open_time.hour']/option")

for hour in weekendHours:
    if hour.get_attribute("value") == "11":
        hour.click()
        break

driver.find_element(By.XPATH, "//div[@class='form-type-time']/div/select[@name='close_time.hour']").click()

weekendHours = driver.find_elements(By.XPATH, "//select[@name='close_time.hour']/option")

for hour in weekendHours:
    if hour.get_attribute("value") == "17":
        hour.click()
        break

driver.find_element(By.XPATH, "(//b[@class='form-item-switch'])[1]").click()

driver.find_element(By.XPATH, "(//div[@class='ui-dropdown form-item'])[1]").click()
time.sleep(0.5)

seatsNumber = driver.find_elements(By.XPATH, "//ul[@class='ui-dropdown-opts']/li")
for seat in seatsNumber:
    if seat.get_attribute("val") == "2":
        seat.click()
        break

time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@name='capacity_default']").clear()
driver.find_element(By.XPATH, "//input[@name='capacity_default']").send_keys("1")

driver.find_element(By.XPATH, "//input[@name='public_holidays_f']").click()

driver.find_element(By.XPATH, "//textarea[@name='break_time']").send_keys("13:00-14:00")

driver.find_element(By.XPATH, "(//div[@class='buttons']/button)[5]").click()

driver.refresh()

navItems = driver.find_elements(By.XPATH, "//nav[@class='btns app-menus']/a")
time.sleep(0.5)
for item in navItems:
    if item.get_attribute("name") == "bot_edit_view":
        item.click()
        break
time.sleep(0.5)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[5]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[5]")).perform()

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//dd[@rt='text']")).send_keys("booking_trigger" + Keys.ENTER).perform()

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//dd[@rt='text']")).send_keys("booking_confirm" + Keys.ENTER).perform()

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//dd[@rt='text']")).send_keys("booking_reminder" + Keys.ENTER).perform()

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//dd[@rt='text']")).send_keys("booking_followup" + Keys.ENTER).perform()

navItems = driver.find_elements(By.XPATH, "//div[@class='settings']/dl/dd")

for item in navItems:
    if item.get_attribute("msg") == "navi-miniapp":
        item.click()
        break

time.sleep(1)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//nav[@class='navi']/div)[7]")).perform()
action.click(driver.find_element(By.XPATH, "//dd[@act='group']/b[@class='icon group']")).perform()
time.sleep(0.5)

driver.find_element(By.XPATH, "//form[@data-name='form']/ul/li/div/input[@name='title']").clear()
driver.find_element(By.XPATH, "//form[@data-name='form']/ul/li/div/input[@name='title']").send_keys("seats")

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(0.5)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//nav[@class='navi']/div)[7]")).perform()
action.click(driver.find_element(By.XPATH, "//dd[@act='group']/b[@class='icon group']")).perform()

driver.find_element(By.XPATH, "(//input[@name='title'])[3]").clear()
driver.find_element(By.XPATH, "(//input[@name='title'])[3]").send_keys("calendar1")
time.sleep(0.5)

driver.find_element(By.XPATH, "//input[@target_name='store_ids']").click()

storeItems = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")

for store in storeItems:
    if store.text == "store1":
        store.click()
        break
time.sleep(0.2)

formOptions = driver.find_elements(By.XPATH, "//div[@class='form-type-radio row']/label/input")

for formOption in formOptions:
    if formOption.get_attribute("value") == "calendar":
        formOption.click()
        break
time.sleep(0.2)

driver.find_element(By.XPATH, "//button[@class='icon save']").click()

driver.refresh()

navItems = driver.find_elements(By.XPATH, "//div[@class='settings']/dl/dd")

for item in navItems:
    if item.get_attribute("msg") == "navi-miniapp":
        item.click()
        break

time.sleep(0.2)

driver.find_element(By.XPATH, "(//section[@class='left-pane group-pane']/ul/li)[3]").click()

driver.find_element(By.XPATH, "(//section[@class='comp-mask'])[2]").click()
driver.find_element(By.XPATH, "(//i[@class='ico trash'])[2]").click()

driver.find_element(By.XPATH, "(//section[@class='comp-mask'])[2]").click()
driver.find_element(By.XPATH, "(//i[@class='ico trash'])[2]").click()

driver.find_element(By.XPATH, "(//section[@class='left-pane group-pane']/ul/li)[3]").click()

action = ActionChains(driver)

action.move_to_element(driver.find_element(By.XPATH, "(//div[@class='edit-bar'])[1]")).perform()
action.move_to_element(driver.find_element(By.XPATH, "(//dd[@tp='formitems'])[1]")).perform()

formItems = driver.find_elements(By.XPATH, "(//dl[@class='sub formitems'])[1]/dd")

for dropdown in formItems:
    if dropdown.get_attribute("tp") == "dropdown":
        #time.sleep(0.5)
        dropdown.click()
        break

driver.find_element(By.XPATH, "(//input[@name='title'])[1]").send_keys("Select number of attendees:")

driver.find_element(By.XPATH, "(//textarea[@name='options'])[1]").send_keys("1人" + Keys.ENTER + "2人" + Keys.ENTER)

driver.find_element(By.XPATH, "(//input[@name='name'])[2]").send_keys("rms_seats")

driver.find_element(By.XPATH, "(//b[@class='form-item-switch'])[2]").click()

driver.find_element(By.XPATH, "(//i[@class='ico save'])[2]").click()
time.sleep(1.5)

driver.find_element(By.XPATH, "(//section[@class='left-pane group-pane']/ul/li)[3]").click()

driver.find_element(By.XPATH, "(//section[@class='comp-mask'])[3]").click()
time.sleep(0.5)

driver.find_element(By.XPATH, "//button[@type='button']").click()
time.sleep(0.5)

driver.find_element(By.XPATH, "//input[@value='view']").click()
time.sleep(0.5)

driver.find_element(By.XPATH, "//input[@target_name='view']").click()
time.sleep(0.5)

chatItems = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")

for viewItem in chatItems:
    if viewItem.text == "calendar1":
        viewItem.click()
        break
time.sleep(1)

driver.find_element(By.XPATH, "//button[@class='icon save']").click()

driver.find_element(By.XPATH, "(//i[@class='ico save'])[3]").click()

time.sleep(0.5)

driver.find_element(By.XPATH, "(//section[@class='left-pane group-pane']/ul/li)[4]").click()

driver.find_element(By.XPATH, "(//section[@class='comp-mask'])[1]").click()
time.sleep(0.5)

driver.find_element(By.XPATH, "//input[@value='chat']").click()
time.sleep(0.5)

driver.find_element(By.XPATH, "//input[@target_name='chat']").click()
time.sleep(0.5)

chatOptions = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")

for chatOption in chatOptions:
    if chatOption.text == "2:booking_confirm":
        chatOption.click()
        break
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='name']").send_keys("rms_start_datetime")

driver.find_element(By.XPATH, "(//i[@class='ico save'])[1]").click()

driver.refresh()

#################################chatflow
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[5]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[5]")).perform()

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[1]").click()
driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[1]").send_keys("booking_trigger"+Keys.ENTER)

driver.find_element(By.XPATH, "(//li[@tp='items'])[1]").click()
driver.find_element(By.XPATH, "//label[@class='icon cog advanced-button']").click()

driver.find_element(By.XPATH, "//input[@name='label']").send_keys("start booking")

driver.find_element(By.XPATH, "//li/span[@tp='app']").click()
time.sleep(0.5)

driver.find_element(By.XPATH, "//li[@name='viewid']/div/div").click()
time.sleep(0.5)

appList = driver.find_elements(By.XPATH, "//ul[@class='ui-dropdown-opts']/li")
for app in appList:
    if app.text == "seats":
        app.click()
        break

driver.find_element(By.XPATH, "//button[@class='icon save label']").click()

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[2]").click()
driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[2]").send_keys("Date: {{user.rms_start_datetime}}" + Keys.ALT+Keys.ENTER)
driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[2]").send_keys("Seats: {{user.rms_seats}}" + Keys.ALT+Keys.ENTER)
driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[2]").send_keys("Confirm booking?" + Keys.ENTER)

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[3]").click()
driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[3]").send_keys("{{user.rms_start_datetime}} booking_reminder" + Keys.ENTER)

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[4]").click()
driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[4]").send_keys("{{user.rms_start_datetime}} booking_followup" + Keys.ENTER)

driver.find_element(By.XPATH, "(//li[@tp='items'])[5]").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "//label[@class='icon cog advanced-button']").click()

time.sleep(0.5)
driver.find_element(By.XPATH, "//button[@class='vip ext-btn icon biz']").click()

time.sleep(0.5)
advancedSettings = driver.find_elements(By.XPATH, "//dl[@class='ui-tab-menu']/dd")
for advancedSetting in advancedSettings:
    if advancedSetting.get_attribute("name") == "rms":
        advancedSetting.click()
        break

time.sleep(0.5)
driver.find_element(By.XPATH, "(//b[@class='form-item-switch'])[2]").click()
driver.find_element(By.XPATH, "//input[@target_name='store_id']").click()

storeOptions = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")

for store in storeOptions:
    if store.text == "store1":
        store.click()
        break

time.sleep(0.5)

driver.find_element(By.XPATH, "//input[@name='before_day']").send_keys("1")
driver.find_element(By.XPATH, "//input[@name='before_hour']").send_keys("15")

driver.find_element(By.XPATH, "//input[@target_name='before_acts']").click()
time.sleep(1)
beforeActions = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")

for beforeAction in beforeActions:
    if beforeAction.text == "3:booking_reminder":
        beforeAction.click()
        break
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='after_day']").send_keys("1")
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@name='after_hour']").send_keys("10")

time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@target_name='after_acts']").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@target_name='after_acts']").send_keys("booking_followup"+Keys.ENTER)

time.sleep(1)
driver.find_element(By.XPATH, "(//button[@class='icon save label'])[2]").click()

driver.find_element(By.XPATH, "//input[@name='label']").send_keys("confirm?"+Keys.ENTER)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[7]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[7]")).perform()
action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//label[normalize-space()='Text']")).send_keys("webhook1"+Keys.ENTER).perform()
action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//label[normalize-space()='Text']")).send_keys("webhook2"+Keys.ENTER).perform()
action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//label[normalize-space()='Text']")).send_keys("webhook3"+Keys.ENTER).perform()
action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()

driver.refresh()
time.sleep(1)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[7]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[7]")).perform()

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[1]").click()

driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[1]").send_keys("webhook1"+Keys.ENTER)

driver.find_element(By.XPATH, "(//li[@tp='items'])[1]").click()

driver.find_element(By.XPATH, "//label[@class='icon cog advanced-button']").click()

time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@name='label']").send_keys("button1")

time.sleep(0.5)
driver.find_element(By.XPATH, "//li[@class='exps ext-btns']/button").click()

time.sleep(0.5)

extensions = driver.find_elements(By.XPATH, "//dl[@class='ui-tab-menu']/dd")

for extension in extensions:
    if extension.get_attribute("name") == "webhook":
        extension.click()
        break

time.sleep(0.5)

driver.find_element(By.XPATH, "//ul[@class='webhook-params']/li/input[@name='uri']").send_keys("/api/service/common/save_ukey")

driver.find_element(By.XPATH, "//ul[@class='webhook-params']/li/input[@name='key']").send_keys("bid")

driver.find_element(By.XPATH, "//ul[@class='webhook-params']/li/div/input[@type='text']").click()

time.sleep(1)
autocompleteOptions = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")

for option in autocompleteOptions:
    if option.get_attribute("val") == "bot.bid":
        option.click()
        break

driver.find_element(By.XPATH, "//i[@class='icon plus-square']").click()
time.sleep(0.5)

driver.find_element(By.XPATH, "(//ul[@class='webhook-params']/li/input[@name='key'])[2]").send_keys("uid")

driver.find_element(By.XPATH, "(//ul[@class='webhook-params']/li/div/input[@type='text'])[2]").click()

time.sleep(1)
autocompleteOptions = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")

for option in autocompleteOptions:
    if option.get_attribute("val") == "user.id":
        option.click()
        break

driver.find_element(By.XPATH, "//i[@class='icon plus-square']").click()
time.sleep(0.5)

driver.find_element(By.XPATH, "(//ul[@class='webhook-params']/li/input[@name='key'])[3]").send_keys("whtest1"+Keys.ENTER)
time.sleep(0.5)

driver.find_element(By.XPATH, "(//ul[@class='webhook-params']/li/div/input[@type='text'])[3]").send_keys("TEST Not testedED"+Keys.ENTER)
time.sleep(1)

driver.find_element(By.XPATH, "//div[@class='ui-tab-menu-container']/footer/button").click()

driver.find_element(By.XPATH, "//button[@scheme='reaction']").click()

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[2]").click()

driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[2]").send_keys("webhook2"+Keys.ENTER)

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[3]").click()

driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[3]").send_keys("{{user.whtest1}}"+Keys.ENTER)

driver.refresh()
time.sleep(1)

#transition item2>item3

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[7]")).perform()

action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[7]")).perform()

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[2]").click()

driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li[@class='item new'])[2]").click()

time.sleep(0.5)

driver.find_element(By.XPATH, "//div[@class='form-type-text']/input[@name='label']").send_keys("button2")
time.sleep(0.5)

driver.find_element(By.XPATH, "//button[@class='icon save label']").click()

#### Coupons & Saved group ####

navItems = driver.find_elements(By.XPATH, "//nav[@class='btns app-menus']/a")
time.sleep(0.5)
for item in navItems:
    if item.get_attribute("name") == "coupon_list_view":
        item.click()
        break
time.sleep(0.5)

driver.find_element(By.XPATH, "//button[@class='new icon plus-circle']").click()

driver.find_element(By.XPATH, "//input[@name='title']").clear()
driver.find_element(By.XPATH, "//input[@name='title']").send_keys("TestCoupon")

driver.find_element(By.XPATH, "//div[@class='default']").click()

time.sleep(1)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\wood1.jpg")
time.sleep(4)
autoit.control_click("Открытие", "Button1")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='discount']").clear()
driver.find_element(By.XPATH, "//input[@name='discount']").send_keys("16")

driver.find_element(By.XPATH, "//input[@value='JPY']").click()

driver.find_element(By.XPATH, "//input[@name='linkto']").send_keys("https://anybot.me/")

driver.find_element(By.XPATH, "//textarea[@name='desc']").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis nulla tortor, consectetur non lectus a, sagittis.")

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(0.5)

driver.find_element(By.XPATH, "//button[@class='new icon plus-circle']").click()

driver.find_element(By.XPATH, "//input[@name='title']").clear()
driver.find_element(By.XPATH, "//input[@name='title']").send_keys("サシャ")

driver.find_element(By.XPATH, "//div[@class='default']").click()

time.sleep(1)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\wood2.jpg")
time.sleep(4)
autoit.control_click("Открытие", "Button1")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='discount']").clear()
driver.find_element(By.XPATH, "//input[@name='discount']").send_keys("34")

driver.find_element(By.XPATH, "//input[@name='linkto']").send_keys("https://anybot.me/")

driver.find_element(By.XPATH, "//textarea[@name='desc']").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis nulla tortor, consectetur non lectus a, sagittis.")

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(0.5)

driver.find_element(By.XPATH, "//button[@class='new icon plus-circle']").click()

driver.find_element(By.XPATH, "//input[@name='title']").clear()
driver.find_element(By.XPATH, "//input[@name='title']").send_keys("さしゃ")

driver.find_element(By.XPATH, "//div[@class='default']").click()

time.sleep(1)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\wood3.jpg")
time.sleep(4)
autoit.control_click("Открытие", "Button1")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='discount']").clear()
driver.find_element(By.XPATH, "//input[@name='discount']").send_keys("8")

driver.find_element(By.XPATH, "//input[@value='JPY']").click()

driver.find_element(By.XPATH, "//input[@name='linkto']").send_keys("https://anybot.me/")

driver.find_element(By.XPATH, "//textarea[@name='desc']").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis nulla tortor, consectetur non lectus a, sagittis.")

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(0.5)

driver.find_element(By.XPATH, "//button[@class='new icon plus-circle']").click()

driver.find_element(By.XPATH, "//input[@name='title']").clear()
driver.find_element(By.XPATH, "//input[@name='title']").send_keys("沙詩弥")

driver.find_element(By.XPATH, "//div[@class='default']").click()

time.sleep(1)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\wood4.jpg")
time.sleep(4)
autoit.control_click("Открытие", "Button1")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='discount']").clear()
driver.find_element(By.XPATH, "//input[@name='discount']").send_keys("45")

driver.find_element(By.XPATH, "//input[@value='JPY']").click()

driver.find_element(By.XPATH, "//input[@name='linkto']").send_keys("https://anybot.me/")

driver.find_element(By.XPATH, "//textarea[@name='desc']").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis nulla tortor, consectetur non lectus a, sagittis.")

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(0.5)

driver.find_element(By.XPATH, "//button[@class='new icon plus-circle']").click()

driver.find_element(By.XPATH, "//input[@name='title']").clear()
driver.find_element(By.XPATH, "//input[@name='title']").send_keys("20220101")

driver.find_element(By.XPATH, "//div[@class='default']").click()

time.sleep(1)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\wood5.jpg")
time.sleep(4)
autoit.control_click("Открытие", "Button1")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@name='discount']").clear()
driver.find_element(By.XPATH, "//input[@name='discount']").send_keys("31")

driver.find_element(By.XPATH, "//input[@name='linkto']").send_keys("https://anybot.me/")

driver.find_element(By.XPATH, "//textarea[@name='desc']").send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis nulla tortor, consectetur non lectus a, sagittis.")

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(0.5)

driver.find_element(By.XPATH, "//button[@class='new icon plus-circle']").click()

driver.find_element(By.XPATH, "//button[@class='icon save']").click()

driver.refresh()

navItems = driver.find_elements(By.XPATH, "//nav[@class='btns app-menus']/a")
time.sleep(0.5)
for item in navItems:
    if item.get_attribute("name") == "bot_edit_view":
        item.click()
        break
time.sleep(0.5)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[8]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[8]")).perform()
action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//label[normalize-space()='Card']")).send_keys("saved"+Keys.ENTER).perform()
time.sleep(0.5)

driver.find_element(By.XPATH, "//b[@class='icon double-right']").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "(//button[@class='ui-menu'])[2]").click()
time.sleep(0.5)

savedOptions = driver.find_elements(By.XPATH, "//ul[@class='ui-dropdown-opts']/li")
for savedOption in savedOptions:
    if savedOption.text == "Coupons":
        savedOption.click()
        break

time.sleep(0.5)
driver.find_element(By.XPATH, "(//li[@class='item new'])[2]").click()

time.sleep(0.5)
driver.find_element(By.XPATH, "//input[@name='label']").send_keys("save")

driver.find_element(By.XPATH, "//span[@class='icon save tp-stock']").click()
time.sleep(0.5)

driver.find_element(By.XPATH, "//button[@class='icon save label']").click()

driver.refresh()

##### Swipe #####

driver.find_element(By.XPATH, "//a[@class='miniapps icon dots-v']").click()
time.sleep(0.5)

submenuItems = driver.find_elements(By.XPATH, "//section[@class='submenus']/ul/li")
for submenu in submenuItems:
    if submenu.text == "Catalog":
        submenu.click()
        break
time.sleep(0.5)

###### Catalog items setting #####
driver.find_element(By.XPATH, "//button[@class='new icon plus-square']").click()

driver.find_element(By.XPATH, "//input[@name='linkto']").clear()
driver.find_element(By.XPATH, "//input[@name='linkto']").send_keys("https://anybot.me/")

driver.find_element(By.XPATH, "//input[@name='title']").clear()
driver.find_element(By.XPATH, "//input[@name='title']").send_keys("Soup")

driver.find_element(By.XPATH, "//textarea[@name='desc']").send_keys("Lorem ipsum dolor sit amet, consectetur amet.")

driver.find_element(By.XPATH, "//div[@class='form-item-file']").click()
time.sleep(1)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\soup.jpg")
time.sleep(3)
autoit.control_click("Открытие", "Button1")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@target_name='category']").send_keys("food" + Keys.ENTER)

driver.find_element(By.XPATH, "//input[@name='price']").send_keys("0")

time.sleep(1)
driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//button[@class='new icon plus-square']").click()

driver.find_element(By.XPATH, "//input[@name='linkto']").clear()
driver.find_element(By.XPATH, "//input[@name='linkto']").send_keys("https://anybot.me/")

driver.find_element(By.XPATH, "//input[@name='title']").clear()
driver.find_element(By.XPATH, "//input[@name='title']").send_keys("Salad")

driver.find_element(By.XPATH, "//textarea[@name='desc']").send_keys("Lorem ipsum dolor sit amet, consectetur amet.")

driver.find_element(By.XPATH, "//div[@class='form-item-file']").click()
time.sleep(1)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\salad.jpg")
time.sleep(3)
autoit.control_click("Открытие", "Button1")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@target_name='category']").send_keys("food" + Keys.ENTER)

driver.find_element(By.XPATH, "//input[@name='price']").send_keys("0")
time.sleep(1)

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//button[@class='new icon plus-square']").click()

driver.find_element(By.XPATH, "//input[@name='linkto']").clear()
driver.find_element(By.XPATH, "//input[@name='linkto']").send_keys("https://anybot.me/")

driver.find_element(By.XPATH, "//input[@name='title']").clear()
driver.find_element(By.XPATH, "//input[@name='title']").send_keys("Drink")

driver.find_element(By.XPATH, "//textarea[@name='desc']").send_keys("Lorem ipsum dolor sit amet, consectetur amet.")

driver.find_element(By.XPATH, "//div[@class='form-item-file']").click()
time.sleep(1)
autoit.win_activate("Открытие")
time.sleep(1)
autoit.control_set_text("Открытие", "Edit1", r"C:\Users\Professional\PycharmProjects\22_09_version\drink.jpg")
time.sleep(3)
autoit.control_click("Открытие", "Button1")
time.sleep(1)

driver.find_element(By.XPATH, "//input[@target_name='category']").send_keys("food" + Keys.ENTER)

driver.find_element(By.XPATH, "//input[@name='price']").send_keys("0")
time.sleep(1)

driver.find_element(By.XPATH, "//button[@class='icon save']").click()
time.sleep(2)

driver.refresh()

navItems = driver.find_elements(By.XPATH, "//nav[@class='btns app-menus']/a")
time.sleep(0.5)
for item in navItems:
    if item.get_attribute("name") == "bot_edit_view":
        item.click()
        break
time.sleep(0.5)

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[9]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[9]")).perform()
time.sleep(0.5)

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//dd[@rt='text']")).send_keys("swipe_start" + Keys.ENTER).perform()
time.sleep(0.5)

action.move_to_element(driver.find_element(By.XPATH, "//button[normalize-space()='New Action']")).perform()
action.click(driver.find_element(By.XPATH, "//dd[@rt='text']")).send_keys("swipe_finish" + Keys.ENTER).perform()
driver.refresh()

action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[9]")).perform()
action.click(driver.find_element(By.XPATH, "(//ul[@class='groups']/li/h5)[9]")).perform()

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[1]").click()
driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[1]").send_keys("Start swipe!"+Keys.ENTER)

driver.find_element(By.XPATH, "(//li[@tp='items'])[1]").click()
driver.find_element(By.XPATH, "//input[@name='label']").send_keys("Swipe")

driver.find_element(By.XPATH, "//li/span[@tp='widget']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//ul/li[@class='icon heart']").click()
time.sleep(1)

driver.find_element(By.XPATH, "//input[@target_name='target_type']").click()

targetOptions = driver.find_elements(By.XPATH, "//ul[@class='autocomplete-options']/li")
for targetOption in targetOptions:
    if targetOption.get_attribute("val") == "act":
        targetOption.click()
        break
time.sleep(1)

driver.find_element(By.XPATH, "//button[@class='icon save label']").click()

driver.find_element(By.XPATH, "(//section[@class='actions']/ul/li)[2]").click()
driver.find_element(By.XPATH, "(//ol[@class='card rt-text']/li/textarea)[2]").send_keys("Thank you!"+Keys.ENTER)

driver.refresh()

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
