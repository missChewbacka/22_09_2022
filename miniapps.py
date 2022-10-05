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

driver.quit()




