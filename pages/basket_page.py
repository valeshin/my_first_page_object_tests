from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Items are presented in basket, but should not be!"

    def should_be_basket_empty_text(self):
        inner_content_text = self.browser.find_element(*BasketPageLocators.INNER_CONTENT_TEXT).text
        assert "Your basket is empty." in inner_content_text, 'Text "Your basket is empty" is not presented'
