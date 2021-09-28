from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys, getopt


def login(driver):

   #test account = p59testa+1@gmail.com   pwd Love1111

   link = driver.find_element_by_xpath(
    '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[3]'
    )
   link.click()
   print('click login')

   time.sleep(5)
   email = driver.find_element_by_xpath('//*[@id="email"]')
   email.send_keys('pitch59testa+1@gmail.com')

   password = driver.find_element_by_xpath('//*[@id="password"]')
   password.send_keys('Love1111')

   logIn = driver.find_element_by_xpath(
    '/html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button'
   )
   logIn.click()
   time.sleep(2)
   print('login complete')

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

def createPitchCard(driver):
   createCard = driver.find_element_by_xpath(
      '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[2]/div[1]'
   )
   createCard.click()
   time.sleep(2)
   print('click create pitch card')

def selectJob(driver):
   cardSelection = driver.find_element_by_xpath( 
      '/html/body/app-root/main/app-choose-pitchcard-page/div/div/app-choose-pitchcard/div/div/div[2]/div[5]/div[3]/button'
   )
   cardSelection.click()
   time.sleep(2)
   print('click select on job')

def numOfJobCardsToCreate(driver):
   # reset the number to 1
   numCards = driver.find_element_by_xpath(
      '/html/body/div[1]/div/div[2]/div/app-create-team-pitchcard/div/div[1]/div[2]/div[1]/p-inputnumber/span/input'
   ).clear()
   time.sleep(2)
   print ('The number of cards to create is reset to 1')

   addPitchCards = driver.find_element_by_xpath(
      '/html/body/div[1]/div/div[2]/div/app-create-team-pitchcard/div/div[2]/button'
   )
   addPitchCards.click()
   time.sleep(2)
   print('click add pitchcards')

def profile(driver):
   profile = driver.find_element_by_xpath(
      '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[4]/img'
   )
   profile.click()
   print('click profile')
