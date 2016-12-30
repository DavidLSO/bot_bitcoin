from captchas.recaptcha import ReCaptcha
from selenium import webdriver


def start_drive(url):
    driver = webdriver.Firefox()
    driver.get(url=url)
    return driver


def execute_login(driver):
    driver.find_element_by_css_selector('li.login_menu_button > a:nth-child(1)').click()
    driver.find_element_by_css_selector('#login_form_btc_address').send_keys("sdavidlevy@gmail.com")
    driver.find_element_by_css_selector('#login_form_password').send_keys("123456789")
    driver.find_element_by_css_selector("select#signup_page_captcha_types > option[value='solvemedia']").click()


def main():
    driver = start_drive('https://freebitco.in/')
    execute_login(driver)

if __name__ == "__main__":
    main()



# PATH = 'browsers/phantomjs-2.1.1-linux-i686/bin/./phantomjs'
# driver = webdriver.PhantomJS(executable_path=PATH)
#
# driver.get('https://google.com/')
# driver.save_screenshot('screen.png')
# sbtn = driver.find_element_by_css_selector('button.gbqfba')
# sbtn.click()
