from Service.LoggerService.Implementation.DefaultPythonLoggingService import \
    DefaultPythonLoggingService as Logger
from Service.LoggerService.Implementation.DefaultPythonLoggingService import LoggingLevel as Level
from Config.ConfigLoader.ConfigLoader.Implementation.IniFileConfigLoader import IniFileConfigLoader
from Config.Configurations import Configuration
from Config.Configurations import ValuesNames as Values
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Utils.Utils import Utils
from Service.SeleniumCrawler import SelemimumCrawler
from Reporter.Implementation.ConsoleReporter import ConsoleReporter

class Launcher:
    def __load_configs(self):
        Logger.add_to_journal(__file__, Level.INFO, 'Started load configuration')

        self.configs = Configuration()
        self.config_loader = IniFileConfigLoader()
        self.config_loader.load("./Resources/settings.ini")

        Logger.configurate_logger()

        Logger.add_to_journal(__file__, Level.INFO, 'Loading configuration finished')
        Logger.add_to_journal(__file__, Level.DEBUG, 'Loaded configurations :\n{}'.format(self.configs.settings))

    def __start__selenium(self):
        options = Options()

        options.add_argument("--disable-notifications")

        if self.configs.settings[Values.SETTINGS][Values.BROWSER_HEADLESS]:
            options.add_argument("--headless")

        selemimumCrawler = SelemimumCrawler(self.configs.settings[Values.SETTINGS][Values.DRIVER_PATH], options)
        result = selemimumCrawler.execute()
        reporter = ConsoleReporter()
        reporter.report(data=result)
        Logger.info(__file__, "Program finished")


    def start(self):
        self.__load_configs()
        self.__start__selenium()

if __name__ == '__main__':
    launcher = Launcher()
    launcher.start()
