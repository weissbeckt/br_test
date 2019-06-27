from selenium.webdriver.common.by import By


class HomePageLocators(object):
    HOME_BUTTON = (By.ID, 'br-logo')
    LOGIN_BUTTON = (By.CLASS_NAME, 'login')
    SIGN_UP_BUTTON = (By.CLASS_NAME, 'sign-up')


class LoginPageLocators(object):
    LOGIN_METHOD_PAGE = (By.CLASS_NAME, 'chooseLoginMethod')
    EMAIL_LOGIN_PAGE = (By.CLASS_NAME, 'emailLoginForm')
    EMAIL_SIGN_IN = (By.CLASS_NAME, 'email')
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    SIGN_IN = (By.CLASS_NAME, 'submit')
    FORGOT_PASSWORD = (By.CLASS_NAME, 'forgot')
    ERROR_MESSAGE = (By.CLASS_NAME, 'errorMessage')


class SignUpPageLocators(object):
    SIGN_UP_PAGE = (By.CLASS_NAME, 'signupPage')
    SIGN_UP_WITH_EMAIL = (By.CLASS_NAME, 'email')
    FIRST_NAME = (By.NAME, 'first_name')
    LAST_NAME = (By.NAME, 'last_name')
    NAMES_PAGE = (By.CLASS_NAME, 'enterYourNames')
    CONTINUE = (By.XPATH, '//button[contains(text(),"Continue")]')
    USERNAME_PAGE = (By.CLASS_NAME, 'pickUserName')
    USERNAME_INPUT = (By.NAME, 'username')
    EMAIL_INPUT = (By.NAME, 'email')
    PASSWORD_INPUT = (By.NAME, 'password')
    EMAIL_SIGN_UP_PAGE = (By.CLASS_NAME, 'emailSignup')
    BACK = (By.CLASS_NAME, 'flowBack')






