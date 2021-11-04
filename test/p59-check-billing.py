from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys, getopt
from selenium.webdriver import ActionChains

def main(argv):
   try:
      opts, args = getopt.getopt(argv,"h")
   except getopt.GetoptError:
      print ('err')
      sys.exit(2)
      
   headless = False
   for opt, arg in opts:
      if opt in ['-h']:
         headless = True

   if headless:
      driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME, options=options) 
   else:
      driver = webdriver.Chrome(executable_path="../../chromedriver", options=options)
   return driver

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
options = webdriver.ChromeOptions()
options.headless = False
options.add_argument(f'user-agent={user_agent}')
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')

driver = main(sys.argv[1:])
driver.get("https://public.p59.dev/welcome")

#old account = 1111@gmail.com   pwd = Love1111
#new test account = p59testa@gmail.com   pwd Love1111

link = driver.find_element_by_xpath(
    #'//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[3]'
    'html/body/app-root/p-sidebar/div/div/div/app-welcome-page-header/div/div[2]/span[4]')
link.click()
print('start test')
print('click login')

time.sleep(5)
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('pitch59testa+1@gmail.com')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('Love1111')

logIn = driver.find_element_by_xpath(
    '/html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button')
logIn.click()
time.sleep(2)
print('log in')

portal = driver.find_element_by_xpath(
    '/html/body/app-root/p-sidebar/div/div/div/app-welcome-page-header/div/div[2]/span[2]'
)
portal.click()
time.sleep(2)

billing_button = driver.find_element_by_xpath(
    '/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-employer-portal/div/div/div/div/div/div/div[2]/div[2]/div/div'
)
billing_button.click()
time.sleep(2)


# Change fields in the more info section. Save the changes, then revert them and save again.
more_info = driver.find_element_by_xpath(
    '/html/body/div/div/div[2]/app-ep-layout/div[2]/div/div/div/app-stepper/div/div/p-carousel/div/div/div/div/div/div[3]/div'
)
more_info.click()
time.sleep(2)

drop_down = driver.find_element_by_xpath(
    '/html/body/div/div/div[2]/app-ep-layout/div[2]/div/div/div[2]/div/app-more-info/div/form/div/span/p-multiselect/div'
)
drop_down.click()
time.sleep(2)

item = driver.find_element_by_xpath(
    '/html/body/div/div/div[2]/app-ep-layout/div[2]/div/div/div[2]/div/app-more-info/div/form/div/span/p-multiselect/div/div[4]/div/ul/p-multiselectitem[3]/li'
)
item.click()
time.sleep(1)

text_box = driver.find_element_by_xpath(
    '/html/body/div/div/div[2]/app-ep-layout/div[2]/div/div/div[2]/div/app-more-info/div/form/div[3]/textarea'
)
text_box.send_keys('This is test information, but I am sure the real information will be pretty spiffy')
time.sleep(1)

save = driver.find_element_by_xpath(
    '/html/body/div/div/div[2]/app-ep-layout/div[2]/div/div/div[3]/div/div[2]/div'
)
save.click()
time.sleep(2)

# Clear data
more_info = driver.find_element_by_xpath(
    '/html/body/div/div/div[2]/app-ep-layout/div[2]/div/div/div/app-stepper/div/div/p-carousel/div/div/div/div/div/div[3]/div'
)
more_info.click()
time.sleep(2)

drop_down = driver.find_element_by_xpath(
    '/html/body/div/div/div[2]/app-ep-layout/div[2]/div/div/div[2]/div/app-more-info/div/form/div/span/p-multiselect/div'
)
drop_down.click()
time.sleep(2)

item = driver.find_element_by_xpath(
    '/html/body/div/div/div[2]/app-ep-layout/div[2]/div/div/div[2]/div/app-more-info/div/form/div/span/p-multiselect/div/div[4]/div/ul/p-multiselectitem[3]/li'
)
item.click()
time.sleep(1)

text_box = driver.find_element_by_xpath(
    '/html/body/div/div/div[2]/app-ep-layout/div[2]/div/div/div[2]/div/app-more-info/div/form/div[3]/textarea'
)
text_box.clear()
time.sleep(2)

save = driver.find_element_by_xpath(
    '/html/body/div/div/div[2]/app-ep-layout/div[2]/div/div/div[3]/div/div[2]/div'
)
save.click()
time.sleep(2)

# Exit more info
exit = driver.find_element_by_xpath(
    '/html/body/div/div/div/div/a/span'
)
exit.click()
time.sleep(1)

profi = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[3]/div/div')
profi.click()
time.sleep(2)

logOut = driver.find_element_by_xpath(
   '/html/body/app-root/p-sidebar/div[2]/div/div/div[2]/div'
)
logOut.click()
time.sleep(2)
print('test done')