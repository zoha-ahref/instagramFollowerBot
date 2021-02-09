from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

SIMILAR_ACCOUNT = "SIMILAR_ACCOUNT_USERNAME"
USERNAME = "YOUR USERNAME"
PASSWORD = "redbull123"

driver_path = "DRIVER_PATH"
class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)



    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        username = self.driver.find_element_by_name("username")
        username.send_keys(USERNAME)
        password = self.driver.find_element_by_name("password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)


    def find_followers(self):
        time.sleep(5)
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/')
        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        time.sleep(2)
        scr1 = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
            time.sleep(2)
    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_button.click()

insta = InstaFollower(driver_path)
insta.login()

insta.find_followers()

insta.follow()