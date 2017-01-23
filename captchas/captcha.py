# http://scraping.pro/recaptcha-solve-selenium-python/
# http://takefreebitcoin.com/
from time import sleep
import settings
import pytesseract
from PIL import Image
import numpy as np

class SolvedMedia:
    """
    http://solvemedia.com/publishers/captcha-type-in
    """

    def __init__(self, driver):
        self.current_driver = driver
    
    @staticmethod
    def extract_text_image(im):
        pytesseract.pytesseract.tesseract_cmd = settings.PYTESSERACT_PATH
        text = ' '.join(pytesseract.image_to_string(im, lang='eng',).split('\n')).strip()
        print(text)
        return text

    def screen_shot(self):
        location = self.current_driver.find_element_by_id("adcopy-puzzle-image").location
        size = self.current_driver.find_element_by_id("adcopy-puzzle-image").size
        im_path = '{0}\\{1}'.format(settings.SCREENSHOT_PATH, 'solved_img.png')
        self.current_driver.save_screenshot(im_path)
        im = Image.open(im_path)
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        im = im.crop((left, top+17, right, bottom))
        im.save(im_path)
        return im

    @staticmethod
    def processing_image(im):
        im = im.convert('RGBA')
        data = np.array(im)
        # just use the rgb values for comparison
        rgb = data[:,:,:3]
        color = [246, 213, 139]   # Original value
        black = [0,0,0, 255]
        white = [255,255,255,255]
        mask = np.all(rgb == color, axis = -1)
        # change all pixels that match color to white
        data[mask] = white

        # change all pixels that don't match color to black
        ##data[np.logical_not(mask)] = black
        new_im = Image.fromarray(data)
        new_im.save('{0}\\{1}'.format(settings.SCREENSHOT_PATH, 'solved_img.png'))
        return new_im

    def broken(self):
        try:
            sleep(5)
            self.current_driver.find_element_by_css_selector("a#adcopy-link-refresh").click()
            sleep(10)
            im = self.screen_shot()
            #im = self.processing_image(im)
            text = self.extract_text_image(im=im)
            self.current_driver.find_element_by_css_selector('input#adcopy_response').send_keys(text)
        except Exception as e:
            print(e)
            self.broken()



