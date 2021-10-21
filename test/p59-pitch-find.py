from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys, getopt
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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


print('test start')
searchBtn = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[1]')
searchBtn.click()
print('Click search btn')
time.sleep(2)

searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[2]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
time.sleep(2)
print('Clean search bar')



searchBar = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[2]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input')
searchBar.send_keys('Aaron Bitton')
time.sleep(2)
print('type Aaron Bitton')

search = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[2]/div/div/div/div/div/div[2]/span').click()

time.sleep(2)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search-swiper > swiper > div > div.swiper-wrapper > div.swiper-slide.ng-star-inserted.swiper-slide-active > app-search-result-thumbnail > div > div.p-col-12.video-thumbnail.sub-head > span"))).click()
print('play video')
time.sleep(5)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/main/app-search-result-page/div/app-search-result/app-pitchcard-modals-wrapper/p-dialog[1]/div/div/div[1]/div/a/span"))).click()
print('exit video')

searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[2]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
time.sleep(5)



# go to job card section
driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/app-search-tabs/div/div[2]/div').click()
print('click jobs')

searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[2]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
searchBar.send_keys('Pitch59 Inc.')
time.sleep(2)
print('type pitch59 inc.')
search = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[2]/div/div/div/div/div/div[2]/span').click()
time.sleep(2)
print('click search')

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search-swiper > swiper > div > div.swiper-wrapper > div.swiper-slide.ng-star-inserted.swiper-slide-active > app-search-result-thumbnail > div > div.p-col-12.video-thumbnail.sub-head > span"))).click()
print('play video')
time.sleep(5)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > main > app-search-result-page > div > app-search-result > app-pitchcard-modals-wrapper > p-dialog.ng-tns-c42-27 > div > div > div.ui-dialog-titlebar.ui-widget-header.ui-helper-clearfix.ui-corner-top.ng-tns-c42-27.ng-star-inserted > div > a > span"))).click()
print('exit video')

searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[2]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
time.sleep(2)

#go to resume section
driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/app-search-tabs/div/div[3]/div').click()
print('click resumes')

searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[2]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
print('Clean search bar')



searchBar = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[2]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input')
searchBar.send_keys('Ryan Price')
time.sleep(2)
print('type Ryan Price')

search = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[2]/div/div/div/div/div/div[2]/span').click()
print('click search')

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search-swiper > swiper > div > div.swiper-wrapper > div > app-search-result-thumbnail > div > div.p-col-12.video-thumbnail.sub-head > span"))).click()

print('click pitch card')
time.sleep(5)

WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > app-root > main > app-search-result-page > div > app-search-result > app-pitchcard-modals-wrapper > p-dialog.ng-tns-c42-27 > div > div > div.ui-dialog-titlebar.ui-widget-header.ui-helper-clearfix.ui-corner-top.ng-tns-c42-27.ng-star-inserted > div > a > span"))).click()
print('exit video')
time.sleep(2)
print('End test')
driver.quit()