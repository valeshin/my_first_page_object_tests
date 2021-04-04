from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Items are presented in basket, but should not be!"

    def should_be_message_text(self):
        assert self.is_element_present(*BasketPageLocators.INNER_CONTENT_TEXT) and \
               self.browser.find_element(*BasketPageLocators.INNER_CONTENT_TEXT).text, "Message text is not presented"
