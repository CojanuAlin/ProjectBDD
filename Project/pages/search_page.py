from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base_page import BasePage

class SearchBox(BasePage):
    SEARCHAREA = (By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div/div/input')
    SEARCHTAG = (By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/span[2]')

    def navigate_to_search_page(self):
        self.chrome.get('https://jules.app/search/all')

    def insert_search(self, something):
        self.chrome.find_element(*self.SEARCHAREA).send_keys(something)
        self.chrome.find_element(*self.SEARCHAREA).send_keys(Keys.ENTER)

    def check_search_item(self, something):
        actual_text = something
        expected_text = self.chrome.find_element(*self.SEARCHTAG).text
        assert actual_text == expected_text, 'Huston, we have a problem'