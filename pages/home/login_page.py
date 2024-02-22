import time
from base.basepage import BasePage
from pages.home.navigation_page import NavigationPage
import utilities.custome_logger as cl
import logging
class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        super().__init__(driver)
        self.driver= driver
        self.nav = NavigationPage(driver)


    #locators
    login_link = "//a[normalize-space()='Sign In']"
    email_feild = "email"
    password_field = "login-password"
    login_btn = "login"
    course = "//a[normalize-space()='ALL COURSES']"


    #perform Action on locators
    def clickLoginLink(self):
        self.elementClick(self.login_link, locatorType="xpath")

    def enterEmail(self,email):
        self.sendKeys(email,self.email_feild)

    def enterPassword(self,password):
        self.sendKeys(password,self.password_field)

    def clickLoginBtn(self):
        self.elementClick(self.login_btn)
        time.sleep(10)

    # def clickAllCourse(self):
    #     self.elementClick(self.course, locatorType="xpath")

    def login(self,email="",password=""):
        self.clickLoginLink()
        self.clearFields()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginBtn()
        # self.clickAllCourse()


    def verifyLoginSuccessfull(self):
        self.waitElement("//div[@class='dropdown']//span[text()='My Account']", locatorType="xpath")
        result = self.isElementPresent("//div[@class='dropdown']//span[text()='My Account']",locatorType="xpath")
        return result

    def verifyLoginFail(self):
        result = self.isElementPresent("//span[contains(text(),'Incorrect login details. Please try again.')]",locatorType="xpath")
        return result



    def verifyTitle(self):
        return self.verifyPageTilte("All Courses")

    def logout(self):
        self.nav.navigateToUserIcon()
        self.waitElement("//a[normalize-space()='Logout']",locatorType="xpath", PollFrequency=1)
        self.elementClick("//a[normalize-space()='Logout']",locatorType="xpath")

    def clearFields(self):
        emailField = self.getElement(locator=self.email_feild)
        emailField.clear()
        passwordField = self.getElement(locator=self.password_field)
        passwordField.clear()