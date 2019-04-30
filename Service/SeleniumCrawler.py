import time

from Config.Configurations import Configuration
from Config.Configurations import ValuesNames as Values
from Service.LoggerService.Implementation.DefaultPythonLoggingService import \
    DefaultPythonLoggingService as Logger
from Service.LoggerService.Implementation.DefaultPythonLoggingService import LoggingLevel as Level
from selenium.webdriver import Chrome
from selenium.common.exceptions import WebDriverException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class SelemimumCrawler:
    __PAGE_URL = "https://www.facebook.com/"
    __EMAIL_INPUT_XPATH = "//input[@name='email']"
    __PASSWORD_INPUT_XPATH = "//input[@name='pass']"
    __ACCOUNT_LINK_XPATH = "//*[@id='userNav']/ul/li[1]/a"
    __FRIENDS_AMOUNT_XPATH = "//*[@data-tab-key='friends']/span[1]"
    __FRIENDS_LINK_XPATH = "//*[@data-tab-key='friends']"
    __FRIENDS_XPATH = "//*[@class='fsl fwb fcb']/a"
    __ACCOUNT_NAME = "//*[@id='fb-timeline-cover-name']/a"

    def __init__(self, driver_path="chromedriver", options=None):
        Logger.info(__file__, "SeleniumCrawler init")

        try:
            self.driver = Chrome(executable_path=driver_path, options=options)
            Logger.info(__file__, "Driver initiated")
        except WebDriverException as err:
            Logger.error(__file__, err.args)

        self.configs = Configuration()

    def execute(self):
        data = dict()

        Logger.info(__file__, f"Opening {self.__PAGE_URL} page")
        self.driver.get(self.__PAGE_URL)

        Logger.info(__file__, "Finding login input web element")
        login_web_element = self.get_element(by=By.XPATH,
                                             value=self.__EMAIL_INPUT_XPATH,
                                             wait=self.configs.settings[Values.SETTINGS][Values.ELEMENT_WAIT_TIME])

        Logger.info(__file__, "Send email to login input web element}")
        login_web_element.send_keys(self.configs.settings[Values.SETTINGS][Values.FACEBOOK_LOGIN])

        Logger.info(__file__, "Finding password input web element")
        password_web_element = self.get_element(by=By.XPATH,
                                                value=self.__PASSWORD_INPUT_XPATH,
                                                wait=self.configs.settings[Values.SETTINGS][Values.ELEMENT_WAIT_TIME])

        Logger.info(__file__, "Send password to password input web element}")
        password_web_element.send_keys(self.configs.settings[Values.SETTINGS][Values.FACEBOOK_PASSWORD])

        Logger.info(__file__, "Send Enter key pressing to password input web element}")
        password_web_element.send_keys(Keys.ENTER)

        Logger.info(__file__, "Finding account link")
        account_button_web_element = self.get_element(by=By.XPATH,
                                                      value=self.__ACCOUNT_LINK_XPATH,
                                                      wait=self.configs.settings[Values.SETTINGS][
                                                          Values.ELEMENT_WAIT_TIME])
        Logger.info(__file__, "Click on account link")
        account_button_web_element.click()

        Logger.info(__file__, "Extracting total friends amount value")
        total_friends_amount = int(self.get_element(by=By.XPATH,
                                                    value=self.__FRIENDS_AMOUNT_XPATH,
                                                    wait=self.configs.settings[Values.SETTINGS][
                                                        Values.ELEMENT_WAIT_TIME]).text)
        Logger.debug(__file__, f"Extracted {total_friends_amount} value")

        Logger.info(__file__, "Finding friends page link")
        friends = self.get_element(by=By.XPATH,
                                   value=self.__FRIENDS_LINK_XPATH,
                                   wait=self.configs.settings[Values.SETTINGS][Values.ELEMENT_WAIT_TIME])

        Logger.info(__file__, "Click on friends page link")
        friends.click()

        Logger.info(__file__, "Extracting account name")
        name = self.get_element(by=By.XPATH,
                                value=self.__ACCOUNT_NAME,
                                wait=self.configs.settings[Values.SETTINGS][Values.ELEMENT_WAIT_TIME]).text

        friends = self.__get_friends_list()

        previous_friend_amount = 0
        current_friends_amount = len(friends)

        while previous_friend_amount != current_friends_amount:
            Logger.info(__file__, "Friends list can be scroll")

            previous_friend_amount = current_friends_amount

            Logger.info(__file__, "Scroll to last friends list element")
            ActionChains(self.driver).move_to_element(friends[-1]).perform()

            time.sleep(1)

            friends = self.__get_friends_list()

            current_friends_amount = len(friends)

        Logger.info(__file__, "Full friends list already loaded")

        Logger.info(__file__, "Extract data from friends web elements list")

        data["Account name: "] = name

        for friend in friends:
            link = friend.get_attribute("href")
            data[link[:friend.get_attribute('href').find('fref') - 1]] = friend.text

        Logger.info(__file__, "Closing web driver")

        Logger.info(__file__, "Closing selenium web driver");

        self.driver.quit()

        data["Total friends amount"] = total_friends_amount
        data["Scanned friends amount"] = current_friends_amount

        return data

    def __get_friends_list(self):
        Logger.info(__file__, "Load friends list web elements")

        list = self.get_elements(by=By.XPATH,
                                 value=self.__FRIENDS_XPATH,
                                 wait=self.configs.settings[Values.SETTINGS][Values.ELEMENT_WAIT_TIME])

        Logger.debug(__file__, f"Size of loaded friends list: {len(list)}")
        return list

    def get_element(self, by, value, wait=0):
        try:
            return WebDriverWait(self.driver, wait).until(EC.presence_of_element_located((by, value)))
        except TimeoutException as err:
            Logger.error(__file__, err.args)

    def get_elements(self, by, value, wait=0):
        try:
            return WebDriverWait(self.driver, wait).until(EC.presence_of_all_elements_located((by, value)))
        except TimeoutException as err:
            Logger.error(__file__, err.args)
