from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# basic functions
def get_chrome_web_driver(options):
    return webdriver.Chrome(chrome_options=options)

def get_web_driver_options():
    return webdriver.ChromeOptions()
    

# now lets call ignore certificate error

def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')
    

def set_browser_as_incognito(options):
    options.add_argument('--incognito')