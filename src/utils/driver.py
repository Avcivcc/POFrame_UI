"""获取驱动"""
from selenium import webdriver


class Driver:

    def get_chrome_driver(self):
        driver_chrome = webdriver.Chrome()
        return driver_chrome

    def get_firefox_driver(self):
        driver_firefox = webdriver.Firefox()
        return driver_firefox

    def get_IE_driver(self):
        driver_ie = webdriver.Ie()
        return driver_ie
