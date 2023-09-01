from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from decouple import config

URL ="https://www.linkedin.com/jobs/search/?currentJobId=3688495253&f_AL=true&keywords=software%20developer&refresh=true&sortBy=R"
email = config("ACCOUNT_EMAIL")
password = config("ACCOUNT_PASSWORD")


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_option)
driver.get(URL)

# Reject cookies
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

# Press sign in buttone
time.sleep(2)
sign_in = driver.find_element(By.CSS_SELECTOR,value="body div.base-serp-page header nav div a.nav__button-secondary.btn-md.btn-secondary-emphasis")
sign_in.click()

# Sign in
time.sleep(5)
email_input = driver.find_element(By.CSS_SELECTOR,value="#username")
email_input.send_keys(email)

password_input = driver.find_element(By.CSS_SELECTOR,value="#password")
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

# # Solve CAPTCHA
# input("Press Enter when you have solved the Captcha.")

# # Apply button
# time.sleep(5)
# apply_button = driver.find_element(By.CSS_SELECTOR,value=".jobs-apply-button--top-card button")
# apply_button.click()

# Listings

def abort_application():
    close_button = driver.find_element(By.CLASS_NAME,value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()

time.sleep(5)
all_listings = driver.find_elements(By.CSS_SELECTOR, value="#main div div.scaffold-layout__list div ul li")

for listing in all_listings:
    print("Opened")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR,value="jobs-apply-button--top-card")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element(By.CSS_SELECTOR,value="input[id*=phoneNumber]")
        if phone.text=="":
            phone.send_keys("07408399966")

            submit_button = driver.find_element(By.CSS_SELECTOR,value="footer button")
            if submit_button.get_attribute("data-control-name") == "continue_unify":
                abort_application()
                print("Complex application, skipped.")
                continue
            else:
                print("Submitting application")
                submit_button.clicked()

            time.sleep(2)
            close_button = driver.find_element(By.CLASS_NAME,value="artdeco-modal__dismiss")
            close_button.click()

    except NoSuchElementException:
        abort_application()
        print("No apply button")
        continue

time.sleep(5)
driver.quit()
