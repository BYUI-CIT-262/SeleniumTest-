#from test.utilities.create_user import create_user
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys, getopt
from utilities.create_user import create_user
from utilities.delete_user import delete_user
import requests

# create a dict with the log in username and password to pass into the create_user function

user_id, user_token,user_email = create_user()
print('user created')


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
      driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
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

time.sleep(2)
email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys(user_email)

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('Love1111')

logIn = driver.find_element_by_xpath(
    '/html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button')
logIn.click()
time.sleep(2)
print('log in')
#code starts here----------------------------------------------------------------------------------------
from selenium.common.exceptions import NoSuchElementException        
def check_exists_by_xpath(xpath):
    try:                                                 # DO NOT DELETE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        driver.find_element_by_xpath(xpath)              # DO NOT DELETE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    except NoSuchElementException:                       # DO NOT DELETE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        return False                                     # DO NOT DELETE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    return True                                          # DO NOT DELETE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Check the xpath value################################################################################

create_pitchcard = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[2]/div[1]')
create_pitchcard.click()
print('click create pitchcard')
time.sleep(3)

xpath = '/html/body/app-root/main/app-choose-pitchcard-page/div/div/app-choose-pitchcard/div/div/div[2]/div[5]/div[3]/button'
if check_exists_by_xpath(xpath):
   jobcard=driver.find_element_by_xpath(xpath)
   jobcard.click()
   print('click job card')
else:
   delete_user(id=user_id,token=user_token)
   print('COULD NOT FIND THE DESIRED XPATH')
   print('user deleted')
   driver.quit()

time.sleep(3)


xpath = '/html/body/div[1]/div/div[2]/div/div[4]/div'
if check_exists_by_xpath(xpath):
   jobcard=driver.find_element_by_xpath(xpath)
   jobcard.click()
   print('click create Employer Portal')
   time.sleep(3)
else:
   delete_user(id=user_id,token=user_token)
   print('COULD NOT FIND THE DESIRED XPATH')
   print('user deleted')
   driver.quit()


xpath = '/html/body/app-root/main/app-billing-page/div/div/div/div/div/app-billing-summary/div/div/div[2]/div[1]/div'
if check_exists_by_xpath(xpath):
   jobcard=driver.find_element_by_xpath(xpath)
   jobcard.click()
   print('click add payment method')
   time.sleep(3)

else:
   delete_user(id=user_id,token=user_token)
   print('COULD NOT FIND THE DESIRED XPATH')
   print('user deleted')
   driver.quit()

######################
# add card info
######################
card_number = '4022400001871076'
cvc = '737'
month = '12'
year = '2021'
xpath = '//*[@id="cardNumber"]/input'
if check_exists_by_xpath(xpath):
   jobcard=driver.find_element_by_xpath(xpath)
   jobcard.send_keys(card_number)
   print('add card number')
   time.sleep(2)
else:
   delete_user(id=user_id,token=user_token)
   print('COULD NOT FIND THE DESIRED XPATH')
   print('user deleted')
   driver.quit()

xpath = '//*[@id="month"]/span/input'
if check_exists_by_xpath(xpath):
   jobcard=driver.find_element_by_xpath(xpath)
   jobcard.send_keys(month)
   print('add month')
else:
   delete_user(id=user_id,token=user_token)
   print('COULD NOT FIND THE DESIRED XPATH')
   print('user deleted')
   driver.quit()

xpath = '//*[@id="year"]/span/input'
if check_exists_by_xpath(xpath):
   jobcard=driver.find_element_by_xpath(xpath)
   jobcard.send_keys(month)
   print('add year')
else:
   delete_user(id=user_id,token=user_token)
   print('COULD NOT FIND THE DESIRED XPATH')
   print('user deleted')
   driver.quit()

xpath = '/html/body/div[2]/div/div[2]/div/div[2]/app-payment-method-forms/div/div/div[1]/form/div[2]/div[3]/span/input'
if check_exists_by_xpath(xpath):
   jobcard=driver.find_element_by_xpath(xpath)
   jobcard.send_keys(cvc)
   print('add cvc')
else:
   delete_user(id=user_id,token=user_token)
   print('COULD NOT FIND THE DESIRED XPATH')
   print('user deleted')
   driver.quit()
###########################
# finish add card
###########################

xpath = '/html/body/div[2]/div/div[2]/div/div[2]/app-payment-method-forms/div/div/div[2]/div/button'
if check_exists_by_xpath(xpath):
   jobcard=driver.find_element_by_xpath(xpath)
   jobcard.click()
   print('click save')
   time.sleep(3)
   delete_user(id=user_id,token=user_token)
   print('user deleted')
   driver.quit()
else:
   delete_user(id=user_id,token=user_token)
   print('COULD NOT FIND THE DESIRED XPATH')
   print('user deleted')
   driver.quit()
#   num_job_card = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/app-create-team-pitchcard/div/div[1]/div[2]/div[1]/p-inputnumber/span/input')
#   num_job_card.clear()
#   num_job_card.send_keys('1')

#   create_job_card = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/app-create-team-pitchcard/div/div[2]/button')
##   create_job_card.click()
 #  print('create 1 Job Card')
   
   #-----------------------------------------------------------------------------------------------------
#profi = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[4]/div')
#profi.click()
#time.sleep(2)

#logOut = driver.find_element_by_xpath('/html/body/app-root/p-sidebar/div')
#logOut.click()
#print('click profile and log out')

#time.sleep(2)
#driver.back()

# time.sleep(5)
#print("test end")





