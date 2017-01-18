import sys, getopt
from captchas.captcha import SolvedMedia
from selenium import webdriver


class Options:
    LOGIN = None
    PASSWORD = None


def start_drive(url):
    print('Inicia driver ...')
    driver = webdriver.Firefox()
    driver.get(url=url)
    return driver


def execute_login(driver):
    print('Logando ...')
    driver.find_element_by_css_selector('li.login_menu_button > a:nth-child(1)').click()
    driver.find_element_by_css_selector('#login_form_btc_address').send_keys(Options.LOGIN)
    driver.find_element_by_css_selector('#login_form_password').send_keys(Options.PASSWORD)
    driver.find_element_by_css_selector("select#signup_page_captcha_types > option[value='solvemedia']").click()
    SolvedMedia(driver).broken()
    driver.find_element_by_id('login_form').submit()


def collect_bit_coin(driver):
    print('Coletando bitcoin ...')
    SolvedMedia.timer(10)
    while True:
        if driver.find_element_by_css_selector('#myModal22 > a:nth-child(2)').is_displayed():
            driver.find_element_by_css_selector('#myModal22 > a:nth-child(2)').click()
        driver.find_element_by_css_selector("select#free_play_captcha_types > option[value='solvemedia']").click()
        SolvedMedia(driver).broken()
        driver.find_element_by_css_selector('input#free_play_form_button').click()
        if not driver.find_element_by_css_selector('div#adcopy-outer').is_displayed():
            SolvedMedia.timer(3600)


def main(argv):
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
            Options.LOGIN = arg
        elif opt in ("-p", "--password"):
            Options.PASSWORD = arg

    driver = start_drive('https://freebitco.in/')
    try:
        if Options.LOGIN and Options.PASSWORD:
            execute_login(driver)
    except Exception as e:
        print('Erro no login ...')
        print(e)
        if Options.LOGIN and Options.PASSWORD:
            driver.refresh()
            execute_login(driver)

    if Options.LOGIN and Options.PASSWORD:
        collect_bit_coin(driver=driver)


if __name__ == "__main__":
    main(sys.argv[1:])
