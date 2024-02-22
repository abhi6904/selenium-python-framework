import unittest
import pytest
from pages.courses.register_courses_pages import RegisterCoursesPage
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp","setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self,oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order = 1)
    def test_invalidEnrollment(self):
        self.courses.clickAllCourse()
        self.courses.enterCourseName("javascript")
        self.courses.selectCourseToEnroll("JavaScript for beginners")
        self.courses.enrollCourse(num="1012 3232 5454 6767", exp="1220", cvv="10")
        result = self.courses.verifyEnrollFailed()
        self.ts.markFinal("test_invalidEnrollment", result, "Enrollment verificartion failed")
