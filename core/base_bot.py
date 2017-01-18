import getopt
import sys
from selenium import webdriver


class BotBase(object):
    def __init__(self, argv, url):
        self.__url = url
        print('Starting the driver')
        driver = webdriver.Firefox()
        driver.get(url=url)
        self.__driver = driver
        self.__menu__(argv=argv)

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
