from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as DC
import sys, getopt


def main(argv):
    test_email = 'pitch59testa+1@gmail.com'
    test_password = 'Love1111'
    driver = setup_chromedriver(argv)

    driver.get("https://public.p59.dev/welcome")
    print("Action: Open browser to pitch59")

    if (login_test_user(driver, test_email, test_password)):
        
        go_to_employee_portal(driver)

        fill_out_form(driver)

        reset_form(driver)

        logout_test_user(driver)



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


def login_test_user(driver, test_email, test_password):
    login_link = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Log in")]')))
    login_link.click()
    print(f"Action: Click login link")

    # Enter email
    email_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
    email_input.send_keys(test_email)
    print(f"Action: Enter email text")

    # Enter password
    password_input = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
    password_input.send_keys(test_password)
    print(f"Action: Enter password text")

    login_button = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "button-simple")]')))
    login_button.click()
    print(f"Action: Click login submit button")

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "profile-photo-container")]')))
    is_element_present = len(driver.find_elements(By.XPATH, '//*[contains(@class, "profile-photo-container")]')) > 0

    if (is_element_present):
        print("Success: Test user has been logged in\n")
        return True
    else:
        print("Fail: Test user was not logged in\n")
        return False


def logout_test_user(driver):
    user_popup_menu = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//img[@class="profile-photo"]')))
    user_popup_menu.click()
    print("Action: Open user popup menu")

    logout_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "logout-btn") and contains(text(), "Logout")]')))
    logout_button.click()
    print("Action: Click logout button")

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Log in")]')))
    is_element_present = len(driver.find_elements(By.XPATH, '//*[contains(text(), "Log in")]')) > 0

    if (is_element_present):
        print("Success: Test user has been logged out\n")
        return True
    else:
        print("Fail: Test user was not logged out\n")
        return False


def go_to_employee_portal(driver):
    
    employ_portal_link = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "Employer Portal")]')))
    employ_portal_link.click()
    print(f"Action: Click employee portal link")

    is_present = len(WebDriverWait(driver, 5).until(EC.presence_of_all_elements_located((By.XPATH, '//*[contains(@class, "ng-tns-c42") and contains(@class, "pi-times")]')))) > 0

    if is_present:
        close_menu_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "ng-tns-c42") and contains(@class, "pi-times")]')))
        close_menu_button.click()
        print(f"Reset Action: Close Billing Pop Up")

    print("Success: Test user has loaded the Employee Portal\n")

    return True


def fill_out_form(driver):
    billing_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Billing")]')))
    billing_button.click()
    print(f"Action: Click Billing")

    more_info_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "More Info")]')))
    more_info_button.click()
    print(f"Action: Click More Info")
    
    industry_drop_down_menu = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(@class, "ui-multiselect-trigger-icon")]')))
    industry_drop_down_menu.click()
    print(f"Action: Click Drop Down Menu")
    
    industry_selection = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Industry") and @class="ng-star-inserted"]')))
    industry_selection.click()
    print(f"Action: Select Industry")

    industry_drop_down_menu = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(@class, "ui-multiselect-trigger-icon")]')))
    industry_drop_down_menu.click()
    print(f"Action: Close Drop Down Menu")
    
    text_entry = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//textarea[@id="description"]')))
    text_entry.send_keys('This is test information, but I am sure the real information will be pretty spiffy')
    print(f"Action: Enter text")

    save_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Save & Next") and contains(@class, "button-simple")]')))
    save_button.click()
    print(f"Action: Save Changes")

    close_menu_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "ng-tns-c42") and contains(@class, "pi-times")]')))
    close_menu_button.click()
    print(f"Action: Close Billing Pop Up")

    print("Success: Form has been filled out\n")

    return True
   

def reset_form(driver):
    billing_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Billing")]')))
    billing_button.click()
    print(f"Action: Click Billing")

    more_info_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(text(), "More Info")]')))
    more_info_button.click()
    print(f"Action: Click More Info")

    industry_drop_down_menu = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(@class, "ui-multiselect-trigger-icon")]')))
    industry_drop_down_menu.click()
    print(f"Action: Click Drop Down Menu")

    industry_deselect = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Industry") and @class="ng-star-inserted"]')))
    industry_deselect.click()
    print(f"Action: Deselect Industry")

    industry_drop_down_menu = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//span[contains(@class, "ui-multiselect-trigger-icon")]')))
    industry_drop_down_menu.click()
    print(f"Action: Close Drop Down Menu")
    
    text_entry = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//textarea[@id="description"]')))
    # For WINDOWS
    text_entry.send_keys(Keys.CONTROL + "a")
    text_entry.send_keys(Keys.BACK_SPACE)
    # For MACOS
    text_entry.send_keys(Keys.COMMAND + "a")
    text_entry.send_keys(Keys.BACK_SPACE)
    print(f"Action: Clear text")

    save_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Save & Next") and contains(@class, "button-simple")]')))
    save_button.click()
    print(f"Action: Save Changes")

    close_menu_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "ng-tns-c42") and contains(@class, "pi-times")]')))
    close_menu_button.click()
    print(f"Action: Close Billing Pop Up")

    print("Success: Form has been reset\n")

    return True


main(sys.argv[1:])