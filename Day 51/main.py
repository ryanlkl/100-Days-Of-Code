from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 20
PROMISED_UP = 10
TWITTER_EMAIL = "ryanla94@gmail.com"
TWITTER_PASSWORD = "Ryanjessica2003"
TWITTER_PHONE = "07307288855"


class InternetSpeedTwitterBot():

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach",True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = None
        self.up = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(5)
        accept_cookies = self.driver.find_element(By.CSS_SELECTOR,value="#onetrust-accept-btn-handler")
        accept_cookies.click()

        go_button = self.driver.find_element(By.CSS_SELECTOR,value="#container div div.main-content div div div div.pure-u-custom-speedtest div.speedtest-container.main-row div.start-button a")
        go_button.click()

        time.sleep(60)
        down_speed = float(self.driver.find_element(By.CSS_SELECTOR,value="#container div div.main-content div div div div.pure-u-custom-speedtest div.speedtest-container.main-row div.main-view div div.result-area.result-area-test div div div.result-container-speed.result-container-speed-active div.result-container-data div.result-item-container.result-item-container-align-center div div.result-data.u-align-left span").text)
        up_speed =  float(self.driver.find_element(By.CSS_SELECTOR,value="#container div div.main-content div div div div.pure-u-custom-speedtest div.speedtest-container.main-row div.main-view div div.result-area.result-area-test div div div.result-container-speed.result-container-speed-active div.result-container-data div.result-item-container.result-item-container-align-left div div.result-data.u-align-left span").text)
        print(f"Download: {down_speed}\nUpload: {up_speed}")
        return [down_speed,up_speed]

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/home")

        time.sleep(5)
        email_input = self.driver.find_element(By.CSS_SELECTOR,value="#layers div div div div div div div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x div div div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu div div div div.css-1dbjc4n.r-mk0yit.r-1f1sjgu.r-13qz1uu label div div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv div input")
        email_input.send_keys(TWITTER_EMAIL)
        time.sleep(1)
        email_input.send_keys(Keys.ENTER)

        time.sleep(5)
        phone_input = self.driver.find_element(By.CSS_SELECTOR,value="#layers div div div div div div div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x div div div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 div div.css-1dbjc4n.r-mk0yit.r-1f1sjgu label div div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv div input")
        phone_input.send_keys(TWITTER_PHONE)
        time.sleep(1)
        phone_input.send_keys(Keys.ENTER)

        time.sleep(5)
        password_input = self.driver.find_element(By.CSS_SELECTOR,value="#layers div div div div div div div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x div div div.css-1dbjc4n.r-kemksi.r-6koalj.r-16y2uox.r-1wbh5a2 div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 div div div.css-1dbjc4n.r-mk0yit.r-13qz1uu div label div div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv div.css-901oao.r-1awozwy.r-1nao33i.r-6koalj.r-37j5jr.r-1inkyih.r-16dba41.r-135wba7.r-bcqeeo.r-13qz1uu.r-qvutc0 input")
        password_input.send_keys(TWITTER_PASSWORD)
        time.sleep(1)
        password_input.send_keys(Keys.ENTER)

        time.sleep(5)
        post_box = self.driver.find_element(By.CSS_SELECTOR,value="#react-root div div div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 main div div div div.css-1dbjc4n.r-kemksi.r-1kqtdi0.r-1ljd8xs.r-13l2t4g.r-1phboty.r-16y2uox.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c div div.css-1dbjc4n.r-kemksi.r-184en5c div div.css-1dbjc4n.r-kemksi.r-1h8ys4a div:nth-child(1) div div div div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t div:nth-child(1) div div div div div div.css-1dbjc4n.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q div div div div label div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 div div div div div div.DraftEditor-editorContainer div div div div")
        post_box.click()
        time.sleep(1)
        post_box.send_keys("Example message.")


test = InternetSpeedTwitterBot()
# test.get_internet_speed()
test.tweet_at_provider()
