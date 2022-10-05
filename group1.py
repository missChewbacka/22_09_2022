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

