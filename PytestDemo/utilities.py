from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

global driver


class Base():

    def browser_launch(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(5)
        print("Browser launch Successfully")

        def browser_close():
            driver.close()

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


