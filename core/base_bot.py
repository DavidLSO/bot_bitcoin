import getopt
import sys
from selenium import webdriver


class BotBase(object):
    def __init__(self, argv, url):
        self.__url = url
        self.__menu__(argv=argv)
        self.__start_driver__()

    @property
    def driver(self):
        return self.__driver

    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @property
    def url(self):
        return self.__url

    @staticmethod
    def timer(sec):
        import time
        for remaining in range(sec, 0, -1):
            print("{:2d} seconds remaining.".format(remaining))
            time.sleep(1)

    @staticmethod
    def __request_proxy__():
        print('Requesting proxy')
        import requests
        r = requests.get(url='http://gimmeproxy.com/api/getProxy')
        return r.json()

    def __set_proxy__(self):
        print('Creating the profile')
        data = self.__request_proxy__()
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type", 1)
        profile.set_preference("network.proxy.http", data['ip'])
        profile.set_preference("network.proxy.http_port", int(data['port']))
        profile.update_preferences()
        return profile

    def __start_driver__(self):
        print('Starting the driver')

        #self.__driver = webdriver.Firefox(firefox_profile=self.__set_proxy__())
        self.__driver = webdriver.PhantomJS()
        self.__driver.set_window_size(1120, 550)
        self.__driver.get(url=self.url)

    def __menu__(self, argv):
        try:
            opts, args = getopt.getopt(argv, "h:l:p:", ["help", "login=", "password="])
        except getopt.GetoptError:
            print('script.py -h <help> -l <login> -p <password>')
            sys.exit(2)

        for opt, arg in opts:
            if opt in ('-h', '--help'):
                print('script.py -h <help> -l <login> -p <password>')
                sys.exit()
            elif opt in ("-l", "--login"):
                self.__login = arg
            elif opt in ("-p", "--password"):
                self.__password = arg

    def execute_login(self):
        pass

    def collect_bit_coin(self):
        pass

    def refresh(self):
        self.driver.refresh()
