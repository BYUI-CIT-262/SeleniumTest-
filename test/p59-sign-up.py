from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys
import getopt


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

# old account = 1111@gmail.com   pwd = Love1111
# new test account = p59testa+1@gmail.com   pwd Love1111


link = driver.find_element_by_xpath(
    '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[2]')
link.click()

user_payload = {
   'firstName': 'UserFirstNameTest',
   'lastName': 'UserLastNameTest',
   'emailId': 'useremailtestp59@gmail.com',
   'contactNumber': '9999999485',
   'zipCode': 'Love@1111',
   'password': 'Love@1111'
}

firstName = WebDriverWait(driver, 2).until(EC.element_to_be_clickable(
    (By.ID, 'firstName')))
firstName.send_keys(user_payload['firstName'])

lastName = driver.find_element_by_xpath('//*[@id="lastName"]')
lastName.send_keys(user_payload['lastName'])

email = driver.find_element_by_xpath('//*[@id="emailId"]')
email.send_keys(user_payload['emailId'])

number = driver.find_element_by_xpath('//*[@id="contactNumber"]/input')
number.send_keys(user_payload['contactNumber'])

zipCode = driver.find_element_by_xpath('//*[@id="zipCode"]')
zipCode.send_keys(user_payload['zipCode'])

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(user_payload['password'])

cPassword = driver.find_element_by_xpath('//*[@id="repassword"]')
cPassword.send_keys(user_payload['password'])

signUp = driver.find_element_by_xpath(
    '/html/body/app-root/main/app-new-sign-up/div/div/div/div[2]/div/form/div[9]/button')
signUp.click()

time.sleep(5)

firstV = driver.find_element_by_xpath(
    '/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[1]')
firstV.send_keys('1')

secondV = driver.find_element_by_xpath(
    '/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[2]')
secondV.send_keys('1')

thirdV = driver.find_element_by_xpath(
    '/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[3]')
thirdV.send_keys('1')

fourth = driver.find_element_by_xpath(
    '/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[1]/input[4]')
fourth.send_keys('1')

button = driver.find_element_by_xpath(
    '/html/body/div/div/div[2]/div/div[2]/div/app-verify-input/div/div[2]/button')
button.click()

# emailR = driver.find_element_by_xpath('//*[@id="refemailId"]')
# emailR.send_keys('1111')
print('created successfully')
time.sleep(5)
driver.quit()
