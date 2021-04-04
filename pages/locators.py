from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn")


class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    INNER_CONTENT_TEXT = (By.CSS_SELECTOR, "#content_inner p")


class LoginPagesLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class MainPageLocators():
    pass


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    MESSAGE_ITEM_ADDED = (By.CSS_SELECTOR, ".alert-success:nth-child(1) strong")
    MESSAGE_COST_OF_BASKET = (By.CSS_SELECTOR, ".alert-info strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
