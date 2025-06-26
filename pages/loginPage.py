from selenium.webdriver.common.by import By
import time


class LoginPage():
    def __init__(self,driver):
        self.driver = driver

        self.username_textbox_css = "input[placeholder='Username']"
        self.password_textbox_css = "input[placeholder='Password']"
        self.login_button_css = "button[type='submit']"


    def enter_username(self,username):
        # self.driver.find_element(self.username_textbox_css).clear()
        self.driver.find_element(By.CSS_SELECTOR,self.username_textbox_css).send_keys(username)
        time.sleep(2)
    def enter_password(self,password):
        # self.driver.find_element(self.password_textbox_css).clear()
        self.driver.find_element(By.CSS_SELECTOR,self.password_textbox_css).send_keys(password)
        time.sleep(2)

    def click_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR,self.login_button_css).click()
        time.sleep(2)