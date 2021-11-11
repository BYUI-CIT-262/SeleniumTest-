from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys
import getopt
from p59_job_utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "h")
    except getopt.GetoptError:
        print('err')
        sys.exit(2)

    headless = False
    for opt, arg in opts:
        if opt in ['-h']:
            headless = True

    if headless:
        driver = webdriver.Remote(
            "http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME, options=options)
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

profile(driver)

employeePortal(driver)

# Clicks on the billing button.
WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                            "#pr_id_9 > div > div > div > div > div.ui-carousel-item.ui-carousel-item-active.ui-carousel-item-start.ng-star-inserted > div"))).click()
print('click billing')
time.sleep(3)


# Clicks on the information button. Will delete information and renter it.
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "#pr_id_9 > div > div > div > div > div:nth-child(2) > div"))).click()
print('click more info')

# delete the business name and reenter "testa"
driver.find_element_by_id("businessName").clear()
time.sleep(1)
driver.find_element_by_id("businessName").send_keys('testa')
print('replace business name')

# delete the your name and reenter "test"
driver.find_element_by_id("title").clear()
time.sleep(1)
driver.find_element_by_id("title").send_keys('test')
print('replace name')

# #delete the email and reenter "pitch59testa+5@gmail.com"
email = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#email")))

# selects and deletes for mac
email.send_keys(Keys.COMMAND + "a")
email.send_keys(Keys.BACK_SPACE)
# selects and deletes for windows
email.send_keys(Keys.CONTROL + "a")
email.send_keys(Keys.BACK_SPACE)
# replaces email
email.send_keys('pitch59testa+5@gmail.com')
print('replace email')

# delete the phone number and reenter "(123) 456-7890"
driver.find_element_by_css_selector("#contactNumber > input").clear()
time.sleep(1)
driver.find_element_by_css_selector(
    "#contactNumber > input").send_keys('(123) 456-7890')
print('replace phone number')


# ---------- enter text into the field and then delete
url = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "websiteLink")))
url.send_keys('Delete me!')
time.sleep(1)
# selects and deletes for mac
url.send_keys(Keys.COMMAND + "a")
url.send_keys(Keys.BACK_SPACE)
# selects and deletes for windows
url.send_keys(Keys.CONTROL + "a")
url.send_keys(Keys.BACK_SPACE)
print('replace url')

# delete the address and reenter "1009 Larch Drive"
address = driver.find_element_by_id("address")
address.clear()
time.sleep(1)
address.send_keys('1009 Larch Drive')
time.sleep(1)
address.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
address.send_keys(Keys.ENTER)
print('replace address')

# delete the city and reenter "Rexburg"
city = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div[1]/div/div[2]/app-ep-layout/div[2]/div/div/div[2]/div/div/app-enter-information/form/div/div[2]/span[3]/p-autocomplete/span/input")))
city.clear()
city.send_keys('Rexburg')
print('replace city')

# #delete the state and reenter "ID"
driver.find_element_by_css_selector("#state > span > input").clear()
driver.find_element_by_css_selector("#state > span > input").send_keys('ID')
print('replace state')

# delete the zip code and reenter "83440"
driver.find_element_by_id("zip").clear()
time.sleep(1)
driver.find_element_by_id("zip").send_keys('83440')
print('replace zip')

# check and uncheck the "Hide your address from customers"
addressCheckOn = driver.find_element_by_xpath(
    '//*[@id="main-form"]/div/div/app-enter-information/form/div/div[2]/p-checkbox/div/div[2]')
addressCheckOn.click()
print('check hide address checkbox')
time.sleep(1)
addressCheckOff = driver.find_element_by_xpath(
    '//*[@id="main-form"]/div/div/app-enter-information/form/div/div[2]/p-checkbox/div/div[2]/span')
addressCheckOff.click()
print('uncheck hide address checkbox')


# Clicks on the more info button.
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pr_id_9 > div > div > div > div > div:nth-child(3) > div > div.icon"))).click()
# print('click on the more info button')


# #########Clicks on the images button
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#pr_id_9 > div > div > div > div > div.ng-star-inserted.ui-carousel-item.ui-carousel-item-active.ui-carousel-item-end > div > div.label"))).click()
# print('click on the images button')


sys.exit()

logout()

driver.back()
# time.sleep(5)
print("test end")
driver.quit()
