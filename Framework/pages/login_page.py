import time

from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def login_orange(self, username, password):
        # Finding WebElements
        username_element = self.driver.find_element(By.NAME, "username")
        password_element = self.driver.find_element(By.NAME, "password")
        login_button = self.driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-button")

        # Type Email
        username_element.clear()
        username_element.send_keys(username)

        # Type Password
        password_element.clear()
        password_element.send_keys(password)

        # Click Login button
        login_button.click()
