import pytest
from selenium import webdriver

def pytest_addoption(parser):
        parser.addoption("--browser", action="store",default="chrome", help="Type in browser name e.g.chrome OR firefox")


@pytest.fixture(scope="class")
def test_setup(request):

        driver = webdriver.Chrome()
        request.cls.driver = driver
        driver.implicitly_wait(5)
        driver.maximize_window()
        browser = request.config.getoption("--browser")
        if browser == 'chrome':
                driver = webdriver.Chrome()
        elif browser == 'firefox':
                driver = webdriver.Firefox()

        yield
        print("Test Completed")
        driver.close()
        driver.quit()