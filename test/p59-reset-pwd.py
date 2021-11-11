from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
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
        driver = webdriver.Chrome(
            executable_path="chromedriver.exe", options=options)
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
# new test account = p59testa@gmail.com   pwd Love1111

pwd1 = 'Love1111'
pwd = 'Love1111'

print('test start')
link = driver.find_element_by_xpath(
    '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[3]')
link.click()

email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('pitch59testa+1@gmail.com')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(pwd)

logIn = driver.find_element_by_xpath(
    '/html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button')
logIn.click()
time.sleep(2)
print('log in')

profi = driver.find_element_by_xpath(
    '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[4]/div')
profi.click()
time.sleep(2)

setting = driver.find_element_by_xpath(
    '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/p-overlaypanel[2]/div/div/div/div[1]/div/a/div')
setting.click()
time.sleep(2)

chagePwd = driver.find_element_by_xpath(
    '/html/body/app-root/main/app-history-favorites-layout/div/div/div/div/div/div[2]/app-account-settings/div/div/div[1]/div[2]')
chagePwd.click()
time.sleep(2)
print('Click Change password')

currentPwd = driver.find_element_by_xpath('//*[@id="oldpassword"]')
currentPwd.send_keys(pwd)

newPwd = driver.find_element_by_xpath('//*[@id="password"]')
newPwd.send_keys(pwd1)

confirmPwd = driver.find_element_by_xpath('//*[@id="confirmpassword"]')
confirmPwd.send_keys(pwd1)

change = driver.find_element_by_xpath(
    '/html/body/app-root/main/app-change-password/div/div/div/div/div[2]/div/form/button')
change.click()
time.sleep(2)
print('Change password successfully')

email = driver.find_element_by_xpath('//*[@id="email"]')
email.send_keys('pitch59testa+1@gmail.com')

password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(pwd1)

logIn = driver.find_element_by_xpath(
    '/html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button')
logIn.click()
time.sleep(2)
print('log in again')

print('test end')
driver.quit()
