import unittest
from selenium import webdriver
import page
import os
dir_path = os.path.dirname(os.path.realpath(__file__))


class HomePageSpec(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=dir_path + '/../chromedriver')
        self.driver.get("http://www.bleacherreport.com")

    def testHomePageDisplays(self):

        # Just validate home page displays
        main_page = page.HomePage(self.driver)
        assert main_page.is_title_matches(), "Bleacher Report title doesn't match."
        assert main_page.is_logo_displayed(), "Bleacher Report logo button not displayed."

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
