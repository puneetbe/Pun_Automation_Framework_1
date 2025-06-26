from selenium.webdriver.common.by import By
class HomePage():
    def __init__(self,driver):
        self.driver = driver

        self.homepage_dropdown_button_CLASS_NAME = "oxd-userdropdown-name"
        self.homepage_logout_button_LINK_TEXT = "Logout"

    def homepage_dropdown_button(self):
        self.driver.find_element(By.CLASS_NAME,self.homepage_dropdown_button_CLASS_NAME).click()

    def homepage_logout_button(self):
        self.driver.find_element(By.LINK_TEXT,self.homepage_logout_button_LINK_TEXT).click()