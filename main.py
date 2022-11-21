import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Keys, ActionChains
from dotenv import load_dotenv
import os

load_dotenv()

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = os.getenv("EMAIL")
TWITTER_PASSWORD = os.getenv("PASSWORD")
CHROME_DRIVER_PATH = Service(
    "C:\Development\chromedriver_win32\chromedriver.exe")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(
            service=driver_path, options=chrome_options)
        self.actions = ActionChains(self.driver)
        self.up = 0
        self.down = 0

    # Creating methods
    def get_internet_speed(self):
        # time.sleep(5)
        self.driver.maximize_window()
        self.driver.get("https://www.speedtest.net/")
        self.go_button = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        self.actions.click(self.go_button).perform()
        time.sleep(45)
        self.down = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(
            By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"Download: {self.down}\nUpload: {self.up} ")

    def tweet_at_provider(self):
        # Login
        self.driver.get("https://twitter.com")
        self.login_button = self.driver.find_element(
            By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a')
        self.actions.click(self.login_button).perform()
        time.sleep(3)
        self.email_input = self.driver.find_element(By.NAME, "text")
        self.actions.click(self.email_input).send_keys(
            TWITTER_EMAIL+Keys.ENTER).perform()
        time.sleep(2)
        self.password_input = self.driver.find_element(By.NAME, "password")
        self.actions.click(self.password_input).send_keys(
            TWITTER_PASSWORD+Keys.ENTER).perform()

        # Complaining with Tweets
        # Not completed from here
        time.sleep(10)
        tweet_input = self.driver.find_element(
            By.ID, 'placeholder-c593c')
        self.actions.click(tweet_input).send_keys("kdjfkdjfdf").perform()


# Creating Object
internet_speed = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
internet_speed.get_internet_speed()
internet_speed.tweet_at_provider()
