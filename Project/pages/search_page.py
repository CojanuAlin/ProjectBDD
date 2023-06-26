import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from base_page import BasePage


class SearchBox(BasePage):
    PAGETITLE = (By.XPATH, '//*[@class="css-1h5x3dy"]')
    ALLITEMSAREA = (By.XPATH, '//*[@class="MuiInputBase-input MuiInput-input"]')
    SEARCHTAG = (By.XPATH, '//*[@id="root"]/div[1]/div[3]/div/div[3]/div[2]/div[2]/div/div/div[1]/div/span[2]')
    NOTIFBELL = (By.XPATH, '//*[@class="css-mhea7a"][1]')
    NOTIFMESSAGE = (By.XPATH, '//*[@class="css-fmd18w"]/span[2]')
    NOTIFSETTINGS = (By.CSS_SELECTOR, '[data-test-id="notifications-settings-tab"]')
    NOTIFSLIDER = (By.XPATH, '//*[@class="MuiTypography-root MuiFormControlLabel-label MuiTypography-body1"]')
    NOTIFERROR = (By.XPATH, '//*[@id="client-snackbar"]/div/div/span')
    QUESTIONMARK = (By.XPATH, '//*[@class="css-mhea7a"][2]')
    QUESTIONMARKLIST = (By.XPATH, '//*[@id="menu-list-grow"]/a')
    MYACCOUNT = (By.XPATH, '//*[@id="menu-list-grow"]/div[1]/li/span[1]')
    PHONEAREA = (By.CSS_SELECTOR, 'a[href^="tel"]')

    def login_to_desired_page(self):
        self.chrome.get('https://jules.app/sign-in')
        user = self.chrome.find_element(*self.USERNAME)
        user.send_keys('alin_nicusor@outlook.com')
        password = self.chrome.find_element(*self.PASSWORD)
        password.send_keys('Digital1!')
        self.chrome.find_element(*self.LOGIN).click()

    def check_login(self):
        actual = 'The C Household'
        expected = self.chrome.find_element(*self.PAGETITLE).text
        assert actual == expected, 'Not the actual message'

    def navigate_to_search_page(self):
        self.chrome.get('https://jules.app/search/all')

    def insert_search_all_items(self):
        self.chrome.find_element(*self.ALLITEMSAREA).send_keys('something')
        self.chrome.find_element(*self.ALLITEMSAREA).send_keys(Keys.ENTER)

    def insert_search_my_items(self):
        self.chrome.get('https://jules.app/search/internal')
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
        element = self.chrome.find_element(*self.NOTIFERROR)
        actual = element.text
        expected = notif_message
        assert actual == expected, "Text doesn't match!"

    def click_question_mark(self):
        self.chrome.find_element(*self.QUESTIONMARK).click()

    def select_question_mark_item(self, question_item):
        item_list = self.chrome.find_elements(*self.QUESTIONMARKLIST)
        for i in item_list:
            if i.text == question_item:
                i.click()
            else:
                continue
        time.sleep(2)

    def check_question_item_url(self, question_url):
        self.chrome.switch_to.window(self.chrome.window_handles[-1])
        actual = self.chrome.current_url
        expected = question_url
        assert actual == expected, f"{actual}"

    def select_my_account(self):
        self.chrome.find_element(*self.PERSONICON).click()
        self.chrome.find_element(*self.MYACCOUNT).click()

    def check_phone(self):
        actual = self.chrome.find_element(*self.PHONEAREA).text
        expected = '1234567890'
        assert actual == expected, 'Wrong phone number'

