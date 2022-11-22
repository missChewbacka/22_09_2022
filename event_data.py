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

driver.find_element(By.XPATH, "//*[contains(text(),'Glenn_1011_Api1.0')]").click()

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