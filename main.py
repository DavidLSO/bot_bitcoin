import time

from captchas.captcha import SolvedMedia
from selenium import webdriver


def start_drive(url):
    driver = webdriver.Firefox()
    driver.get(url=url)
    return driver


def execute_login(driver):
    driver.find_element_by_css_selector('li.login_menu_button > a:nth-child(1)').click()
    driver.find_element_by_css_selector('#login_form_btc_address').send_keys("sdavidlevy@gmail.com")
    driver.find_element_by_css_selector('#login_form_password').send_keys("Le352623")
    driver.find_element_by_css_selector("select#signup_page_captcha_types > option[value='solvemedia']").click()
    time.sleep(5)
    while driver.find_element_by_id('adcopy-outer').is_displayed():
        SolvedMedia(driver).broken()
        driver.find_element_by_css_selector('input#login_button').click()


def collect_bit_coin(driver):
    driver.find_element_by_css_selector("select#free_play_captcha_types > option[value='solvemedia']").click()
    time.sleep(5)
    while True:
        SolvedMedia(driver).broken()
        driver.find_element_by_css_selector('input#free_play_form_button').click()
        time.sleep(60000)


def main():
    driver = start_drive('https://freebitco.in/')
    execute_login(driver)
    collect_bit_coin(driver=driver)

if __name__ == "__main__":
    main()
