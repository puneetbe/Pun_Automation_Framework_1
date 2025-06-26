# This is my first automation practise

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import allure
from datetime import datetime

# import moment
# global driver

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver=self.driver
        driver.get(utils.URL)
        login_page = LoginPage(driver)
        login_page.enter_username(utils.username)
        login_page.enter_password(utils.password)
        login_page.click_login_button()

    def test_logout(self):
        try:
            driver=self.driver
            home_page = HomePage(driver)
            home_page.homepage_dropdown_button()
            home_page.homepage_logout_button()
            assert driver.title == "abc"

        except AssertionError as error:
            print("Assertion error occurred")
            print(error)
            # currTime = moment.now().strftime("%d-%m-%Y %Hhr/%Mmin/%Ssec")
            currTime = datetime.now().strftime("%d-%m-%Y %Hhr/%Mmin/%Ssec")
            testName = utils.whoami()
            screenshotName = testName +"_"+ currTime

            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)

            driver.get_screenshot_as_file("C:/Users/puntiwar/PycharmProjects/Pun_Automation_Framework_1/screenshots" + screenshotName + ".png")
            raise

        except Exception as e:
            print("There was an exception")

            currTime = datetime.now().strftime("%d-%m-%Y %Hhr/%Mmin/%Ssec")
            testName = utils.whoami()
            screenshotName = testName + "_" + currTime

            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)

            raise

        else:
            print("No Exception Occurred")

        finally:
            print("I am inside finally block")








