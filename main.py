from src.bots.thomasCookBot.thomasCookCollector import ThomasCookBot
from src.bots.doorStepForex.doorStepForexCollector import DoorStepForex
from flask import Flask,render_template,render_template_string,request,json,redirect,url_for,g,send_from_directory
from werkzeug.utils import secure_filename



thomasCookBot = ThomasCookBot('configs/sites/thomasCook/basicConfig.yaml',
                              'configs/common/commonConfigs')
doorStepForex = DoorStepForex('configs/sites/doorStepForex/basicConfig.yaml',
                               'configs/common/commonConfigs')


thomasCookBot.start()
thomasCookBot.saveInfo()

doorStepForex.start()
doorStepForex.saveInfo()


