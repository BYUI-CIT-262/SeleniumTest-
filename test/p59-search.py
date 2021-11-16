# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import time
# import sys, getopt
# from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as DC
import sys, getopt
import time


# def main(argv):
#    try:
#       opts, args = getopt.getopt(argv,"h")
#    except getopt.GetoptError:
#       print ('err')
#       sys.exit(2)
      
#    headless = False
#    for opt, arg in opts:
#       if opt in ['-h']:
#          headless = True


#    if headless:
#       driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME, options=options) 
#    else:
#       driver = webdriver.Chrome(executable_path="chromedriver", options=options)
#    return driver

# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"
# options = webdriver.ChromeOptions()
# options.headless = False
# options.add_argument(f'user-agent={user_agent}')
# options.add_argument('--disable-gpu')
# options.add_argument('--disable-dev-shm-usage')
# options.add_argument('--no-sandbox')

# driver = main(sys.argv[1:])

def main(argv):
   driver = setup_chromedriver(argv)

   driver.get("https://public.p59.dev/welcome")
   print("Action: Open browser to pitch59")

   go_to_search(driver)
   clear_search_bar(driver)

   search_test_1(driver)
   time.sleep(2)
   clear_search_bar(driver)

   search_test_2(driver)
   time.sleep(2)
   clear_search_bar(driver)

   search_test_3(driver)
   time.sleep(2)

   print("Success: Search test finished")



def setup_chromedriver(argv):
    try:
        opts, args = getopt.getopt(argv, "h")
    except getopt.GetoptError:
        print('err')
        sys.exit(2)

    headless = False
    for opt, arg in opts:
        if opt in ['h']:
            headless = True

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.35 (X11; Linux x86_64) Safari/537.36"
    options = webdriver.ChromeOptions()
    options.headless = False
    # options.add_argument(f'user-agent={user_agent}')
    options.add_argument("start-maximized")
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    # options.add_argument('incognito')

    if headless:
        driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DC.CHROME, options=options) 
    else:
        driver = webdriver.Chrome(executable_path="chromedriver", options=options)

    print("Success: Chromedriver has been setup\n")
    return driver


def go_to_search(driver):
   search_link = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "search-icon")]')))
   search_link.click()
   print("Action: Click search link")

   
def clear_search_bar(driver):
   clear_search = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[contains(@class, "ui-inputtext")]')))
   # For Windows
   clear_search.send_keys(Keys.CONTROL + "a")
   clear_search.send_keys(Keys.BACK_SPACE)
   # For MacOS
   clear_search.send_keys(Keys.COMMAND + "a")
   clear_search.send_keys(Keys.BACK_SPACE)
   print("Action: Reset search input")


def search_test_1(driver):
   search_bar = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[contains(@class, "ui-inputtext")]')))
   search_bar.send_keys('software developer')
   search_bar.send_keys(Keys.RETURN)
   print("Action: Search 'software developer' -- 1st time")

   time.sleep(1)
   search_bar.send_keys(Keys.RETURN)
   print("Action: Search 'software developer' -- 2nd time")

   time.sleep(1)
   search_bar.send_keys(Keys.RETURN)
   print("Action: Search 'software developer' -- 3rd time")

   print("Success: Test 1 has been completed\n")


def search_test_2(driver):
   jobs_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "search-tab") and contains(text(), "Jobs")]')))
   jobs_button.click()
   print("Action: Click Jobs")

   search_bar = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[contains(@class, "ui-inputtext")]')))
   search_bar.send_keys('pitch59')
   search_bar.send_keys(Keys.RETURN)
   print("Action: Search 'pitch59'")

   print("Success: Test 2 has been completed\n")


def search_test_3(driver):
   resume_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "search-tab") and contains(text(), "Resumés")]')))
   resume_button.click()
   print("Action: Click Resumes")

   search_bar = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[contains(@class, "ui-inputtext")]')))
   search_bar.send_keys('ryan')
   search_bar.send_keys(Keys.RETURN)
   print("Action: Search 'ryan'")

   print("Success: Test 3 has been completed\n")

# print('test start')
# searchBtn = driver.find_element_by_xpath('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[1]')
# searchBtn.click()
# print('Click search btn')
# time.sleep(3)

# searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[2]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
# time.sleep(3)
# print('Clean search bar')



# searchBar = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[2]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input')
# searchBar.send_keys('software developer')
# time.sleep(2)
# print('type software developer')

# act = ActionChains(driver)
# act.send_keys(Keys.RETURN).perform()
# time.sleep(2)


# searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[2]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
# searchBar.send_keys('Software developer')
# time.sleep(2)
# print('type Software developer')
# act.send_keys(Keys.RETURN).perform()
# time.sleep(2)

# searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[2]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
# searchBar.send_keys('Software Developer')
# time.sleep(2)
# print('type Software Developer')
# act.send_keys(Keys.RETURN).perform()
# time.sleep(2)

# searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[2]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
# time.sleep(2)

# # go to job card section
# driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/app-search-tabs/div/div[2]/div').click()
# searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[2]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
# searchBar.send_keys('pitch59')
# time.sleep(2)
# print('search pitch59')
# act.send_keys(Keys.RETURN).perform()
# time.sleep(2)

# #go to resume section
# driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[1]/app-search-tabs/div/div[3]/div').click()
# searchBarClean = driver.find_element_by_xpath('/html/body/app-root/main/app-search-result-page/div/app-search-result/div/div[2]/div/div/div/div/div/div[1]/div/p-autocomplete/span/input').clear()
# searchBar.send_keys('ryan')
# time.sleep(2)
# print('search ryan')
# act.send_keys(Keys.RETURN).perform()
# time.sleep(5)

# print('End test')
# driver.quit()

main(sys.argv[1:])