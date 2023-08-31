from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from decouple import config
import time

# Configuration
URL = "https://tinder.com/app/recs"
PHONE = config("PHONE")
PASSWORD = config("PASSWORD")

# Initialize WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# Helper function to find elements and wait
def find_element(selector, timeout=5):
    return driver.find_element(By.CSS_SELECTOR, value=selector)

def wait(seconds):
    time.sleep(seconds)

# Actions
wait(5)
find_element("#u-1535117240 div ... button").click()  # Decline cookies

wait(5)
find_element("#u-1535117240 div ... a").click()  # Click Log in

wait(5)
find_element("... button").click()  # Click log in with Facebook

wait(5)
driver.switch_to.window(driver.window_handles[1])
print(driver.title)

wait(2)
find_element("... button").click()  # Decline cookies

wait(5)
find_element("#email").send_keys(PHONE)
find_element("#pass").send_keys(PASSWORD + Keys.ENTER)

driver.switch_to.window(driver.window_handles[0])
print(driver.title)

wait(10)
find_element("... button:nth-child(1)").click()  # Allow location

wait(2)
find_element("... button:nth-child(1)").click()  # Allow notifications

swiped = 0
wait(5)
while swiped < 6:
    find_element("... button").click()  # Like
    swiped += 1
    wait(1)

wait(5)
find_element("... button").click()  # Not interested

while True:
    find_element("... button").click()  # Keep swiping
    wait(1)
