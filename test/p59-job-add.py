#
# Adds an empty job card to the employer portal
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys, getopt
from p59_job_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
# test test test 
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
      driver = webdriver.Chrome("chromedriver", options=options)
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

# first, count the number of job cards on hand by going to the employee portal
profile(driver)
employeePortal(driver)
# myPitchCards(driver)

time.sleep(3)

# get all the rows in the employer portal table (assume only one table exists on the page)
jobTable = driver.find_elements_by_tag_name('tr')

# count the number of rows; -1 is needed to account for the header row
num_rows = len(jobTable) - 1
print('The original number of job cards:', num_rows)

#for row in jobTable:
#    print(row.text)
#    print(row.get_attribute('id'))

# create a new job pitch card
createPitchCard(driver)
#selectJob(driver)


# Click on the "ADDPITCHCARDS" button in "How many Job PitchCards would you like 
# to create now?" window. 
#time.sleep(5)
#numCards = driver.find_element_by_xpath(
#   '/html/body/div[1]/div/div[2]/div/app-create-team-pitchcard/div/div[1]/div[2]/div[1]/p-inputnumber/span/input'
#)

# some debug info
#print('element', numCards)
#print('type', numCards.get_attribute("type"))
#print('id', numCards.get_attribute("id"))
#print('aria-valuenow', numCards.get_attribute("aria-valuenow"))
#print('aria-valumin', numCards.get_attribute("aria-valumin"))
#print('aria-valuemax', numCards.get_attribute("aria-valuemax"))
   
# clear the number of job cards to create.  This will reset to 1.
#numCards.clear()
   
# click the add pitchcards button
#addPitchCards = driver.find_element_by_xpath(
#   '/html/body/div[1]/div/div[2]/div/app-create-team-pitchcard/div/div[2]/button'
#)
#addPitchCards.click()
#time.sleep(2)
#print('click add pitchcards')

#selects the job option when prompted with what pitch card to create
selectJob(driver)
time.sleep(2)
selectNumOfJobs(driver)
time.sleep(2)
clickAddPitchCards(driver)
time.sleep(2)
clickTestaX(driver)
time.sleep(2)
clickCreatedOrder(driver)
time.sleep(4)
editJobCard(driver)
fillInInfo(driver)



# now, count the number of jopb cards.  It should be one greater.
# get all the rows in the table (assume only one table exists on the page)
#jobTableNew = driver.find_elements_by_tag_name('tr')
# count the number of rows; -1 is needed to account for the header row
#num_rows_new = len(jobTableNew) - 1
#print('The number of job cards after additon(s):', num_rows_new)

#if num_rows_new != (num_rows + 1):
#   print('test failed.  table row did not inclement by one after adding a job card')
#else:
#   print('success')


time.sleep(3)
driver.find_element_by_css_selector('body > app-root > main > app-history-favorites-layout > div > div > div > div > div > div.p-col-12.p-md-8.p-lg-9.container-layout > app-account-employer-portal > div.ng-star-inserted > div > div > div.ep-body.ng-star-inserted > app-employer-portal-table > div > p-table > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2) > span').click()

#firstLink = driver.find_element_by_class_name("ng-star-inserted")
#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, firstLink[0]))).click()









logout(driver)

driver.back()
#time.sleep(5)
print("test end")
driver.quit()

