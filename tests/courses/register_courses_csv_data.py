import unittest
import pytest
from pages.courses.register_courses_pages import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
from  ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp")
@ddt()
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self,oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)


    def setUp(self):
        self.nav.navigateToAllCourses()


    @pytest.mark.run(order = 1)
    # @data(("JavaScript for beginners", "1012 3232 5454 6767", "1220", "10"),("Selenium WebDriver 4 With Python","1212 4343 6564 7654", "3440","20"))
    # @unpack
    @data(*getCSVData("/home/abhishek/Desktop/selenium/automation_Framework1/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName,ccNum,ccExp,ccCvv):
        self.courses.clickAllCourse()
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCvv)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment verificartion failed")
