# http://scraping.pro/recaptcha-solve-selenium-python/
# http://takefreebitcoin.com/
from time import sleep

import pytesseract
from PIL import Image


class SolvedMedia:
    """
    http://solvemedia.com/publishers/captcha-type-in
    """
    CURRENT_DRIVER = None

    def __init__(self, driver):
        self.CURRENT_DRIVER = driver

    @staticmethod
    def extract_text_image(im):
        text = pytesseract.image_to_string(im)
        print(text)
        return text.split('. ')[1]

    def screen_shot(self):
        location = self.CURRENT_DRIVER.find_element_by_id("adcopy-puzzle-image").location
        size = self.CURRENT_DRIVER.find_element_by_id("adcopy-puzzle-image").size
        self.CURRENT_DRIVER.save_screenshot('solved_img.png')
        im = Image.open('solved_img.png')
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        im = im.crop((left, top, right, bottom))
        im.save('solved_img.png')
        return im

    def broken(self):
        try:
            sleep(5)
            self.CURRENT_DRIVER.find_element_by_css_selector("a#adcopy-link-refresh").click()
            sleep(10)
            im = self.screen_shot()
            text = self.extract_text_image(im=im)
            self.CURRENT_DRIVER.find_element_by_css_selector('input#adcopy_response').send_keys(text)
        except Exception as e:
            print(e)
            self.broken()



