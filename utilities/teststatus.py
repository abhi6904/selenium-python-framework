from base.selenium_driver import SeleniumDriver


class TestStatus(SeleniumDriver):

    def __init__(self,driver):
        """
        Inits CheckPoints class
        """

        super(TestStatus,self).__init__(driver)
        self.resultList = []

    def setResult(self,result, resultMessage):
        try:
            if result is not None:
                if result:
                    self.resultList.append("PASS")
                    self.log.info("### VERIFICATION SUCCESSFULL :: " + resultMessage)
                else:
                    self.resultList.append("FAIL")
                    self.log.info("### VERIFICATION FAILED :: " + resultMessage)
                    self.screenShot(resultMessage)
            else:
                self.resultList.append("FAIL")
                self.log.error("### VERIFICATION FAILED :: " + resultMessage)
                self.screenShot(resultMessage)

        except:
            self.resultList.append("FAIL")
            self.log.error("### Exception Occured !!!")
            self.screenShot(resultMessage)



    def mark(self,result, resultMessage):
        """
        Mark the result of the verification point in a test case
        """

        self.setResult(result,resultMessage)


    def markFinal(self,testName, result, resultMessage):
        """
        Mark the final result of the verification point in a test case
        This needs to be calle at least once in a test case
        This should be final test status of the test case
        """

        self.setResult(result,resultMessage)

        if "FAIL" in self.resultList:
            self.log.error(testName+ "### Test Failed")
            self.resultList.clear()
            assert  True == False
        else:
            self.log.info(testName + "### TEST SUCCESSFULL")
            self.resultList.clear()
            assert True == True