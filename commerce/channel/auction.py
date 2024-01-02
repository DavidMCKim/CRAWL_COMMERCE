from lib2to3.pgen2 import driver
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


class Auction():
    def __init__(self, channel_code, channel_name, placement, url) -> None:
        self.channel_code = channel_code
        self.channel_name = channel_name
        self.placement    = placement
        self.url          = url

        self.options = webdriver.ChromeOptions()
        service = ChromeService(executable_path='')
        driver = webdriver.Chrome(service=service, options=self.options)
        self.driver       = driver
    
    def crawl_auction():
        pass