
import selenium.webdriver.common.by as By
from selenium import webdriver as wd
import selenium.webdriver.common.keys as Keys
import time
### chromedriver included
driver = wd.Chrome(executable_path='C:\chrome_driver\chromedriver')
######################## EPNM server login
driver.get('https://10.65.205.49')
driver.find_element_by_xpath('//*[@id="label_username"]').send_keys('root')
driver.find_element_by_xpath('//*[@id="label_password"]').send_keys('Public123')
driver.find_element_by_id('loginPage_LoginButton_label').click()
driver.set_page_load_timeout(100)
### To maximize the window
driver.maximize_window()
### After login will print the page (EPNM) title
print(driver.title)
driver.implicitly_wait(60)

#### manage licence popop
#driver.find_element_by_class_name('dijitReset dijitInline dijitButtonText').click()
driver.find_element_by_xpath('//span[@id="xwt_widget_form_TextButton_2_label"]').click()
### To click the "Open Navigation"
driver.find_element_by_xpath('//div[@class="toggleIcon icon-cisco-menu"]').click()
print('Open Navigation: window clicked')
driver.implicitly_wait(10)
### To click the "Inventory" navigation
driver.find_element_by_xpath('//a[contains(text(),"Inventory")]').click()
print('"Inventory" navigation clicked')
driver.implicitly_wait(20)
### To click the "Network Devcies" navigation
driver.find_element_by_xpath('//*[contains(@class,"xwtSlide")]//a[text()="Network Devices"]').click()
print('"Network Devices" navigation is clicked')
driver.implicitly_wait(10)
### Trying to take the screenshot
########################### not working as of now
driver.save_screenshot("C:\screen_shot\test.png")
print('Screenshot1 taken , please check in C:\screen_shot\yyest.png')
driver.get_screenshot_as_file("sample_screenshot_2.png")
print('Screenshot1 taken , please check in ....')

##### completed string entred to filter the completed
driver.implicitly_wait(10)
driver.find_element_by_xpath('//input[@aria-label="Last Inventory Collection Status"]').send_keys('Completed')

##### to select all for sync initiate
driver.implicitly_wait(10)
time.sleep(10)
driver.find_element_by_xpath('//input[@type="checkbox" and @class="select-all"]').click()

### click the Yes button in procceed
driver.implicitly_wait(10)
time.sleep(10)
driver.find_element_by_xpath('//span[@id="syncDeviceButton_label"]').click()
print('Sync:yes button is clicked')
###??????????????
driver.implicitly_wait(10)
time.sleep(10)
driver.find_element_by_xpath('//span[*="Yes"]').click()

#### ROOT DOMAIN Navigation is clicked
driver.implicitly_wait(10)
time.sleep(10)
driver.find_element_by_xpath('//div[contains(text(),"ROOT-DOMAIN")]').click()
driver.implicitly_wait(10)
print('Root_domain navigation is clicked')

### Logout is clicked
driver.find_element_by_xpath('//td[@id="logout_text"]').click()
time.sleep(10)
print('Log out is clicked')

## close browser
#driver.close()
print('Browser closed')
