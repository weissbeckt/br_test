from locators import HomePageLocators, LoginPageLocators, SignUpPageLocators
from base import BasePage
import time


class HomePage(BasePage):

    def is_title_matches(self):
        return "Bleacher Report" in self.driver.title

    def is_logo_displayed(self):
        element = self.driver.find_element(*HomePageLocators.HOME_BUTTON)
        return element.is_displayed()

    def select_home_button(self):
        element = self.driver.find_element(*HomePageLocators.HOME_BUTTON)
        element.click()

    def select_login(self):
        element = self.driver.find_element(*HomePageLocators.LOGIN_BUTTON)
        element.click()

    def select_sign_up(self):
        element = self.driver.find_element(*HomePageLocators.SIGN_UP_BUTTON)
        element.click()


class LoginPage(BasePage):

    def is_login_method_page_displayed(self):
        element = self.driver.find_element(*LoginPageLocators.LOGIN_METHOD_PAGE)
        return element.is_displayed()

    def is_email_login_page_displayed(self):
        element = self.driver.find_element(*LoginPageLocators.EMAIL_LOGIN_PAGE)
        return element.is_displayed()

    def select_email_login(self):
        element = self.driver.find_element(*LoginPageLocators.EMAIL_SIGN_IN)
        element.click()

    def input_email(self, val):
        element = self.driver.find_element(*LoginPageLocators.EMAIL_INPUT)
        element.clear()
        element.send_keys(val)

    def input_password(self, val):
        element = self.driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        element.clear()
        element.send_keys(val)

    def sign_in(self):
        element = self.driver.find_element(*LoginPageLocators.SIGN_IN)
        element.click()

    def is_error_message_displayed(self):
        element = self.driver.find_element(*LoginPageLocators.ERROR_MESSAGE)
        return element.is_displayed()


class SignUp(BasePage):

    def is_sign_up_page_displayed(self):
        element = self.driver.find_element(*SignUpPageLocators.SIGN_UP_PAGE)
        return element.is_displayed()

    def is_username_sign_up_displayed(self):
        element = self.driver.find_element(*SignUpPageLocators.USERNAME_PAGE)
        return element.is_displayed()

    def is_name_page_displayed(self):
        element = self.driver.find_element(*SignUpPageLocators.NAMES_PAGE)
        return element.is_displayed()

    def is_email_sign_up_page_displayed(self):
        element = self.driver.find_element(*SignUpPageLocators.EMAIL_SIGN_UP_PAGE)
        return element.is_displayed()

    def select_email_sign_up(self):
        element = self.driver.find_element(*SignUpPageLocators.SIGN_UP_WITH_EMAIL)
        element.click()

    def input_first_name(self, val):
        element = self.driver.find_element(*SignUpPageLocators.FIRST_NAME)
        element.clear()
        element.send_keys(val)

    def input_last_name(self, val):
        element = self.driver.find_element(*SignUpPageLocators.LAST_NAME)
        element.clear()
        element.send_keys(val)

    def input_username(self, val):
        element = self.driver.find_element(*SignUpPageLocators.USERNAME_INPUT)
        element.clear()
        element.send_keys(val)

    def input_email(self, val):
        element = self.driver.find_element(*SignUpPageLocators.EMAIL_INPUT)
        element.clear()
        element.send_keys(val)

    def input_password(self, val):
        element = self.driver.find_element(*SignUpPageLocators.PASSWORD_INPUT)
        element.clear()
        element.send_keys(val)

    def select_continue(self):
        # Guess the button is still clickable when it is disabled so unfortunately just made a 2 second sleep for now
        # element = WebDriverWait(self.driver, 10).until(
        #    EC.element_to_be_clickable((SignUpPageLocators.CONTINUE))
        # )
        time.sleep(2)
        element = self.driver.find_element(*SignUpPageLocators.CONTINUE)
        element.click()

    def back(self):
        element = self.driver.find_element(*SignUpPageLocators.BACK)
        element.click()

