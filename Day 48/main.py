from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# URL = "https://www.amazon.co.uk/Portable-Mechanical-Keyboard-Minimalist-Convenient/dp/B09YV448ZY/ref=sr_1_4?crid=L3Y149K4I8V4&keywords=white%2Bmechanical%2Bkeyboard&qid=1693235122&sprefix=white%2Bmechanical%2Bkeyboar%2Caps%2C87&sr=8-4&th=1"


# # Keep Chrome browser open after program finishes
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options = chrome_options)
# driver.get("https://www.python.org")

# time.sleep(10)

# price_pound = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
# price_pennies = driver.find_element(By.CLASS_NAME,value="a-price-fraction").text


# search_bar = driver.find_element(By.NAME, value="q")
# button = driver.find_element(By.ID,value="submit")
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")


# print(f"The price is {price_pound}.{price_pennies}")
# print(search_bar.get_attribute("placeholder"))
# print(button.size)
# print(documentation_link.text)

# # driver.close()
# driver.quit()

# Scraping events from python website

URL = "https://www.python.org/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

event_times = driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR,value=".event-widget a")

upcoming_events = {}
for i in range(0,len(event_times)):
    dict = {
        "time": event_times[i].text,
        "name": event_names[i].text,
    }
    upcoming_events[i] = dict

print(upcoming_events)

driver.quit()
