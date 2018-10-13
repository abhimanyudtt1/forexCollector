import yaml
import os


class ParseConfig(object):
    def __init__(self,configFile):
        if os.path.isfile(configFile) :
            FH = open(configFile)
            self.config  = yaml.load(FH)
            FH.close()
        else:
            print "Invalid Config File : %s " % configFile

    def getConfig(self):
        return self.config


