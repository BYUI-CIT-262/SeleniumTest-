from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys, getopt
from p59_job_utils import *

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


print('test start')

login(driver)
print('log in')

profile(driver)
print('click profile')

time.sleep(2)

employeePortal(driver)
print('click employee portal')

time.sleep(2)

#
# Moves the slider switch to the deactivate position in Employer Portal
#
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > main > app-history-favorites-layout > div > div > div > div > div > div.p-col-12.p-md-8.p-lg-9.container-layout > app-account-employer-portal > div.ng-star-inserted > div > div > div.ep-body.ng-star-inserted > app-employer-portal-table > div > p-table > div > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > div > p-inputswitch > div > span"))).click()
print('toggle off Employee portal')
time.sleep(2)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > main > app-history-favorites-layout > div > div > div > div > div > div.p-col-12.p-md-8.p-lg-9.container-layout > app-account-employer-portal > div.ng-star-inserted > div > div > div.ep-body.ng-star-inserted > app-employer-portal-table > div > p-table > div > div > table > tbody > tr:nth-child(2) > td:nth-child(4) > div > p-inputswitch > div > span"))).click()
print('toggle on Employee portal')


logout(driver)
print('logout')

driver.back()
# time.sleep(5)
print("test end")
driver.quit()