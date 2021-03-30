from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def goods_should_be_added_to_basket(self):
        goods_name = self.browser.find_element(*ProductPageLocators.GOODS_NAME).text
        message_goods_added = self.browser.find_element(*ProductPageLocators.MESSAGE_GOODS_ADDED).text
        assert message_goods_added == goods_name, \
            f"The product {message_goods_added} in the box is not equal to the added product {goods_name}"

    def cost_of_basket_is_correct(self):
        goods_price = self.browser.find_element(*ProductPageLocators.GOODS_PRICE).text
        message_cost_of_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_COST_OF_BASKET).text
        assert message_cost_of_basket == goods_price, \
            f"The cost of basket {message_cost_of_basket} is not equal to the goods_price {goods_price}"
