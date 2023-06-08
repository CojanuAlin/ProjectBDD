import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base_page import BasePage


class SearchBox(BasePage):
    ALLITEMSAREA = (By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div/div/input')
    SEARCHTAG = (By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/span[2]')
    NOTIFBELL = (By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div[2]/div[1]/div')
    NOTIFMESSAGE = (By.XPATH, '//*[@id="root"]/div[5]/div[2]/div[2]/span[2]')
    NOTIFSETTINGS = (By.XPATH, '//*[@id="root"]/div[5]/div[2]/div[3]/div[1]/div/div/div/button[2]/span[1]/div')
    NOTIFSLIDER = (By.XPATH, '//*[@class="MuiTypography-root MuiFormControlLabel-label MuiTypography-body1"]')
    NOTIFERROR = (By.XPATH, '//*[@id="client-snackbar"]/div')

    def login_to_desired_page(self):
        self.chrome.get('https://jules.app/sign-in')
        user = self.chrome.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[1]/div/div/input')
        user.send_keys('alin_nicusor@outlook.com')
        password = self.chrome.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[2]/div/div/input')
        password.send_keys('Digital1!')
        self.chrome.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[3]/button/span[1]').click()

    def check_login(self):
        actual = 'The Cojanu Household'
        expected = self.chrome.find_element(By.XPATH, '//*[@id="root"]/div[1]/div[1]/div/div[1]/span/span').text
        assert actual == expected, 'Not the actual message'

    def navigate_to_search_page(self):
        self.chrome.get('https://jules.app/search/all')

    def insert_search_all_items(self):
        self.chrome.find_element(*self.ALLITEMSAREA).send_keys('something')
        self.chrome.find_element(*self.ALLITEMSAREA).send_keys(Keys.ENTER)

    def insert_search_my_items(self):
        self.chrome.find_element(*self.ALLITEMSAREA).send_keys('another')
        self.chrome.find_element(*self.ALLITEMSAREA).send_keys(Keys.ENTER)

    def insert_search_external_items(self):
        self.chrome.get('https://jules.app/search/external')
        self.chrome.find_element(*self.ALLITEMSAREA).send_keys('last')
        self.chrome.find_element(*self.ALLITEMSAREA).send_keys(Keys.ENTER)

    def check_search_item(self, message):
        actual_text = message
        expected_text = self.chrome.find_element(*self.SEARCHTAG).text
        assert actual_text == expected_text, 'Huston, we have a problem'

    def access_notification_bell(self):
        self.chrome.find_element(*self.NOTIFBELL).click()
        time.sleep(1)

    def check_notif_message(self):
        actual = 'From here you can manage your account notifications.'
        expected = self.chrome.find_element(*self.NOTIFMESSAGE).text
        assert actual == expected, 'Is not the actual message'

    def click_notification(self, notif_name):
        self.chrome.find_element(*self.NOTIFBELL).click()
        time.sleep(1)
        self.chrome.find_element(*self.NOTIFSETTINGS).click()
        time.sleep(1)
        notification = self.chrome.find_elements(*self.NOTIFSLIDER)
        for i in range(0, 10):
            if notification[i].text == notif_name:
                notification[i].click()
                time.sleep(1)
            else:
                continue

    def check_disabled_message(self, notif_message):
        actual = self.chrome.find_element(*self.NOTIFERROR).text
        expected = notif_message
        assert actual == expected, 'Is not disabled'

