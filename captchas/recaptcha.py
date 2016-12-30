# http://scraping.pro/recaptcha-solve-selenium-python/

import csv
from random import uniform, randint
from time import sleep, time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ReCaptcha:
    def __init__(self, driver):
        self.__CURRENT_DRIVER = driver

    def write_stat(self, loops, time):
        with open('stat.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([loops, time])

    def check_exists_by_xpath(self, xpath):
        try:
            driver = self.__CURRENT_DRIVER
            driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return True

    @staticmethod
    def wait_between(a, b):
        rand = uniform(a, b)
        sleep(rand)

    @staticmethod
    def dimention(driver):
        d = int(driver.find_element_by_xpath('//div[@id="rc-imageselect-target"]/table').get_attribute("class")[-1])
        return d if d else 3

    def broken(self):
        driver = self.__CURRENT_DRIVER
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "rc-imageselect-target"))
        )
        dim = self.dimention(driver)
        # ****************** check if there is a clicked tile ******************
        if self.check_exists_by_xpath(
                '//div[@id="rc-imageselect-target"]/table/tbody/tr/td[@class="rc-imageselect-tileselected"]'):
            rand2 = 0
        else:
            rand2 = 1

        # wait before click on tiles
        self.wait_between(0.5, 1.0)
        # ****************** click on a tile ******************
        tile1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(
                    randint(1, dim), randint(1, dim))))
        )
        tile1.click()
        if rand2:
            try:
                driver.find_element_by_xpath(
                    '//div[@id="rc-imageselect-target"]/table/tbody/tr[{0}]/td[{1}]'.format(randint(1, dim),
                                                                                            randint(1, dim))).click()
            except NoSuchElementException:
                print('\n\r No Such Element Exception for finding 2nd tile')

        # ****************** click on submit buttion ******************
        driver.find_element_by_id("recaptcha-verify-button").click()
