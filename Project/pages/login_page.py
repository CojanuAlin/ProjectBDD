from selenium.webdriver.common.by import By

from base_page import BasePage


class LoginPage(BasePage):

    ERROR = (By.ID, 'client-snackbar')
    NO_USER = (By.CSS_SELECTOR, 'div p')
    LOGOUT = (By.CSS_SELECTOR, '[data-test-id="logout-option-business"]')
    LOGOUTCONFIRM = (By.CSS_SELECTOR, '[data-test-id="confirm-logout-button"]')

    def navigate_to_login_page(self):
        self.chrome.get('https://jules.app')

    def insert_username(self, username):
        self.chrome.find_element(*self.USERNAME).send_keys(username)

    def insert_password(self, password):
        self.chrome.find_element(*self.PASSWORD).send_keys(password)

    def click_login_button(self):
        self.chrome.find_element(*self.LOGIN).click()

    def loged_in_page(self):
        expected_link = 'https://jules.app/search/all'
        actual_link = self.chrome.current_url
        assert actual_link == expected_link, 'Nu sunt pe pagina potrivita!!'

    def check_error_message(self, error_message):
        expected_error_message = error_message
        actual_error_message = self.chrome.find_element(*self.ERROR).text
        assert expected_error_message == actual_error_message, 'Nu sunt aceleasi erori!'

    def no_user_error(self, no_user):
        expected_no_user_error = no_user
        actual_error_no_user = self.chrome.find_element(*self.NO_USER).text
        assert actual_error_no_user == expected_no_user_error, 'Avem alta eroare!'

    def logout(self):
        self.chrome.find_element(*self.PERSONICON).click()
        self.chrome.find_element(*self.LOGOUT).click()
        self.chrome.find_element(*self.LOGOUTCONFIRM).click()

    def insert_credentials(self):
        self.chrome.find_element(*self.USERNAME).send_keys('alin_nicusor@outlook.com')
        self.chrome.find_element(*self.PASSWORD).send_keys('Digital1!')
        self.chrome.find_element(*self.LOGIN).click()

    def loged_out_page(self):
        expected_link = 'https://jules.app/sign-in'
        actual_link = self.chrome.current_url
        assert actual_link == expected_link, 'Nu sunt pe pagina de login!!'

