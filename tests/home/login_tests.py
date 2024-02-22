import unittest
import pytest
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus

@pytest.mark.usefixtures("oneTimesetUp","setUp")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimesetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    # need to verify two varification point
    # 1 fails, code will not go to the next verification point
    # if assert fails, it stops current test execution and move to the next method

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("yabhishek9599@gmail.com","Abhi123456789@")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1,"Title is incorrect")
        result2 = self.lp.verifyLoginSuccessfull()
        self.ts.markFinal("TestValidLogin", result2, "Login was successfull")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("y12@gmail.com", "Abhi56789@")
        result = self.lp.verifyLoginFail()
        assert result == True






