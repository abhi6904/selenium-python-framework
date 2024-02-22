import unittest
import pytest
from pages.courses.register_courses_pages import RegisterCoursesPage
from utilities.teststatus import TestStatus
from  ddt import ddt, data, unpack


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
@ddt()
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self,oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order = 1)
    @data(("JavaScript for beginners", "1012 3232 5454 6767", "1220", "10"),("Selenium WebDriver 4 With Python","1212 4343 6564 7654", "3440","20"))
    @unpack
    def test_invalidEnrollment(self, courseName,ccNum,ccExp,ccCvv):
        self.courses.clickAllCourse()
        self.courses.enterCourseName(courseName)
        self.courses.selectCourseToEnroll(courseName)
        self.courses.enrollCourse(num=ccNum, exp=ccExp, cvv=ccCvv)
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment verificartion failed")
