"""
Util class Implementation
All most commonly used utilities should be implemented in this class

Example:
    name = self.util.getUniqueName()
"""
import logging
import random
import string
import time
import traceback

import utilities.custome_logger as cl


class Util(object):

    log = cl.customLogger(logging.INFO)

    def sleep(self,sec,info=""):
        """
        Put the program to wait for the specified amount of time
        """
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "'second for" + info)
            try:
                time.sleep(sec)
            except InterruptedError:
                traceback.print_stack()

    def getAlphaNumeric(self, length, type ='letters'):
        """
        Get random strin of characters

        Parameters:
            length: Length of string, number of characters string should have
            type: Type of characters string should have. Default is letters
            Provide lower/upper/digits for different types
        """

        alpha_num = ''
        if type == 'lower':
            case = string.ascii_lowercase
        elif type == 'upper':
            case = string.ascii_uppercase
        elif type == 'digits':
            case = string.digits
        elif type == 'mix':
            case = string.ascii_letters
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))


    def getUniqueName(self, charCount=10):
        """
        Get a unique name
        """
        return self.getAlphaNumeric(charCount,'lower')


    def getUniqueNameList(self,listSize=5, itemLength=None):
        """
        Get a list of valid email ids

        Parameters:
            listSize: Number of names. Default is 5 email in list
            itemLength: It should be a list containing number of items equal to the listSize
            This determines the length of the each item in the list
        """

        nameList=[]
        for i in range(0,listSize):
            nameList.append(self.getUniqueName(itemLength[i]))



    def verifyTextContains(self,actualText, expectedText):
        """
        Verify actual text contains expected text string

        Parameters:
            expectedList: Expected Text
            actulaList: Actual Text
        """
        self.log.info("Actual Text Fron Application Web UI --> :: " + actualText)
        self.log.info("Expected Text Fron Application Web UI --> :: " + expectedText)
        if expectedText.lower() in actualText.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False

    def verifyTextMatch(self,actualText, expectedText):
        """
        Verify text match

        Parameter:
            expectedList: Expected Text
            actulaList: Actual Text
        """
        if actualText.lower() == expectedText.lower():
            self.log.info("### VERIFICATION MATCHED  !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT MATCHED !!!")
            return False

    def verifyListContains(self, expectedList, actualList):
        """
        Verify temail list contains elements of expected list

        Parameter:
            expectedList: Expected Text
            actulaList: Actual Text
        """
        length = len(expectedList)
        for i in range(0,length):
            if expectedList[i] == actualList[i]:
                return False
        else:
            return True

