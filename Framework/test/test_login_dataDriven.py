import unittest

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
from Framework.utils import excel_utils
from Framework.pages.login_page import LoginPage


class LoginTest(unittest.TestCase):

    def test_login(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        time.sleep(5)

        # Excel implement
        file = "E:\\BITM_Online_16\\Projects\\TestAutomationBITM16\\Framework\\data\\test_data.xlsx"
        sheet = "Sheet1"

        number_of_rows = excel_utils.get_row_count(file, sheet)

        for r in range(2, number_of_rows + 1):
            username = excel_utils.read_data(file, sheet, r, 1)
            password = excel_utils.read_data(file, sheet, r, 2)

            login_page_obj = LoginPage(driver)
            login_page_obj.login_orange(username, password)

        driver.close()
