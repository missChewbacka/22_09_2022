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
driver.find_element(By.CSS_SELECTOR, "#pass").send_keys("221373897")
driver.find_element(By.CSS_SELECTOR, ".show-mail-login").click()

time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(text(),'test-br-v2')]").click()

time.sleep(4)

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

#time.sleep(2)
#driver.find_element(By.XPATH, "//footer[@class='exps']/button[@class='icon save label']']").click()