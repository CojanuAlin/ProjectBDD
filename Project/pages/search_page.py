import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base_page import BasePage

class SearchBox(BasePage):
    ALLITEMSHAREA = (By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div/div/input')
    MYITEMSAREA = (By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div/div/input')
    EXTERNALITEMS = (By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div/div/input')
    SEARCHTAG = (By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/span[2]')

    def navigate_to_search_page(self):
        self.chrome.get('https://jules.app/search/all')

    def insert_search_all_items(self):
        self.chrome.find_element(*self.ALLITEMSHAREA).send_keys('something')
        self.chrome.find_element(*self.ALLITEMSHAREA).send_keys(Keys.ENTER)

    def insert_search_my_items(self):
        self.chrome.find_element(*self.MYITEMSAREA).send_keys('another')
        self.chrome.find_element(*self.MYITEMSAREA).send_keys(Keys.ENTER)

    def insert_search_external_items(self):
        self.chrome.find_element(*self.EXTERNALITEMS).send_keys('last')
        self.chrome.find_element(*self.EXTERNALITEMS).send_keys(Keys.ENTER)

    def check_search_item(self, message):
        actual_text = message
        expected_text = self.chrome.find_element(*self.SEARCHTAG).text
        assert actual_text == expected_text, 'Huston, we have a problem'

