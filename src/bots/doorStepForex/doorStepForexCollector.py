from src.bots.baseBot.baseBot import BaseBot
from doorStepForexSelectors import *
from pprint import pprint

class DoorStepForex(BaseBot):
    def __init__(self,config, commonConfigFile):
        super(DoorStepForex, self).__init__( config, commonConfigFile)
    def getInfo(self):
        currencyInfo = []
        rows = self.findElements(rowSelector)
        for eachRow in rows:
            try :
                currency = self.findElement(currencySelector,eachRow).text
                currencyValue = self.findElement(currencyValueSelector,eachRow).text
                currencyInfo.append((currency,currencyValue))
            except Exception :
                pass
        pprint(currencyInfo)
        self.mainInfo = currencyInfo

    def start(self):
        self.redirectToBaseUrl()
        self.getInfo()