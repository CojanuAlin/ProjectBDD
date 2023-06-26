from browser import Browser
from selenium.webdriver.common.by import By

class BasePage(Browser):

    USERNAME = (By.CSS_SELECTOR, '[placeholder="Enter your email"]')
    PASSWORD = (By.CSS_SELECTOR, '[placeholder="Enter your password"]')
    LOGIN = (By.XPATH, '//*[@class="MuiButton-label"]')
    PERSONICON = (By.XPATH, '//*[@class="css-mhea7a"][3]')

