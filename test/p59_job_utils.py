#
# Routines common to testing job cards
# (Actions unique to a specific test scenario should be kept in its test script)
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
import time
import sys, getopt

# 
# Login as p59testa+1@gmail.com / Love1111
#
def login(driver):

   #test account = p59testa+5@gmail.com   pwd Love1111

   link = driver.find_element_by_xpath(
    '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[3]'
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
   createCard = driver.find_element_by_xpath(
      '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[2]/div[1]'
   )
   createCard.click()
   time.sleep(2)
   print('click create pitch card')

#
# Click on the "SELECT" button under "Job" in "Choose a PitchCard Type" window
#
def selectJob(driver):
   cardSelection = driver.find_element_by_xpath( 
      '/html/body/app-root/main/app-choose-pitchcard-page/div/div/app-choose-pitchcard/div/div/div[2]/div[5]/div[3]/button'
   )
   cardSelection.click()
   time.sleep(2)
   print('click select on job')

#
# Click on the "ADDPITCHCARDS" button in "How many Job PitchCards would you like 
# to create now?" window.  Select the number of cards specified.
#
def numOfJobCardsToCreate(driver, num_job_cards):
   
   #numCards = Select(driver.find_element_by_xpath(
   #   '/html/body/div[1]/div/div[2]/div/app-create-team-pitchcard/div/div[1]/div[2]/div[1]/p-inputnumber/span/input'
   #   '/html/body/div[2]/div/div[2]/div/app-create-team-pitchcard/div/div[1]/div[2]/div[1]/p-inputnumber/span'
   #))

   numCards = driver.find_element_by_xpath(
      '/html/body/div[3]/div/div[2]/div/app-create-team-pitchcard/div/div[1]/div[2]/div[1]/p-inputnumber/span/input'
   )
   #numCards = Select(driver.find_element_by_class_name(
   #   '/html/body/div[3]/div/div[2]/div/app-create-team-pitchcard/div/div[1]/div[2]/div[1]/p-inputnumber/span/input'
   #   '/html/body/div[3]/div/div[2]/div/app-create-team-pitchcard/div/div[1]/div[2]/div[1]/p-inputnumber/span'
   #   'input.ui-inputnumber-input.ui-inputtext.ui-corner-all.ui-state-default.ui-widget.ui-state-filled'
   #))
   #numCards.select_by_value(num_job_cards)
   print(numCards.get_attribute('value'))
   numCards.clear()
   numCards.send_keys(num_job_cards)
   print ('The number of cards to create is set to ' + repr(num_job_cards))
   time.sleep(2)
  
   addPitchCards = driver.find_element_by_xpath(
      '/html/body/div[1]/div/div[2]/div/app-create-team-pitchcard/div/div[2]/button'
   )
   #addPitchCards.click()
   time.sleep(2)
   print('click add pitchcards')

#
# Click on the profile icon at the right-top cornor of the screen which brings down a menu for
# selecting the "Employer Protal" among other things (My PtichCards, Pockets, Logout, etc.)
#
def profile(driver):
   profile = driver.find_element_by_xpath(
      '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[4]/img'
   )
   profile.click()
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



