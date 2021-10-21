#
# Routines common to testing job cards
# (Actions unique to a specific test scenario should be kept in its test script)
#
#   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ''))).click()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
import time
import sys, getopt
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains









# 
# Login as p59testa+1@gmail.com / Love1111
#
def login(driver):
   #test account = p59testa+5@gmail.com   pwd Love1111
   link = driver.find_element_by_xpath(
    '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[4]'
    )
   link.click()
   print('click login')

   time.sleep(5)
   email = driver.find_element_by_xpath('//*[@id="email"]')
   email.send_keys('pitch59testa+5@gmail.com')

   password = driver.find_element_by_xpath('//*[@id="password"]')
   password.send_keys('Love1111')

   logIn = driver.find_element_by_xpath(
    '/html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button'
   )
   logIn.click()
   time.sleep(2)
   print('login complete')

#makes sure the number of job cards being created it 1
def selectNumOfJobs(driver):
   driver.find_element_by_css_selector('body > div.ng-tns-c42-63.ui-dialog-mask.ui-widget-overlay.ui-dialog-visible.ui-dialog-mask-scrollblocker.ng-star-inserted > div > div.ng-tns-c42-63.ui-dialog-content.ui-widget-content > div > app-create-team-pitchcard > div > div.p-grid.p-align-start.no-margins > div.p-col-8 > div.mt-20.mb-20 > p-inputnumber > span > input').clear()
  # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By. '/html/body/div[1]/div/div[2]/div/app-create-team-pitchcard/div/div[1]/div[2]/div[1]/p-inputnumber/span/input'))).clear()
  # driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/app-create-team-pitchcard/div/div[1]/div[2]/div[1]/p-inputnumber/span/input').clear()
   print('enters 1 into text for how many job cards you want to create')
#
# Logout
#
def logout(driver):
   profi = driver.find_element_by_xpath(
    '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[4]/div'
   )
   profi.click()
   time.sleep(2)
   print('click profile')

   logOut = driver.find_element_by_xpath(
      '/html/body/app-root/p-sidebar/div[2]/div/div/div[2]/div'
   )
   logOut.click()
   time.sleep(2)
   print('logout complete')

#
# Click on the "CREATE A PITCHCARD" button at the top of the screen after login
#
def createPitchCard(driver):
   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[1]/app-my-profile/div/ul/li[1]/div/div/i'))).click()
   time.sleep(1)
   print('click create pitch card')

#
# Click on the "SELECT" button under "Job" in "Choose a PitchCard Type" window
#
def selectJob(driver):
   #this does not work unless window is maximized. when it's not full screen it will scroll down to the button but you'll get an error when trying to click it. 
   driver.maximize_window()
   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/main/app-choose-pitchcard-page/div/div/app-choose-pitchcard/div[1]/div/div[2]/div[5]/div[3]/button'))).click()
   print('click select on job')


#
# Click on the profile icon at the right-top cornor of the screen which brings down a menu for
# selecting the "Employer Protal" among other things (My PtichCards, Pockets, Logout, etc.)
#
def profile(driver):
   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[3]/img'))).click()
   print('click profile')

#
# Click on the "Employer Portal" option under the profile menu
#
def employeePortal(driver):
   employer_portals = driver.find_element_by_xpath(
     '/html/body/app-root/p-sidebar/div[2]/div/div/ul/li[3]/a/span'

   )
   employer_portals.click()
   print('click employer portal')  


def myPitchCards(driver):
   my_pitchCards = driver.find_element_by_xpath(
      '/html/body/app-root/p-sidebar/div[2]/div/div/ul/li[1]/a/span'
   )
   my_pitchCards.click()
   print('click my pitch cards')

#creates 1 job card
def clickAddPitchCards(driver):
   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > div.ng-tns-c42-63.ui-dialog-mask.ui-widget-overlay.ui-dialog-visible.ui-dialog-mask-scrollblocker.ng-star-inserted > div > div.ng-tns-c42-63.ui-dialog-content.ui-widget-content > div > app-create-team-pitchcard > div > div.p-grid.p-justify-end.p-align-center > button'))).click()
   print('Clicked add pitchcards')

#categorizes pitch cards by lastest first
def clickCreatedOrder(driver):
   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-employer-portal/div[1]/div/div/div[2]/app-employer-portal-table/div/p-table/div/div/table/thead/tr/th[3]/div/span'))).click()
   print('Clicked created to organize')

#clicks on the latest pitch card to edit it
def editJobCard(driver):
   WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-employer-portal/div[1]/div/div/div[2]/app-employer-portal-table/div/p-table/div/div/table/tbody/tr[1]/td[7]/div/div[4]/div/img'))).click()
   print('opened up the edit of the job card screen')

