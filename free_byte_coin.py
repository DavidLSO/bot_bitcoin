from captchas.captcha import SolvedMedia
from selenium import webdriver


def start_drive(url):
    print('Inicia driver ...')
    driver = webdriver.Firefox()
    driver.get(url=url)
    return driver


def execute_login(driver):
    print('Logando ...')
    driver.find_element_by_css_selector('li.login_menu_button > a:nth-child(1)').click()
    driver.find_element_by_css_selector('#login_form_btc_address').send_keys("sdavidlevy@gmail.com")
    driver.find_element_by_css_selector('#login_form_password').send_keys("Le352623")
    driver.find_element_by_css_selector("select#signup_page_captcha_types > option[value='solvemedia']").click()
    SolvedMedia(driver).broken()
    driver.find_element_by_id('login_form').submit()


def collect_bit_coin(driver):
    print('Coletando bitcoin ...')
    SolvedMedia.timer(10)
    while True:
        driver.find_element_by_css_selector("select#free_play_captcha_types > option[value='solvemedia']").click()
        SolvedMedia(driver).broken()
        driver.find_element_by_css_selector('input#free_play_form_button').click()
        SolvedMedia.timer(6000)


def main():
    driver = start_drive('https://freebitco.in/')
    try:
        execute_login(driver)
    except Exception as e:
        print('Erro no login ...')
        print(e)
        driver.refresh()
        execute_login(driver)

    collect_bit_coin(driver=driver)

if __name__ == "__main__":
    main()
