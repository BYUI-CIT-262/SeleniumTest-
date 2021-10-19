from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys, getopt


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
      driver = webdriver.Chrome(executable_path="chromedriver", options=options)
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

print('test start')
link = driver.find_element_by_xpath(
    '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[3]')
link.click()
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

# contact = driver.find_element_by_xpath(
#     '//*[@id="search-swiper-pr_id_9"]/swiper/div/div[1]/div[3]/app-search-result-thumbnail/div/div[5]/div[2]')
# time.sleep(3)

# contact.click()
# time.sleep(3)

# rightBotton = driver.find_element_by_xpath(
#     '//*[@id="search-swiper-pr_id_9"]/swiper/div/div[4]')
# rightBotton.click()
# time.sleep(2)
# rightBotton.click()
# time.sleep(2)
# print('click right arrow on the pitch card')

profi = driver.find_element_by_xpath(
    '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[4]/div')
profi.click()
time.sleep(2)

logOut = driver.find_element_by_xpath(
    '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/p-overlaypanel[2]/div/div/div/div[2]/div')
logOut.click()
print('click profile and log out')

time.sleep(2)
driver.back()

# time.sleep(5)
print("test end")
driver.quit()
# log in
# //*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[3]

# Email
# //*[@id="email"]

# password
# //*[@id="password"]

# logIn button
# /html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button
