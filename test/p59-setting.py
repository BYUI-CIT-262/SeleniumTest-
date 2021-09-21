from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys, getopt


# def main(argv):
#    try:
#       opts, args = getopt.getopt(argv,"h")
#    except getopt.GetoptError:
#       print ('err')
#       sys.exit(2)
      
#    driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME, options=options)
#    for opt, arg in opts:
#       if opt in ['-h']:
#          return driver

#    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
#    return driver

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


test1 = 'test'
test2 = 'testtest'
emailAddress1 = "1111@gmail.com"
emailAddress2 = "2222@gmail.com"
phone1 = '(999) 999-7485'
phone2 = '(999) 999-7482'
zip1 = '83440'
zip2 = '93440'

print('test start')
link = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[3]')
link.click()

email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys(emailAddress1)

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('Love1111')

logIn = driver.find_element_by_xpath('/html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button')
logIn.click()
time.sleep(2)
print('log in')

profi = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[4]/div')
profi.click()
time.sleep(2)

setting = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/p-overlaypanel[2]/div/div/div/div[1]/div/a/div')
setting.click()
time.sleep(2)
print('on setting page')

firstNameClean = driver.find_element_by_xpath('//*[@id="firstName"]').clear()
firstName = driver.find_element_by_xpath('//*[@id="firstName"]')
firstName.send_keys(test2)
time.sleep(2)
print('Change first name')

lastNameClean = driver.find_element_by_xpath('//*[@id="lastName"]').clear()
lastName = driver.find_element_by_xpath('//*[@id="lastName"]')
lastName.send_keys(test2)
time.sleep(2)
print('Change last name')


emailClean = driver.find_element_by_xpath('//*[@id="emailId"]').clear()
email = driver.find_element_by_xpath('//*[@id="emailId"]')
email.send_keys(emailAddress2)
time.sleep(2)
print('Change Email')


phoneClean = driver.find_element_by_xpath('//*[@id="contactNumber"]/input').clear()
phone = driver.find_element_by_xpath('//*[@id="contactNumber"]/input')
phone.send_keys(phone2)
time.sleep(2)
print('Change phone')


zipCodeClean = driver.find_element_by_xpath('//*[@id="zipCode"]').clear()
zipCode = driver.find_element_by_xpath('//*[@id="zipCode"]')
zipCode.send_keys(zip2)
time.sleep(2)
print('Change Zip Code')

UpdateClick = driver.find_element_by_xpath('/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-settings/div/div/div[1]/div[1]')
UpdateClick.click()
time.sleep(3)
print('Enter verify number')
first = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[1]')
first.send_keys('1')

second = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[2]')
second.send_keys('1')

third = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[3]')
third.send_keys('1')

fourth = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[4]')
fourth.send_keys('1')

verifyClick = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[2]/button')
verifyClick.click()
time.sleep(3)


print('End first profile update')

account = driver.find_element_by_xpath('//*[@id="email"]')

account.send_keys(emailAddress2)

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('Love1111')

logIn = driver.find_element_by_xpath('/html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button')
logIn.click()
time.sleep(2)
print('Second time log in')

profi = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[4]/div')
profi.click()
time.sleep(2)

setting = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/p-overlaypanel[2]/div/div/div/div[1]/div/a/div')
setting.click()
time.sleep(2)
print('on setting page - 2')

firstNameClean = driver.find_element_by_xpath('//*[@id="firstName"]').clear()
firstName = driver.find_element_by_xpath('//*[@id="firstName"]')
firstName.send_keys(test1)
time.sleep(2)
print('Change first name - 2')

lastNameClean = driver.find_element_by_xpath('//*[@id="lastName"]').clear()
lastName = driver.find_element_by_xpath('//*[@id="lastName"]')
lastName.send_keys(test1)
time.sleep(2)
print('Change last name - 2')

emailClean = driver.find_element_by_xpath('//*[@id="emailId"]').clear()
email = driver.find_element_by_xpath('//*[@id="emailId"]')
email.send_keys(emailAddress1)
time.sleep(2)
print('Change Email - 2')

phoneClean = driver.find_element_by_xpath('//*[@id="contactNumber"]/input').clear()
phone = driver.find_element_by_xpath('//*[@id="contactNumber"]/input')
phone.send_keys(phone1)
time.sleep(2)
print('Change phone - 2')

zipCodeClean = driver.find_element_by_xpath('//*[@id="zipCode"]').clear()
zipCode = driver.find_element_by_xpath('//*[@id="zipCode"]')
zipCode.send_keys(zip1)
time.sleep(2)
print('Change Zip Code - 2')

UpdateClick = driver.find_element_by_xpath('/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-settings/div/div/div[1]/div[1]')
UpdateClick.click()
time.sleep(3)
print('Enter verify number - 2')


first = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[1]')
first.send_keys('1')

second = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[2]')
second.send_keys('1')

third = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[3]')
third.send_keys('1')

fourth = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[4]')
fourth.send_keys('1')

verifyClick = driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[2]/button')
verifyClick.click()
time.sleep(3)
print('End second profile update')

print('test end')
driver.close()
driver.quit()
