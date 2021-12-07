from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys
import getopt
from selenium.webdriver.common.action_chains import ActionChains


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
link = driver.find_element(By.XPATH,
    '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[3]')
link.click()

email = driver.find_element(By.XPATH,'//*[@id="email"]')
email.send_keys('pitch59testa+1@gmail.com')

password = driver.find_element(By.XPATH,'//*[@id="password"]')
password.send_keys('Love1111')

logIn = driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button')
logIn.click()
time.sleep(2)
print('Log in')

createPitchCard = driver.find_element(By.XPATH,
    '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/div[2]')
createPitchCard.click()
time.sleep(2)

resume = driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-choose-pitchcard-page/div/div/app-choose-pitchcard/div/div/div[2]/div[2]/div[3]/button')
resume.click()
time.sleep(5)

# --------Information page ------------
time.sleep(3)
fullName = driver.find_element(By.XPATH,'//*[@id="businessName"]')
fullName.send_keys('Test')

emailInfor = driver.find_element(By.XPATH,'//*[@id="email"]')
emailInfor.send_keys('p59testa@gmail.com')

phoneNumber = driver.find_element(By.XPATH,'//*[@id="contactNumber"]/input')
phoneNumber.send_keys('9999999876')

addressInfor = driver.find_element(By.XPATH,'//*[@id="address"]')
addressInfor.send_keys('330E 1nd S')

cityInfor = driver.find_element(By.XPATH,'//*[@id="city"]/span/input')
cityInfor.send_keys('rexburg')

stateInfor = driver.find_element(By.XPATH,'//*[@id="state"]/span/input')
stateInfor.send_keys('ID')

zipInfor = driver.find_element(By.XPATH,'//*[@id="zip"]')
zipInfor.send_keys('83440')
time.sleep(2)

saveAbdNext = driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-layout/div[2]/div/div/div[1]/div[3]/div/div[2]/div')
saveAbdNext.click()
time.sleep(2)
print('finish information page')

# -------------- link page -------------------
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
yourInfo.send_keys('//*[@id="description"]')

saveAbdNext = driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-layout/div[2]/div/div/div[1]/div[3]/div/div[2]/div')
saveAbdNext.click()
time.sleep(2)
print('finish link page')


# ------------------Radius page --------------------
location = driver.find_element(By.XPATH,'//*[@id="address"]')
location.send_keys('rexburg')
time.sleep(2)
act = ActionChains(driver)
act.send_keys(Keys.DOWN).perform()
time.sleep(2)

act.send_keys(Keys.RETURN).perform()
time.sleep(2)

saveAbdNext = driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-layout/div[2]/div/div/div[1]/div[3]/div/div[2]/div')
saveAbdNext.click()
time.sleep(2)
print('finish Radius page')

# ----------------- position page -----------------------
# position = driver.find_element(By.XPATH,'//*[@id="main-form"]/div/app-employment/form/div/span[1]/p-autocomplete/span/ul/li/input')
# position.send_keys('software')
# # act.send_keys(Keys.DOWN).perform()
# time.sleep(2)
# act.send_keys(Keys.RETURN).perform()
# time.sleep(2)

# driver.find_element(By.XPATH,'//*[@id="main-form"]/div/app-employment/form/div/div[1]/div[1]/p-multiselect/div').click()
# driver.find_element(By.XPATH,'//*[@id="main-form"]/div/app-employment/form/div/div[1]/div[1]/p-multiselect/div/div[4]/div/ul/p-multiselectitem[1]/li').click()

# driver.find_element(By.XPATH,'//*[@id="main-form"]/div/app-employment/form/div/div[1]/div[2]/p-dropdown/div').click()
# driver.find_element(By.XPATH,'//*[@id="main-form"]/div/app-employment/form/div/div[1]/div[2]/p-dropdown/div/div[4]/div/ul/p-dropdownitem[7]/li').click()

# driver.find_element(By.XPATH,'//*[@id="main-form"]/div/app-employment/form/div/span[2]/p-autocomplete/span/ul/li/input').send_keys('BYUI')
time.sleep(2)

act.send_keys(Keys.RETURN).perform()
time.sleep(2)

saveAbdNext = driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-layout/div[2]/div/div/div[1]/div[3]/div/div[2]/div')
saveAbdNext.click()
time.sleep(2)
print('finished Employment page')


# -------------------- image update page -------------------
time.sleep(2)

driver.find_element(By.XPATH,
    '//*[@id="main-form"]/div/app-images/div/div[1]/div[1]/button/app-image-uploader/input').send_keys('../images/BYUI.png')
time.sleep(3)

driver.find_element(By.XPATH,
    '/html/body/div[4]/div/div[3]/p-footer/div').click()
time.sleep(3)
print('upload cover image')

driver.find_element(By.XPATH,
    '//*[@id="main-form"]/div/app-images/div/div[1]/div[3]/button/input').send_keys('WeiChunTang resume.pdf')
time.sleep(3)
print('upload resume')

driver.find_element(By.XPATH,
    '//*[@id="main-form"]/div/app-images/div/div[2]/div[1]/button/input').send_keys('BYUI.png')
time.sleep(3)

saveAbdNext = driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-layout/div[2]/div/div/div[1]/div[3]/div/div[2]/div')
saveAbdNext.click()
time.sleep(3)

# --------------------- video update  -------------------------

driver.find_element(By.XPATH,
    '//*[@id="main-form"]/div/app-pitch-video/div/div/p-fileupload/span/input').send_keys('test.mp4')
time.sleep(10)
# C:/Users/after/OneDrive/桌面/selenium/images/test.mp4

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
