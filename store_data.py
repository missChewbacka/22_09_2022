import time
import autoit
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
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









