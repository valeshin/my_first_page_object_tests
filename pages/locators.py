from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    pass


class LoginPagesLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    GOODS_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    GOODS_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    MESSAGE_GOODS_ADDED = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    MESSAGE_COST_OF_BASKET = (By.CSS_SELECTOR, ".alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
