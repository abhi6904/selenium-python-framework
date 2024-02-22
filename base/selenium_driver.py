import os.path
import time
from traceback import print_stack

from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities.custome_logger as cl
import logging
import os


class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver = driver

    def screenShot(self,resultMessage):
        """
        Takes screenshot of the current open web page
        """
        fileName = resultMessage + "." +str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "../screenshot/"
        relativeFileName = screenshotDirectory + fileName
        currentDirectory = os.path.dirname(__file__)
        destinationFile = os.path.join(currentDirectory,relativeFileName)
        destinationDirectory = os.path.join(currentDirectory,screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFile)
            self.log.info("screenshot save to directory: " + destinationFile)
        except:
            self.log.error("### Exception Occured")
            print_stack()

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType  = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("locator type " + locatorType + "not corrected/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("element found with locator " + locator + "locatorType " + locatorType)
        except:
            self.log.info("Element not found with locator " + locator + "locatorType " + locatorType)
        return element


    def getElementList(self,locator,locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_elements(byType,locator)
            self.log.info("element list found with locator " + locator + "locatorType " + locatorType)
        except:
            self.log.info("Element list not found with locator " + locator + "locatorType " + locatorType)

        return element


    def elementClick(self,locator="",locatorType = "id",element = None):
        try:
            if locator:
                element = self.getElement(locator,locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + "locatorType: " + locatorType)
        except:
            self.log.info("cannot click on element " + locator + "locatorType: " + locatorType)
            print_stack()

    def sendKeys(self,data,locator="",locatorType = "id",element = None):
        try:
            if locator:
                element = self.getElement(locator,locatorType)
            element.send_keys(data)
            self.log.info("send data on element with locator: " + locator + "locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data click on element " + locator + "locatorType: " + locatorType)
            print_stack()


    def getText(self,locator="",locatorType = "id",element = None, info = ""):
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.getElement(locator,locatorType)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is: "+ str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innertext")
            if len(text) !=0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("the text is :: '" + text + "'")
                text = text.strip()
        except:
            self.log.error("Failed to get text on element " + info)
            print_stack()
            text = None
        return text

    def isElementPresent(self, locator, locatorType="id", element = None):
        try:
            if locator:
                element = self.getElement(locator,locatorType)
            if element is not None:
                self.log.info("element present with locator " + locator + "locatorType: " + locatorType)
                return True
            else:
                self.log.info("element not present with locator " + locator + "locatorType: " + locatorType)
                return False
        except:
            print("Element not found")
            return False


    def isElementDisplayed(self,locator, locatorType="id", element = None):

        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator,locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                self.log.info("element is displayed with locator " + locator + "locatorType: " + locatorType)
            else:
                self.log.info("element is not displayed with locator " + locator + "locatorType: " + locatorType)
            return isDisplayed
        except:
            print("Element not found")
            return False


    def isElementPresenceCheck(self, locator, byType):
        try:
            elementlist = self.driver.find_elements(byType, locator)
            if len(elementlist) > 0:
                self.log.info("element is present with locator " + locator + "locatorType: " + str(byType))
                return True
            else:
                self.log.info("element is not present with locator " + locator + "locatorType: " + str(byType))
                return False
        except:
            self.log.info("Element not found")
            return False

    def waitElement(self, locator, locatorType="id", timeout=10, PollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("waiting for maximum :: " + str(timeout) + " :: second for element for visible")
            wait = WebDriverWait(self.driver, timeout, PollFrequency, ignored_exceptions=[
                NoSuchElementException,
                ElementNotVisibleException,
                ElementNotSelectableException
            ])

            element = wait.until(EC.visibility_of_element_located(
                (byType, locator)))

            self.log.info("element appear on the web page")

        except:
            self.log.info("element not appear on the web page")
            print_stack()
        return element


    def webScroll(self, direction="up"):
        if direction == "up":
        # scroll up
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            #scroll down
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def SwitchFrameByIndex(self, locator, locatorType="xpath"):

        """
        Get iframe index using element locator inside iframe

        Parameters:
            1. Required:
                locator   - Locator of the element
            2. Optional:
                locatorType - Locator Type to find the element
        Returns:
            Index of iframe
        Exception:
            None
        """
        result = False
        try:
            iframe_list = self.getElementList("//iframe", locatorType="xpath")
            self.log.info("Length of iframe list: ")
            self.log.info(str(len(iframe_list)))
            for i in range(len(iframe_list)):
                self.switchToFrame(index=iframe_list[i])
                result = self.isElementPresent(locator, locatorType)
                if result:
                    self.log.info("iframe index is:")
                    self.log.info(str(i))
                    break
                self.switchToDefaultContent()
            return result
        except:
            print("iFrame index not found")
            return result

    def switchToFrame(self, id="", name="", index=None, xpath=""):
        """
        Switch to iframe using element locator inside iframe

        Parameters:
            1. Required:
                None
            2. Optional:
                1. id    - id of the iframe
                2. name  - name of the iframe
                3. index - index of the iframe
        Returns:
            None
        Exception:
            None
        """
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        elif xpath:
            iframe_element = self.driver.find_element(By.XPATH, xpath)
            self.driver.switch_to.frame(iframe_element)
        else:
            self.driver.switch_to.frame(index)

    def switchToDefaultContent(self):
        """
        Switch to default content

        Parameters:
            None
        Returns:
            None
        Exception:
            None
        """
        self.driver.switch_to.default_content()

    def getElementAttributValue(self,attribute, element=None, locator="", locatorType="id"):
        """
        Get value of the attribute of element

        Parameter:
            1. required:
        1. attribute - attribute whose value to find

        2. optional:
            1.element - element whose attribute to be find
            2. locatoe- locator of the element
            3. locatortype- locatortype to find the element

        returns;
            value of the attribute

        """
        if locator:
            element= self.getElement(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)
        return value


    def isEnabled(self,locator,locatorType="id", info=""):

        """
        check if element is enabled
        Parameter:
            1. required:
                1. locator - locator of the element to check

        2. optional:
            1 locatortype- type of the locator(id(default), xpath,css,className,linkText)
            2. info - information about the element, label/name of the element

        returns;
            boolean
        """
        element = self.getElement(  locator,locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributValue(element=element, attribute="class")
                self.log.info("Attribute value from application web ui --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is enabled")
        except:
            self.log.info("Element :: '" + info + "' state could not be found")
        return enabled



