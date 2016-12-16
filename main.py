from selenium import webdriver
PATH = '/home/dpge/Projeto/bot_bitcoinenv/bot_bitcoin/browsers/phantomjs-2.1.1-linux-i686/bin/phantomjs'
driver = webdriver.PhantomJS()
driver.set_window_size(1024, 768)
driver.get('https://google.com/')
driver.save_screenshot('screen.png')
sbtn = driver.find_element_by_css_selector('button.gbqfba')
sbtn.click()
