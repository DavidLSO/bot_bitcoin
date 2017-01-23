import sys
from captchas.captcha import SolvedMedia
from core.base_bot import BotBase


class FreeBitCoin(BotBase):
    def execute_login(self):
        print('Initiating login process')
        driver = self.driver
        driver.find_element_by_css_selector('li.login_menu_button > a:nth-child(1)').click()
        driver.find_element_by_css_selector('#login_form_btc_address').send_keys(self.login)
        driver.find_element_by_css_selector('#login_form_password').send_keys(self.password)
        driver.find_element_by_css_selector("select#signup_page_captcha_types > option[value='solvemedia']").click()
        counter = 0
        while driver.current_url == 'https://freebitco.in/':
            counter +=1
            driver.find_element_by_css_selector("#adcopy-link-refresh").click()
            print('Realizing the breaking of captcha: try {0}'.format(counter))
            SolvedMedia(driver).broken()
            print('Sending form')
            driver.find_element_by_id('login_form').submit()
        print('Login success')

    def collect_bit_coin(self):
        print('Starting bitcoin collection')
        self.timer(10)
        driver = self.driver
        while True:
            print(driver.current_url)
            if driver.find_element_by_css_selector('#myModal22 > a:nth-child(2)').is_displayed():
                driver.find_element_by_css_selector('#myModal22 > a:nth-child(2)').click()
            driver.find_element_by_css_selector("select#free_play_captcha_types > option[value='solvemedia']").click()
            SolvedMedia(driver).broken()
            driver.find_element_by_css_selector('input#free_play_form_button').click()
            if not driver.find_element_by_css_selector('div#adcopy-outer').is_displayed():
                self.timer(3600)


def main(argv):
    fbc = FreeBitCoin(argv, 'https://freebitco.in/')

    if fbc.login and fbc.password:
        try:
            fbc.execute_login()
        except Exception as e:
            print('An error occurred while trying to login')
            print(e)
            fbc.refresh()
            fbc.execute_login()

        fbc.collect_bit_coin()


if __name__ == "__main__":
    main(sys.argv[1:])
