from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.user_suit
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "qwertasdfg12"
        login_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        login_page = LoginPage(browser, login_link)
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.item_should_be_added_to_basket()
        page.cost_of_basket_is_correct()


@pytest.mark.need_review
@pytest.mark.parametrize('number',
                         ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, number):
    promo_link = f"{link}?promo=offer{number}"
    page = ProductPage(browser, promo_link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.item_should_be_added_to_basket()
    page.cost_of_basket_is_correct()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.success_message_should_have_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items()
    basket_page.should_be_message_text()
