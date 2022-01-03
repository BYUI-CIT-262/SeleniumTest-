Standardized tests can also be found in a github repo https://github.com/BYUI-CIT-262/pitch59selenium_standardized

Setup

Headless Mode
Configures the app to run in headless mode (chrome window wont show up while testing).
--headless or -h

## Docker Mode
=======
Run pip install -r requirements.txt

Run the tests with pytest


If you would like to run a specific test, run pytest /path/to/test_file.py

Command Line Options

Headless Mode
Configures the app to run in headless mode (chrome window wont show up while testing).
--headless or -H

Docker Mode
Configures the app to look for a remote copy of the chrome driver running locally on a docker container.
--docker or -D

CI Mode
Configures the app to run in headless mode and forces the --docker flag to false. Used for running the tests on a CI server in gitlab or github.
--ci

Writing New Tests

Documentation: https://docs.pytest.org/en/6.2.x/index.html

This project makes use of a library named pytest, which is a testing framework that makes writing tests easier to write and read.

Writing a New Test
In pytest, code is marked as a test by function and file naming conventions. To mark code as a test, the code must (1) be contained in a function named with the prefix test
def test_equality():
    assert 1 == 1
and (2) must be located in a file named with the prefix test_
/tests/test_equality.py

Pytest Fixtures

Documentation: https://docs.pytest.org/en/6.2.x/fixture.html

This project makes use of a feature of pytest named fixtures. In short, pytest fixtures are small bits of reusable data or logic that are injected into your test functions. The pytest fixtures are located in the conftest.py file in the root of this project.
Here is a list of the fixtures set up in the project:

driver
Returns an instance of webdriver.Chrome or webdriver.Remote depending on the --docker command line flag
This is an
def test_load_website(driver):
    # Load the website you want to test
    driver.get("https://public.p59.dev/welcome")


user
Returns a dictionary with a valid user firstName, lastName, email, password, phone, zip, userId, roleId, and token
This is a global user that is used across all tests. Only use this user for non-destructive tasks. The user is created before the tests run, and then is deleted after the tests run.
def test_same_first_and_last_name(user):
    assert user['firstName'] == user['lastName']


wait
Returns a function that takes an xpath
When wait is called with an xpath as an input, it will wait for the element at that xpath to be clickable before returning the element
def test_click_a_button(driver, wait):
    driver.get("https://public.p59.dev/welcome")

    # Wait for the nav bar login button to be clickable and then click on it
    wait('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[3]').click()


wait_for_url
Returns a function that takes a url
When wait_for_url is called with a url as an input, it will wait for the current url to change to the given url
def test_click_then_navigate(driver, wait, wait_for_url):
    driver.get("https://public.p59.dev/welcome")

    # Wait for the nav bar pricing button to be clickable and then click on it
    wait('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span').click()
      
    # Wait for url to change to the pricing url      
    wait_for_url('https://public.p59.dev/cards-packages')


get_local_storage
Returns a function that takes a local storage key
When get_local_storage is called with a local storage key (string), it will return a dictionary with the data contained at that key
def test_user_details(driver, wait, wait_for_url):
   # pitch59 uses local storage to store some data about the user, lets login and then print >    some of the data.
   
   driver.get("https://public.p59.dev/welcome")

   # Click nav bar login
   wait('//*[@id="header-container"]/div/app-welcome-page-header/div/div[2]/span[3]').click()

   # Fill out username and password
   wait('//*[@id="email"]').send_keys(user['email'])
   wait('//*[@id="password"]').send_keys(user['password'])

   # Click login
   wait('/html/body/app-root/main/app-new-sign-in/div/div/div/div/div[2]/div/form/button').click()

   userDetails = get_local_storage('userDetails')
   print(userDetails['userId'])    # >> 367083231017103355
   print(userDetails['token'])     # >> eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...


Notes on Fixtures

You will almost always need the driver and wait fixture, so make sure you put that in your test function's parameters.
Generally, you will want to use the wait fixture anytime you want to get an element with an xpath, this ensures the test runs as fast as possible without running into errors where the element doesn't exist yet.
It's also important to note that most of the fixtures are merely shortcuts to Selenium features. You can still make use of all of the features of Selenium directly in your tests, so don't hesitate to import things that you need. However, consider making a fixture for it to make it easier next time you need to use the same feature :)


Docker Mode
Docker is a containerization framework, whereby you can access any type of computer with a single command, and it runs almost anywhere (especially the cloud).
In this case we are accessing a miniature computer or 'container' running chrome browser.
The advantage to this approach is not having to install the Selenium Chrome Driver on your computer, AND we are now ready to deploy this to the cloud.

Setup

Install Docker: https://docs.docker.com/get-docker/

Make sure Docker is running - you should see an icon on your computer showing it running
Run this command docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome:4.0.0-beta-3-20210426

Now that chrome is running in the docker container on port 4444, you can access it by running the tests in docker mode pytest --docker



Zalenium
Zalenium record Selenium Test Execution Video

docker pull elgalu/selenium
docker pull elgalu/zelanium
docker run --rm -ti --name zalenium -p 4444:4444 -v /var/run/docker.sock:/var/run/docker.sock -v /tmp/videos:/home/seluser/videos --privileged dosel/zalenium start

run the test in docker mode
headless mode selenimun test record http://localhost:4444/dashboard/
