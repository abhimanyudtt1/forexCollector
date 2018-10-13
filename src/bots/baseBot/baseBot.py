from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ActionChains
import os
import time
from selenium.common import exceptions
from src.common.retry import retry
from src.configParser.parseConfig import ParseConfig
from src.common.configKeys import configKeys
from src.common.selectors import selectors
from src.common.selectorType import selectorType

class BaseBot(object):

    baseUrl = None  # type: Union[ str]
    FIND_ELEMENT_STRING = "find_element_by_"
    FIND_ELEMENTS_STRING = "find_elements_by_"


    def __init__(self,config,commonConfigFile):
        self.botConfig = ParseConfig(config)
        self.baseUrl = self.botConfig.getConfig()[configKeys.COMMON_CONFIGS_URL]
        self.commonConfig = ParseConfig(commonConfigFile)
        self.driver = webdriver.Remote(
            command_executor='http://%s:%s/wd/hub' % (
                self.commonConfig.getConfig()[configKeys.SELENIUM_SERVER][configKeys.SELENIUM_IP],
                self.commonConfig.getConfig()[configKeys.SELENIUM_SERVER][configKeys.SELENIUM_PORT]),
            desired_capabilities=DesiredCapabilities.FIREFOX)
        self.mainInfo = None

    def getPageDriver(self):
        return  self.driver


    @retry(10,1)
    def findElements(self,element,selector=None):
        seleniumElement = None
        if selector == None:
            seleniumElement = self.getPageDriver()
        else:
            seleniumElement = selector
        elementFinder = getattr(seleniumElement,self.FIND_ELEMENTS_STRING+element.getType())
        return elementFinder(element.getSelector())

    @retry(10, 1)
    def findElement(self,element,selector=None):
        seleniumElement = None
        if selector == None:
            seleniumElement = self.getPageDriver()
        else:
            seleniumElement = selector
        elementFinder = getattr(seleniumElement,self.FIND_ELEMENT_STRING+element.getType())
        return elementFinder(element.getSelector())

    def redirectToBaseUrl(self):
        self.driver.get(self.baseUrl)

    def __del__(self):
        screenShotDir = self.botConfig.getConfig()[configKeys.SCREENSHOT_DIR]
        screenShotFileName = self.__class__.__name__ + time.strftime("_%Y_%m_%d_%H_%M_%S", time.gmtime())
        screenShotFilePath = '/'.join([screenShotDir,screenShotFileName])
        if not os.path.exists(screenShotDir) :
            os.mkdir(screenShotDir)
        self.driver.save_screenshot("%s.png" % screenShotFilePath)
        self.driver.close()

    def saveInfo(self):
        dataSaveDir = self.botConfig.getConfig()[configKeys.DATA_SAVE_DIR]
        dataSaveFileName = self.__class__.__name__ + time.strftime("_%Y_%m_%d_%H_%M_%S", time.gmtime())+'.dat'
        dataSaveFilePath = '/'.join([dataSaveDir, dataSaveFileName])
        if not os.path.exists(dataSaveDir) :
            os.makedirs(dataSaveDir)
        FH = open(dataSaveFilePath,'w')
        for k,v in self.mainInfo:
            FH.write('%s -> %s\n' % (k,v))
        FH.close()


    def clickElement(self,tag,driver = None):
        element = self.getPageDriver().find_element_by_xpath()
        counter = 0
        lag = 10
        while True :
            counter += 1
            try :
                element.click()
                break
            except exceptions.WebDriverException :
                print "Element not clickable, Waiting to click on element %s" % element
                time.sleep(1)
                if int(counter) > int(lag):
                    print "Timeout Error"
                    raise exceptions.WebDriverException
