import time

import utilities.custome_logger as cl
import logging
from base.basepage import BasePage

class RegisterCoursesPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    ################
    ### Locators ###
    ################
    _all_courses = "//a[normalize-space()='ALL COURSES']"
    _search_box = "//input[@id='search']"
    _search_icon = "//button[@type='submit']"
    _course = "//div[contains(@class,'zen-course-list') and contains(normalize-space(), '{0}')]"
    _enroll_button = "//button[normalize-space()='Enroll in Course']"
    _cc_num = "cardnumber"
    _cc_exp = "exp-date"
    _cc_cvv = "cvc"
    _submit_enroll = "//button[contains(@class, 'zen-subscribe') and contains(@class, 'sp-buy') and contains(@class, 'btn-submit')]"
    _enroll_error_message = "//span[normalize-space()='Your card number is invalid.']"

    ############################
    ### Element Interactions ###
    ############################
    def clickAllCourse(self):
        self.elementClick(locator=self._all_courses, locatorType="xpath")

    def enterCourseName(self, name):
        self.sendKeys(name,locator=self._search_box, locatorType="xpath")
        self.elementClick(locator=self._search_icon,locatorType="xpath")

    def selectCourseToEnroll(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickOnEnrollButton(self):
        self.elementClick(locator=self._enroll_button,locatorType="xpath")

    def enterCardNum(self, num):
        time.sleep(6)
        self.SwitchFrameByIndex(self._cc_num,locatorType="name")
        self.sendKeys(num, locator=self._cc_num, locatorType="name")
        self.switchToDefaultContent()

    def enterCardExp(self, exp):
        self.SwitchFrameByIndex(self._cc_exp,locatorType="name")
        self.sendKeys(exp, locator=self._cc_exp, locatorType="name")
        self.switchToDefaultContent()

    def enterCardCVV(self, cvv):
        self.SwitchFrameByIndex(self._cc_cvv, locatorType="name")
        self.sendKeys(cvv, locator=self._cc_cvv, locatorType="name")
        self.switchToDefaultContent()

    def clickEnrollSubmitButton(self):
        self.elementClick(self._submit_enroll,locatorType="xpath")

    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)

    def enrollCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num,exp,cvv)

    def verifyEnrollFailed(self):
        result = self.isEnabled(locator=self._submit_enroll, locatorType="xpath",
                                info="Enroll Button")
        return not result