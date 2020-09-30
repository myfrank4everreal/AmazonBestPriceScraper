# Basic import essentials
import requests
import json
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from web_driver_conf import get_web_driver_options
from web_driver_conf import get_chrome_web_driver


from web_driver_conf import set_browser_as_incognito
from web_driver_conf import set_ignore_certificate_error


from product import Product




# basic function call
options = get_web_driver_options()
driver = get_chrome_web_driver(options)


# calling the web page and search term
URL = "http://www.amazon.ae/"
NUMBER_OF_PAGES_TO_SEARCH = 5
QUESTION_PRODUCT = "wHAT ARE YOU LOOKING FOR ?\n:"

search_term = str(input(QUESTION_PRODUCT))

# opening the web page
driver.get(URL)
element = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
element.send_keys(search_term)
element.send_keys(Keys.ENTER)


products = []

# set  page limits 
page= NUMBER_OF_PAGES_TO_SEARCH

while True:
    if page != 0:
        try:
            driver.get(driver.current_url + "&page=" + str(page))
        except:
            break

    for i in driver.find_elements_by_xpath('//*[@id="search"]/div[1]/div[2]/div/span[4]/div[1]'):
        counter = 0
        for element in i.find_elements_by_xpath('//div/div/div[2]/div[2]/div/div[2]/div[1]/div/div[1]/div/div/a'):
            should_add = True
            name = ""
            price = ""
            prev_price = ""
            link = ""
            try:
                name = i.find_elements_by_tag_name('h2')[counter].text
                price = element.find_element_by_class_name('a-price').text
                link = i.find_elements_by_xpath('//h2/a')[counter].get_attribute("href")
            except:
                print('exception')
                should_add = False 
            product = Product(name, price, prev_price, link)
            if should_add:
                products.append(product)
            counter = counter + 1
    page = page - 1
    if page == 0:
        break
    print(page)

run = 0



with open('products.json', 'w') as json_file:
    data = {}
    data["Products"] = []
    for prod in products:
        data["Products"].append(prod.serialize())
    json.dump(data, json_file, sort_keys=True, indent=4)



options = get_web_driver_options()
set_ignore_certificate_error(options)
driver = get_chrome_web_driver(options)
# driver.get(best_deal_product.link)
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')