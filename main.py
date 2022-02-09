from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "E:\Softwares\Chromedriver\chromedriver.exe"
TWITTER_EMAIL = "sina_eshrati@yahoo.com"
TWITTER_PASSWORD = "sinairge1376"
TWITTER_USERNAME = "sinaeshrati"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=self.service)
        self.down = 1
        self.up = 1

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(4)
        start = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start.click()
        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, 'download-speed').text
        self.up = self.driver.find_element(By.CLASS_NAME, 'upload-speed').text

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:

            # ----------------------------------------- Sign in to Twitter ------------------------------------
            self.driver.get("https://twitter.com/")
            time.sleep(3)
            sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[5]/a/div')
            sign_in.click()
            time.sleep(4)
            email_input = self.driver.find_element(By.NAME, "text")
            email_input.send_keys(TWITTER_EMAIL)
            next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div/span/span')
            next_button.click()
            time.sleep(3)
            try:
                username_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
                username_input.send_keys(TWITTER_USERNAME)
                username_input.send_keys(Keys.ENTER)
                time.sleep(2)
            except NoSuchElementException:
                pass
            password_input = self.driver.find_element(By.NAME, 'password')
            password_input.send_keys(TWITTER_PASSWORD)
            password_input.send_keys(Keys.ENTER)
            time.sleep(3)

            # ---------------------------------------------- Twitting -----------------------------------------------
            tweet_input = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            tweet_input.send_keys(f"Hey internet provider, Why is my internet speed is {self.down}down/{self.up}up when i paid for {PROMISED_DOWN}down/{PROMISED_UP}up ")
            tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
            tweet_button.click()
            time.sleep(2)
            self.driver.quit()


# ------------------------------------------------- Create Object from Class ---------------------------------
bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
