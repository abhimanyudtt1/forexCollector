from src.bots.baseBot.baseBot import BaseBot
from thomasCookSelectors import *
from pprint import pprint

class ThomasCookBot(BaseBot):
    def __init__(self,config, commonConfigFile):
        super(ThomasCookBot, self).__init__( config, commonConfigFile)

    def getInfo(self):
        currencyInfo = []
        rows = self.findElements(rowSelector)
        for eachRow in rows:
            currency = self.findElement(currencySelector,eachRow).text
            currencyValue = self.findElement(currencyValueSelector,eachRow).text

            currencyInfo.append((currency,currencyValue))
        self.mainInfo = currencyInfo

    def start(self):
        self.redirectToBaseUrl()
        self.getInfo()