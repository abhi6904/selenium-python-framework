import time
from base.basepage import BasePage
import utilities.custome_logger as cl
import logging
class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver= driver


    #locators
    _home = "HOME"
    _AllCourses = "ALL COURSES"
    _INTERVIEW = "INTERVIEW"
    _SUPPORT = "SUPPORT"
    _BLOG = "BLOG"
    _PRACTICE = "PRACTICE"
    _MY_COURSES = "MY COURSES"
    _USER_ICON = "//button[@id='dropdownMenu1']//a[@class='dynamic-link']"


    #perform Action on locators

    def navigateToHome(self):
        self.elementClick(locator=self._home, locatorType="link")
    def navigateToAllCourses(self):
        self.elementClick(locator=self._AllCourses, locatorType="link")
    def navigateToInterview(self):
        self.elementClick(locator=self._INTERVIEW, locatorType="link")
    def navigateToSupport(self):
        self.elementClick(locator=self._SUPPORT, locatorType="link")
    def navigateToBlog(self):
        self.elementClick(locator=self._BLOG, locatorType="link")
    def navigateToPractice(self):
        self.elementClick(locator=self._PRACTICE, locatorType="link")
    def navigateToMyCourses(self):
        self.elementClick(locator=self._MY_COURSES, locatorType="link")
    def navigateToUserIcon(self):
        userIconElement = self.waitElement(locator=self._USER_ICON, locatorType="xpath", PollFrequency=1)
        self.elementClick(element=userIconElement)
