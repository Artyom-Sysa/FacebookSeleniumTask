import os

from Decorators.Decorators import singleton


@singleton
class Configuration:
    def __init__(self):
        '''
        self.setting - dictionary which filled with default values
        After loading configurations, they will be filled in this dictionary
        '''
        self.settings = {
            ValuesNames.SETTINGS: {
                ValuesNames.DRIVER_PATH: "/usr/bin/chromedriver",
                ValuesNames.FACEBOOK_LOGIN: "",
                ValuesNames.FACEBOOK_PASSWORD: "",
                ValuesNames.BROWSER_HEADLESS: False,
                ValuesNames.ELEMENT_WAIT_TIME:2
            },
            ValuesNames.LOGGER:{
                ValuesNames.LOGGING_CONFIGURAION_FILE_PATH: os.path.join('.', 'Resources', 'logging.ini'),
            }
        }


class ValuesNames:
   SETTINGS = "SETTINGS"
   LOGGER = "LOGGER"
   FACEBOOK_LOGIN = "facebook_login"
   FACEBOOK_PASSWORD = "facebook_password"
   BROWSER_HEADLESS = "browser_headless"
   LOGGING_CONFIGURAION_FILE_PATH ="logging_configurations_file_path"
   DRIVER_PATH = "driver_path"
   ELEMENT_WAIT_TIME= "wait_time_value_in_seconds"