import unittest
from selenium import webdriver
import page
import os
dir_path = os.path.dirname(os.path.realpath(__file__))


class LoginSpec(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=dir_path + '/../chromedriver')
        self.driver.get("http://www.bleacherreport.com/")

    def testEmailSignUpFlow(self):
        first_name = "first"
        last_name = "last"
        dummy_user_name = "b2lasdftds3lf3"
        main_page = page.HomePage(self.driver)

        # Select sign up (Not actually creating a user in prod for you guys testing back and home buttons here as well)
        main_page.select_sign_up()
        sign_up_page = page.SignUp(self.driver)
        assert sign_up_page.is_sign_up_page_displayed(), "Sign Up page did not display."
        sign_up_page.select_email_sign_up()
        assert sign_up_page.is_name_page_displayed(), "Name input page did not display."
        sign_up_page.input_first_name(first_name)
        sign_up_page.input_last_name(last_name)
        sign_up_page.select_continue()
        assert sign_up_page.is_username_sign_up_displayed(), "Username input page did not display."
        sign_up_page.input_username(dummy_user_name)
        sign_up_page.select_continue()
        assert sign_up_page.is_email_sign_up_page_displayed(), "Email input page for sign up did not display."
        sign_up_page.back()
        assert sign_up_page.is_username_sign_up_displayed(), "Username input page did not display after going back."
        main_page.select_home_button()
        assert main_page.is_logo_displayed(), "User not navigated home after selecting home button."

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
