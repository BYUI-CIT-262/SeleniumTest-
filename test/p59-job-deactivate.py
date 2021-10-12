from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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

profile(driver)

employeePortal(driver)

#
# Moves the slider switch to the deactivate position in Employer Portal
#
deactivate = driver.find_element_by_xpath(
    
'/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-employer-portal/div[1]/div/div[2]/app-employer-portal-table/div/p-table/div/div/table/tbody/tr[1]/td[4]/div/p-inputswitch/div/div/input'
)
deactivate.click()
print('slide to deactivate')    

sys.exit()

logout()

driver.back()
# time.sleep(5)
print("test end")
driver.quit()