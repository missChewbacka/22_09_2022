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

####################
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




