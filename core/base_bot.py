import getopt
import sys
import requests
from selenium import webdriver
import settings

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
        r = requests.get(url='http://gimmeproxy.com/api/getProxy')
        return requests.utils.get_encodings_from_content(r)

    def __set_proxy__(self):
        print('Creating the profile')
        data = self.__request_proxy__()
        return [
            '--proxy={0}'.format(data['ipPort']),
            '--proxy-type=https',
            ]

    def __start_driver__(self):
        print('Starting the driver')
        dcap = dict(webdriver.DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
        #self.__driver = webdriver.PhantomJS(executable_path=settings.PHANTOMJS_DRIVER, service_args=self.__set_proxy__(), desired_capabilities=dcap)
        self.__driver = webdriver.PhantomJS(executable_path=settings.PHANTOMJS_DRIVER, desired_capabilities=dcap)
        self.__driver.maximize_window()
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
