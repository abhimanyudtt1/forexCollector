from enum import Enum


class configKeys(Enum):
    SELENIUM_SERVER = "SeleniumServer"
    SELENIUM_PORT = "port"
    SELENIUM_IP = "ip"
    COMMON_CONFIGS_URL = 'url'
    SCREENSHOT_DIR = 'screenshotDir'
    DATA_SAVE_DIR = 'dataSaveLocation'
    UI_PROPERTIES = 'ui'
    UI_HOST = 'host'
    UI_PORT = 'port'
    BRANCH_CONFIGS = 'branchConfig'
    TEMPLATE_CONFIGS = 'templateConfig'
    TEMPLATE_LOCATION = 'templateLocation'
    BOT = 'bots'
    BOT_LOCATION = 'botLocation'

class branchKeys(Enum):
    MAIN_PAGE = 'mainPage'
    UPDATE_DATA = 'updateData'


class templateKeys(Enum):
    MAIN_PAGE = 'mainPage'