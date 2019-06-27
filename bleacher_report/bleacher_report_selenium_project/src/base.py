class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(20)
        self.driver.delete_all_cookies()
        self.driver.set_window_size(1280, 800)
