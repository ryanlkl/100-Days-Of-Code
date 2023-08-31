from selenium import webdriver

class InternetSpeedTwitterBot():

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("Detach",True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = None
        self.up = None

    def get_internet_speed(self):
        pass

    def tweet_at_provider()
        pass
