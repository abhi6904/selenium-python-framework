import unittest
from tests.home.login_tests import LoginTest
from tests.courses.register_courses_csv_data import RegisterCoursesCSVDataTests

#Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)

# create all tests suit combining all test classes
smokeTest = unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner(verbosity=2).run(smokeTest)