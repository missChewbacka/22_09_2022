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
driver.find_element(By.XPATH, "//*[contains(text(),'Glenn_1011_Api1.0')]").click()

time.sleep(4)

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




