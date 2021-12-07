from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys
import getopt
from selenium.webdriver.common.action_chains import ActionChains
from p59_job_utils import *


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
        #driver = webdriver.Chrome(options=options)
        driver = webdriver.Chrome(executable_path=r"C:/Users/user1/Documents/School/00TA/chromedriver.exe")
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

# click to create pitchcard
time.sleep(5)
createPitchCard = driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-welcome-page/section[1]/div/div/div[1]/div[3]/div')
createPitchCard.click()
print('click create pitchcard')
time.sleep(2)

business = driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-choose-pitchcard-page/div/div/app-choose-pitchcard/div/div/div[2]/div[4]/div[3]/button')
business.click()
print('select business pitchcard')
time.sleep(2)

free = driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-billing-page/div/div/div/div/div[2]/app-visual-video/div/div[1]/div[2]/div[1]/div/div[2]')
time.sleep(5)
free.click()
print('select free')
time.sleep(2)

billing = driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-billing-page/div/div/div/div/div[2]/app-billing-summary/div/div/div[2]/div[1]/div')
billing.click()
print('click add billing info')
time.sleep(2)

driver.find_element(By.XPATH,
    '//*[@id="cardNumber"]/input').send_keys('4022400001871076')
driver.find_element(By.XPATH,'//*[@id="month"]/span/input').send_keys('12')
driver.find_element(By.XPATH,'//*[@id="year"]/span/input').send_keys('2021')
driver.find_element(By.XPATH,'//*[@id="cvc"]').send_keys('737')
print('insert card information')
time.sleep(5)

driver.find_element(By.XPATH,
    '/html/body/div/div/div[2]/div/div[2]/app-payment-method-forms/div/div/div[2]/div/button').click()
time.sleep(2)

driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-billing-page/div/div/div/div/div[2]/app-billing-summary/div/div/div[2]/div[4]/button').click()
time.sleep(3)
driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-layout/p-dialog[2]/div/div/div[2]/div/button').click()
time.sleep(3)
driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-layout/div[2]/div/div/div/div[3]/div/div[2]/div').click()
time.sleep(3)

# -------------------  Information page  ----------------------
fullName = driver.find_element(By.XPATH,'//*[@id="businessName"]')
fullName.send_keys('Test')

title = driver.find_element(By.XPATH,'//*[@id="title"]')
title.send_keys("Web Developer")

emailInfor = driver.find_element(By.XPATH,'//*[@id="email"]')
emailInfor.send_keys('p59testa@gmail.com')

phoneNumber = driver.find_element(By.XPATH,'//*[@id="contactNumber"]/input')
phoneNumber.send_keys('9999999999')

website = driver.find_element(By.XPATH,'//*[@id="websiteLink"]')
website.send_keys('https://www.linkedin.com/in/jim-tang-19873513b/')

addressInfor = driver.find_element(By.XPATH,'//*[@id="address"]')
addressInfor.send_keys('235W 2nd S')

cityInfor = driver.find_element(By.XPATH,'//*[@id="city"]/span/input')
cityInfor.send_keys('rexburg')

stateInfor = driver.find_element(By.XPATH,'//*[@id="state"]/span/input')
stateInfor.send_keys('ID')

zipInfor = driver.find_element(By.XPATH,'//*[@id="zip"]')
zipInfor.send_keys('83440')

saveAbdNext = driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-layout/div[2]/div/div/div[1]/div[3]/div/div[2]/div')
saveAbdNext.click()
time.sleep(2)
print('finish information page')

# ----------------- Link page -----------------------------


driver.find_element(By.XPATH,
    '//*[@id="main-form"]/div/app-more-info/div/form/div[1]/span/p-autocomplete/span/ul/li/input').send_keys('web')
time.sleep(3)

act = ActionChains(driver)
act.send_keys(Keys.DOWN).perform()
time.sleep(3)

act.send_keys(Keys.RETURN).perform()
time.sleep(2)

facebookLink = driver.find_element(By.XPATH,'//*[@id="facebookLink"]')
facebookLink.send_keys('11111')

twitterLink = driver.find_element(By.XPATH,'//*[@id="twitterLink"]')
twitterLink.send_keys('11111')

instagramLink = driver.find_element(By.XPATH,'//*[@id="instagramLink"]')
instagramLink.send_keys('11111')

linkedInLink = driver.find_element(By.XPATH,'//*[@id="linkedinLink"]')
linkedInLink.send_keys('11111')

pinterestLink = driver.find_element(By.XPATH,'//*[@id="linkedinLink"]')
pinterestLink.send_keys('11111')

yourInfo = driver.find_element(By.XPATH,'//*[@id="description"]')
yourInfo.send_keys('testing')

saveAbdNext = driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-layout/div[2]/div/div/div[1]/div[3]/div/div[2]/div')
saveAbdNext.click()
time.sleep(2)
print('finish link page')

# --------------------map ---------------------
location = driver.find_element(By.XPATH,'//*[@id="address"]')
location.send_keys('rexburg')
time.sleep(3)
act.send_keys(Keys.DOWN).perform()
time.sleep(3)

act.send_keys(Keys.RETURN).perform()
time.sleep(2)

saveAbdNext = driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-layout/div[2]/div/div/div[1]/div[3]/div/div[2]/div')
saveAbdNext.click()
time.sleep(2)
print('finish Radius page')

# ----------------- upload image page -----------------
time.sleep(2)


driver.find_element(By.XPATH,
    '//*[@id="main-form"]/div/app-images/div/div[1]/div[1]/button/app-image-uploader/input').send_keys('.\logo.png')
time.sleep(4)

driver.find_element(By.XPATH,
    '/html/body/div[4]/div/div[3]/p-footer/div').click()
time.sleep(4)
print('upload cover image')

driver.find_element(By.XPATH,
    '//*[@id="main-form"]/div/app-images/div/div[1]/div[3]/button/app-image-uploader/input').send_keys('./logo.png')
time.sleep(4)

driver.find_element(By.XPATH,
    '/html/body/div[4]/div/div[3]/p-footer/div').click()
time.sleep(2)
print('upload business logo')

driver.find_element(By.XPATH,
    '//*[@id="main-form"]/div/app-images/div/div[2]/div[1]/button/input').send_keys('BYUI.png')
time.sleep(5)

saveAbdNext = driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-layout/div[2]/div/div/div[1]/div[3]/div/div[2]/div')
saveAbdNext.click()
time.sleep(5)

#  ----------------- up load video page -------------------

driver.find_element(By.XPATH,
    '//*[@id="main-form"]/div/app-pitch-video/div/div/p-fileupload/span/input').send_keys('test.mp4')
time.sleep(10)

driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-layout/div[2]/div/div/div/div[3]/div/div[1]/div').click()
time.sleep(2)
driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-layout/div[2]/div/div/div/div[3]/div/div[2]/div').click()
time.sleep(2)
driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-layout/div[2]/div/div/div/div[3]/div/div[2]').click()
time.sleep(2)
driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-layout/p-dialog[1]/div/div/div[1]/div/a/span').click()

profi = driver.find_element(By.XPATH,
    '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[4]/div')
profi.click()
time.sleep(2)
driver.find_element(By.XPATH,
    '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/p-overlaypanel[2]/div/div/div/ul/li[1]/a/span').click()
time.sleep(5)

print('test end')
driver.quit()
