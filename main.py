from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = 'http://www.bezfrazi.cz'
webdriver_path = '/home/kijifa/PycharmProjects/chromedriver'


def main():

    browser = open_browser(url,webdriver_path)
    browser.get(url)
    #browser.find_element_by_id('read-next-button').click()
    #i = 0
    #while i < 2:
    #    browser.find_element_by_id('read-next-button').click()
    #    i =+ 1

    a=[]
    a = browser.find_elements_by_xpath("//*[@class='post-header']/ancestor::a")
    print(a)


    browser.close()

    return


def open_browser(url, webdriver_path):
    driver = webdriver.Chrome(executable_path=webdriver_path)

    return driver


def click_next():

    return


if __name__ == '__main__':
    main()
