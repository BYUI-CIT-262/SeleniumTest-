from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from bs4 import BeautifulSoup
import time
import sys
import getopt
import smtplib
import imaplib
import email
#from lxml import etree
USERNAME = 'p59testa@gmail.com'
PASSWORD = "Love1111"


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
# new test account = p59testa@gmail.com   pwd Love1111
print('test start')
link = driver.find_element_by_xpath(
    '//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[4]')
link.click()
print('click login')
time.sleep(3)

forgot_password = driver.find_element_by_xpath(
    '/html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/div[2]/span')
forgot_password.click()
print('click forgot password')

input_email = driver.find_element_by_xpath(
    '//*[@id="userName"]')
input_email.send_keys(USERNAME)
print('input email')

send = driver.find_element_by_xpath(
    '/html/body/app-root/main/app-forgot-password/div/div/div/div/div[2]/div/form/button')
send.click()
print('click send \nsending otp email')
time.sleep(3)

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login('p59testa@gmail.com', '8lP%3f&aSr8rvFzgDLmN4!t0!TJzuu')
mail.list()
# Out: list of "folders" aka labels in gmail.
mail.select("inbox")  # connect to inbox.
result, data = mail.search(
    None, '(FROM "Pitch59" SUBJECT "Reset your forgotten password")')
ids = data[0]  # data is a list.
id_list = ids.split()  # ids is a space separated string
latest_email_id = id_list[-1]  # get the latest
# fetch the email body (RFC822)             for the given ID
result, data = mail.fetch(latest_email_id, "(RFC822)")
raw_email = data[0][1]  # here's the body, which is raw text of the whole email
# including headers and alternate payloads
# print(raw_email)
raw_email_string = raw_email.decode('utf-8')
#
email_message = email.message_from_string(raw_email_string)
# this will loop through all the available multiparts in mail
body = ''
# b = email.message_from_string(email_message)
if email_message.is_multipart():
    for part in email_message.walk():
        ctype = part.get_content_type()
        cdispo = str(part.get('Content-Disposition'))
        # skip any text/plain (txt) attachments
        if ctype == 'text/plain' and 'attachment' not in cdispo:
            body = part.get_payload(decode=True)  # decode
            break
# not multipart - i.e. plain text, no attachments, keeping fingers crossed
else:
    body = email_message.get_payload(decode=True)
# print(raw_email_string)
index = raw_email_string.find('enter the following code:</p>')
code = index + 1
# print('this is code:', raw_email_string[index])
word = 'enter the following code:</p>'
last_word_in_word = raw_email_string.index(word)+len(word)-1
found = True
worddd = raw_email_string[last_word_in_word]
# print(worddd)
i = 1
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
codenum = []
while found:
    if raw_email_string[last_word_in_word+i] != '>':
        i = i + 1
    else:
        i = i+1
        if raw_email_string[last_word_in_word+i] in nums:
            codeword = raw_email_string[last_word_in_word+i]
            for y in range(0, 4):
                codeword = raw_email_string[last_word_in_word+i+y]
                codenum.append(codeword)
            found = False
        else:
            print('Not found')
            found = False
# print('second', worddd)
print('code', codenum)
input_code = driver.find_element_by_xpath(
    '//*[@id="smsOtpCode"]')
for i in codenum:
    input_code.send_keys(i)
    print(i)
print('insert code')
input_new_pwd = driver.find_element_by_xpath(
    '//*[@id="newpassword"]')
input_new_pwd.send_keys(PASSWORD)
print('insert new password')
verify_new_pwd = driver.find_element_by_xpath(
    '//*[@id="confirmpassword"]')
verify_new_pwd.send_keys(PASSWORD)
print('verify new password')
reset = driver.find_element_by_xpath(
    '/html/body/app-root/main/app-reset-password/div/div/div/div/div/form/div[6]/button')
reset.click()
print('click reset')
driver.quit()
