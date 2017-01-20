# http://scraping.pro/recaptcha-solve-selenium-python/
# http://takefreebitcoin.com/
from time import sleep
import settings
import pytesseract
from PIL import Image


class SolvedMedia:
    """
    http://solvemedia.com/publishers/captcha-type-in
    """

    def __init__(self, driver):
        self.current_driver = driver
    
    @staticmethod
    def p(img, letter):
        A = img.load()
        B = letter.load()
        mx = 1000000
        max_x = 0
        x = 0
        for x in range(img.size[0] - letter.size[0]):
            _sum = 0
            for i in range(letter.size[0]):
                for j in range(letter.size[1]):
                    _sum = _sum + abs(A[x+i, j][0] - B[i, j][0])
            if _sum < mx :
                mx = _sum
                max_x = x
        return mx, max_x
        
    @staticmethod   
    def ocr(im, threshold=200, alphabet="0123456789abcdef"):
        img = Image.open(im)
        img = img.convert("RGB")
        box = (8, 8, 58, 18)
        img = img.crop(box)
        pixdata = img.load()

        letters = Image.open('letters.bmp')
        ledata = letters.load()

        # Clean the background noise, if color != white, then set to black.
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if (pixdata[x, y][0] > threshold) \
                        and (pixdata[x, y][1] > threshold) \
                        and (pixdata[x, y][2] > threshold):

                    pixdata[x, y] = (255, 255, 255, 255)
                else:
                    pixdata[x, y] = (0, 0, 0, 255)

        counter = 0;
        old_x = -1;

        letterlist = []

        for x in range(letters.size[0]):
            black = True
            for y in range(letters.size[1]):
                if ledata[x, y][0] != 0 :
                    black = False
                    break
            if black :
                if True :
                    box = (old_x + 1, 0, x, 10)
                    letter = letters.crop(box)
                    t = SolvedMedia.p(img, letter);
                    print(counter, x, t)
                    letterlist.append((t[0], alphabet[counter], t[1]))
                old_x = x
                counter += 1

        box = (old_x + 1, 0, 140, 10)
        letter = letters.crop(box)
        t = SolvedMedia.p(img, letter)
        letterlist.append((t[0], alphabet[counter], t[1]))

        t = sorted(letterlist)
        t = t[0:5]  # 5-letter captcha

        final = sorted(t, key=lambda e: e[2])
        answer = ""
        for l in final:
            answer = answer + l[1]
        print(answer)
        return answer

    #print(ocr(sys.argv[1]))
    
    @staticmethod
    def extract_text_image(im):
        text = pytesseract.image_to_string(im)
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

        im = im.crop((left, top, right, bottom))
        im.save(im_path)
        return im

    def broken(self):
        try:
            sleep(5)
            self.current_driver.find_element_by_css_selector("a#adcopy-link-refresh").click()
            sleep(10)
            im = self.screen_shot()
            text = self.extract_text_image(im=im)
            self.current_driver.find_element_by_css_selector('input#adcopy_response').send_keys(text)
        except Exception as e:
            print(e)
            self.broken()



