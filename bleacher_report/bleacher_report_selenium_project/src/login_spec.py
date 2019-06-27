import unittest
from selenium import webdriver
import page
import os
dir_path = os.path.dirname(os.path.realpath(__file__))


class LoginSpec(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=dir_path + '/../chromedriver')
        self.driver.get("http://www.bleacherreport.com")

    def testLoginPage(self):
        dummy_email = "dummyemail@blah.com"
        dummy_password = "letmein"
        main_page = page.HomePage(self.driver)

        # Navigate to login page
        main_page.select_login()
        login_page = page.LoginPage(self.driver)
        assert login_page.is_login_method_page_displayed(), "Login method page did not display."
        # Navigate to login by email
        login_page.select_email_login()
        assert login_page.is_email_login_page_displayed(), "Email login page did not display."
        login_page.input_email(dummy_email)
        login_page.input_password(dummy_password)
        login_page.sign_in()
        assert login_page.is_error_message_displayed(), "Error message for login did not display."

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
