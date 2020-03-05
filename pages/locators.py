from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_URL = (By.CSS_SELECTOR, "div.container-fluid.page > div > ul > li.active")
    LOGIN_FORM = (By.ID, "#login_form")
    REGISTER_FORM = (By.ID, "#register_form")