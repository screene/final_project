from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time

#def test_guest_can_add_product_to_basket(browser):
#    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#    page = ProductPage(browser, url)
#    page.open()
#    page.add_in_basket()
#    page.solve_quiz_and_get_code()

#def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#    page = ProductPage(browser, url)
#    page.open()
#    page.add_in_basket()
#    page.should_not_be_success_message()

#def test_guest_cant_see_success_message(browser):
#    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#    page = ProductPage(browser, url)
#    page.open()
#    page.should_not_be_success_message()

#def test_message_disappeared_after_adding_product_to_basket(browser):
#    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#    page = ProductPage(browser, url)
#    page.open()
#    page.add_in_basket()
#    page.should_disappeared_message()

#def test_guest_should_see_login_link_on_product_page(browser):
#    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page = ProductPage(browser, url)
#    page.open()
#    page.should_be_login_link()

#def test_guest_can_go_to_login_page_from_product_page(browser):
#    url = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#    page = ProductPage(browser, url)
#    page.open()
#    page.go_to_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    url = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, url)
    page.open()
    page.go_to_basket_page()
    page.basket_do_not_have_product()
    page.basket_have_text_about_empty()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = BasketPage(browser, url)
    page.open()
    page.go_to_basket_page()
    page.basket_do_not_have_product()
    page.basket_have_text_about_empty()

