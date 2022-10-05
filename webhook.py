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
driver.find_element(By.CSS_SELECTOR, "#pass").send_keys("221373897qw")
driver.find_element(By.CSS_SELECTOR, ".show-mail-login").click()

time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(text(),'test_bot')]").click()

time.sleep(4)

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

