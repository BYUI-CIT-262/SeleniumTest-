from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys, getopt
from p59_job_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


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

time.sleep(5)

########Clicks on the edit button
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-employer-portal/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div"))).click()
print('click on edit button')



#######Clicks on the billing button. 
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/app-ep-layout/div[2]/div/div/div[1]/app-stepper/div/div/p-carousel/div/div/div/div/div/div[1]/div"))).click()
print('click on billing button')



########Clicks on the information button. Will delete information and renter it.
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/app-ep-layout/div[2]/div/div/div[1]/app-stepper/div/div/p-carousel/div/div/div/div/div/div[2]"))).click()
print('click on the more info button')

#delete the business name and reenter "P59 Test"
driver.find_element_by_id("businessName").clear()
time.sleep(1)
driver.find_element_by_id("businessName").send_keys('P59 Test')

#delete the your name and reenter "John Brown"
driver.find_element_by_id("title").clear()
time.sleep(1)
driver.find_element_by_id("title").send_keys('John Brown')

#delete the email and reenter "jbrown@gmail.com"
time.sleep(3)
driver.find_element_by_id("email").clear() 
time.sleep(3)
driver.find_element_by_id("email").send_keys('jbrown@gmail.com')

#delete the phone number and reenter "(123) 456-7890"
driver.find_element_by_id("contactNumber").clear()
time.sleep(1)
driver.find_element_by_id("contactNumber").send_keys('(123) 456-7890')

#enter jibberish into the website and then delete that info
driver.find_element_by_id("websiteLink").send_keys('Blorpity Florp. Delete me!')
time.sleep(1)
driver.find_element_by_id("websiteLink").clear()

#delete the address and reenter "1009 Larch Drive"
driver.find_element_by_id("address").clear()
time.sleep(1)
driver.find_element_by_id("address").send_keys('1009 Larch Drive')

#delete the city and reenter "Rexburg"
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/app-ep-layout/div[2]/div/div/div[2]/div/div/app-enter-information/form/div/div[2]/span[3]/p-autocomplete/span/input").clear()
driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/app-ep-layout/div[2]/div/div/div[2]/div/div/app-enter-information/form/div/div[2]/span[3]/p-autocomplete/span/input").send_keys('Rexburg')

# #delete the state and reenter "ID"
# driver.find_element_by_id("").clear()
# driver.find_element_by_id("").send_keys('ID')

#delete the zip code and reenter "83440"
driver.find_element_by_id("zip").clear()
time.sleep(1)
driver.find_element_by_id("zip").send_keys('83440')
#check and uncheck the "Hide your address from customers"

########Clicks on the more info button. Will delete information and renter it.
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/app-ep-layout/div[2]/div/div/div[1]/app-stepper/div/div/p-carousel/div/div/div/div/div/div[3]"))).click()
# print('click on the more info button')



# #########Clicks on the images button
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/app-ep-layout/div[2]/div/div/div[1]/app-stepper/div/div/p-carousel/div/div/div/div/div/div[4]"))).click()
# print('click on the images button')




########Clicks on the edit button
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-employer-portal/div[1]/div/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div/img"))).click()
print('click on edit button')



#######Clicks on the billing button. Will delete information and reenter it.
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/app-ep-layout/div[2]/div/div/div[1]/app-stepper/div/div/p-carousel/div/div/div/div/div/div[1]/div"))).click()
print('click on billing button')



########Clicks on the information button. Will delete information and renter it.
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/app-ep-layout/div[2]/div/div/div[1]/app-stepper/div/div/p-carousel/div/div/div/div/div/div[2]"))).click()
print('click on the more info button')

#delete the business name and reenter "P59 Test"
driver.find_element_by_id("businessName").clear()
time.sleep(1)
driver.find_element_by_id("businessName").send_keys('P59 Test')

#delete the your name and reenter "John Brown"
driver.find_element_by_id("title").clear()
time.sleep(1)
driver.find_element_by_id("title").send_keys('John Brown')

#delete the email and reenter "jbrown@gmail.com"
time.sleep(3)
driver.find_element_by_id("email").clear() 
time.sleep(1)
driver.find_element_by_id("email").send_keys('jbrown@gmail.com')

#delete the phone number and reenter "(123) 456-7890"
driver.find_element_by_id("contactNumber").clear()
time.sleep(1)
driver.find_element_by_id("contactNumber").send_keys('(123) 456-7890')

#enter jibberish into the website and then delete that info
driver.find_element_by_id("websiteLink").send_keys('Blorpity Florp. Delete me!')
time.sleep(1)
driver.find_element_by_id("websiteLink").clear()

#delete the address and reenter "1009 Larch Drive"
driver.find_element_by_id("address").clear()
time.sleep(1)
driver.find_element_by_id("address").send_keys('1009 Larch Drive')

#delete the city and reenter "Rexburg"
driver.find_element_by_id("/html/body/div[1]/div/div[2]/app-ep-layout/div[2]/div/div/div[2]/div/div/app-enter-information/form/div/div[2]/span[3]/p-autocomplete/span/input").clear()
driver.find_element_by_id("/html/body/div[1]/div/div[2]/app-ep-layout/div[2]/div/div/div[2]/div/div/app-enter-information/form/div/div[2]/span[3]/p-autocomplete/span/input").send_keys('Rexburg')

# #delete the state and reenter "ID"
# driver.find_element_by_id("").clear()
# driver.find_element_by_id("").send_keys('ID')

#delete the zip code and reenter "83440"
driver.find_element_by_id("zip").clear()
time.sleep(1)
driver.find_element_by_id("zip").send_keys('83440')
#check and uncheck the "Hide your address from customers"

########Clicks on the more info button. Will delete information and renter it.
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/app-ep-layout/div[2]/div/div/div[1]/app-stepper/div/div/p-carousel/div/div/div/div/div/div[3]"))).click()
# print('click on the more info button')



# #########Clicks on the images button
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/app-ep-layout/div[2]/div/div/div[1]/app-stepper/div/div/p-carousel/div/div/div/div/div/div[4]"))).click()
# print('click on the images button')



sys.exit()

logout()

driver.back()
# time.sleep(5)
print("test end")
driver.quit()

