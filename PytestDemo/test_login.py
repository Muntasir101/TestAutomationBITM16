import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time


def login(username, password):
    # Finding WebElements
    username_element = driver.find_element(By.NAME, "username")
    password_element = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

    # Type Email
    username_element.clear()
    username_element.send_keys(username)

    # Type Password
    password_element.clear()
    password_element.send_keys(password)

    # Click Login button
    login_button.click()

@pytest.fixture()
def browser_config():
    global driver

    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    time.sleep(5)
    print("Browser launch Successfully")

    yield
    driver.close()


@pytest.mark.order(1)
def test_login_valid_testCase01(browser_config):
    login("Admin", "admin123")


@pytest.mark.order(2)
def test_login_invalid_testCase02(browser_config):
    login("Admin Invalid", "123123")
