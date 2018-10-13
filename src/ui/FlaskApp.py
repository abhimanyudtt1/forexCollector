from src.bots.thomasCookBot.thomasCookCollector import ThomasCookBot
from src.bots.doorStepForex.doorStepForexCollector import DoorStepForex
from flask import Flask, render_template
from src.configParser.parseConfig import ParseConfig
from src.common.configKeys import configKeys, branchKeys, templateKeys
from src.backend.fs.fileSystemFacade import FileSystemFacade
import jinja2
import os

os.environ['PYTHONPATH'] = ''
from werkzeug.contrib.fixers import ProxyFix
import sys


class forexCollectorApplication(object):
    def __init__(self, configFile):
        self.config = ParseConfig(configFile)
        self.branchConfig = ParseConfig(
            self.config.getConfig()
            [configKeys.UI_PROPERTIES]
            [configKeys.BRANCH_CONFIGS]
        )
        self.templateConfig = ParseConfig(
            self.config.getConfig()
            [configKeys.UI_PROPERTIES]
            [configKeys.TEMPLATE_CONFIGS]
        )
        #print self.branchConfig.getConfig()[branchKeys.UPDATE_DATA]

        host = self.config.getConfig()[configKeys.UI_PROPERTIES][configKeys.UI_HOST]
        port = self.config.getConfig()[configKeys.UI_PROPERTIES][configKeys.UI_PORT]
        self.app = Flask(__name__)
        self.app.wsgi_app = ProxyFix(self.app.wsgi_app)
        self.app.jinja_loader = jinja2.ChoiceLoader([
            self.app.jinja_loader,
            jinja2.FileSystemLoader(self.config.getConfig()[configKeys.UI_PROPERTIES][configKeys.TEMPLATE_LOCATION]),
        ])

        @self.app.route(self.branchConfig.getConfig()[branchKeys.UPDATE_DATA])
        def updatedData():
            thomasCookBot = ThomasCookBot('configs/sites/thomasCook/basicConfig.yaml',
                                          'configs/common/commonConfigs')
            thomasCookBot.start()
            thomasCookBot.saveInfo()
            del thomasCookBot
            
            doorStepForex = DoorStepForex('configs/sites/doorStepForex/basicConfig.yaml',
                                          'configs/common/commonConfigs')
            doorStepForex.start()
            doorStepForex.saveInfo()
            del doorStepForex

            return "Done"

        @self.app.route(self.branchConfig.getConfig()[branchKeys.MAIN_PAGE])
        def loader():
            fileSystemFacade = FileSystemFacade()
            data = fileSystemFacade.getFullData()
            return render_template(self.templateConfig.getConfig()[templateKeys.MAIN_PAGE],message=data)
        self.app.run(host=host, port=port, debug=True)





forexCollectorApplication(sys.argv[1])
