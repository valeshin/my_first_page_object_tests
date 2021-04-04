from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def item_should_be_added_to_basket(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        message_item_added = self.browser.find_element(*ProductPageLocators.MESSAGE_ITEM_ADDED).text
        assert message_item_added == item_name, \
            f"The product {message_item_added} in the box is not equal to the added product {item_name}"

    def cost_of_basket_is_correct(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        message_cost_of_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_COST_OF_BASKET).text
        assert message_cost_of_basket == item_price, \
            f"The cost of basket {message_cost_of_basket} is not equal to the item_price {item_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_have_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message did not disappeared, but should have"
