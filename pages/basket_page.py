from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()

    def basket_do_not_have_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_HAVE_PRODUCT), "Basket don't have a product"

    def basket_have_text_about_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_IS_EMPTY), "Basket don't have a text about empty"
