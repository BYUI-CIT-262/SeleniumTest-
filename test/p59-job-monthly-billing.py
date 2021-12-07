#
# Selects the monthly billing option on Choose PitchCard Type
#

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import sys
import getopt
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
        driver = webdriver.Chrome(
            executable_path="chromedriver", options=options)
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
createPitchCard(driver)

# Get the current billing info
billingInfo = driver.find_element(By.XPATH,
    '/html/body/app-root/main/app-choose-pitchcard-page/div/div/app-choose-pitchcard/div/div/div[1]/div/div/div/p-inputswitch/div/div/input'
)

# If it is Annual Billing (aria-checked == "true"), set it to Monthly billing ("false")
billingChoice = billingInfo.get_attribute("aria-checked")
if billingChoice == "true":
    driver.find_element(By.XPATH,
        '/html/body/app-root/main/app-choose-pitchcard-page/div/div/app-choose-pitchcard/div/div/div[1]/div/div/div/p-inputswitch/div/span'
    ).click()

    time.sleep(2)

    # Verify that the billing choice is set to Monthly Billing ("false")
    billingChoice = billingInfo.get_attribute("aria-checked")
    if billingChoice == "false":
        print('Billing choice is set to Monthly.')

        # Change back to Annual billing
        driver.find_element(By.XPATH,
            '/html/body/app-root/main/app-choose-pitchcard-page/div/div/app-choose-pitchcard/div/div/div[1]/div/div/div/p-inputswitch/div/span'
        ).click()
        time.sleep(2)
    else:
        print("ERROR: Billing choice didn't get set to Monthly.")


else:
    print('Billing choice was set to Monthly Already. No change.' + billingChoice)


logout(driver)
driver.back()

print("test end")
driver.quit()
