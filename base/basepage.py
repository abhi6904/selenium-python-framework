"""
Base page class implementation
it implement method which are common to all the pages throughout the application

This class needs to be inherited by all the pages classes
This should be used by creating objects instances

Example:
    Class LoginPage(BasePage)
"""

from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from  utilities.util import Util

class BasePage(SeleniumDriver):

    def __init__(self,driver):
        """
        Inits BasePage class

        Returns:
            None
        """
        super(BasePage,self).__init__(driver)
        self.driver = driver
        self.util = Util()


    def verifyPageTilte(self,titleToVerify):
        """
        Verify the page title

        Parameters:
        titletoverify: Title on the page that needs to verified
        """
        try:
            actualTitle = self.getTitle()
            return self.util.verifyTextContains(actualTitle, titleToVerify)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False