from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSf7h1tv_ineAkFouXPc3K7RksxPlvR3GKQYo0RwfN8zLISiOw/viewform?usp=sf_link"
RM_URL = "https://www.rightmove.co.uk/property-to-rent/find.html?locationIdentifier=REGION%5E904&maxBedrooms=3&minBedrooms=1&maxPrice=800&minPrice=400&propertyTypes=flat&mustHave=&dontShow=&furnishTypes=furnished&keywords="

response = requests.get(url=RM_URL)
data = response.text
soup = BeautifulSoup(data,"html.parser")
all_listings = soup.find_all(name="div",class_="is-list")

address = [listing.find(name="address").text.strip() for listing in all_listings]
prices = [listing.find(name="span",class_="propertyCard-priceValue").text.strip() for listing in all_listings]
links = [listing.find(name="a",class_="propertyCard-link").get("href") for listing in all_listings]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(FORM_URL)
for i in range(len(all_listings)):
  time.sleep(2)

  address_input = driver.find_element(By.CSS_SELECTOR,value="#mG61Hd div.RH5hzf.RLS9Fe div div.o3Dpx div:nth-child(1) div div div.AgroKb div div.aCsJod.oJeWuf div div.Xb9hP input")
  address_input.send_keys(address[i])

  price_input = driver.find_element(By.CSS_SELECTOR,value="#mG61Hd div.RH5hzf.RLS9Fe div div.o3Dpx div:nth-child(2) div div div.AgroKb div div.aCsJod.oJeWuf div div.Xb9hP input")
  price_input.send_keys(prices[i])

  link_input = driver.find_element(By.CSS_SELECTOR,value="#mG61Hd div.RH5hzf.RLS9Fe div div.o3Dpx div:nth-child(3) div div div.AgroKb div div.aCsJod.oJeWuf div div.Xb9hP input")
  link_input.send_keys(links[i])

  submit_button = driver.find_element(By.CSS_SELECTOR,value="#mG61Hd div.RH5hzf.RLS9Fe div div.ThHDze div.DE3NNc.CekdCb div.lRwqcd div")
  submit_button.click()

  time.sleep(1)
  restart_button = driver.find_element(By.CSS_SELECTOR,value="body div.Uc2NEf div:nth-child(2) div.RH5hzf.RLS9Fe div div.c2gzEf a")
  restart_button.click()

driver.quit()
