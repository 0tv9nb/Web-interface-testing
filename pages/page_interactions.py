import time
import random

from locators.locators_page_interactions import SortableLocators, SelectableLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locator = SortableLocators()

    def mixing_elements(self, element):
        elements = {
            'list': {
                'tab': self.locator.TAB_LIST,
                'item': self.locator.ITEM_LIST
            },
            'grid': {
                'tab': self.locator.TAB_GRID,
                'item': self.locator.ITEM_GRID
            },
        }
        self.element_is_visible(elements[element]['tab']).click()
        item = self.element_are_visible(elements[element]['item'])
        before = self.sequence_of_elements(item)

        nums = random.sample(item, 2)
        self.swap_elements(nums[0], nums[1])
        after = self.sequence_of_elements(item)
        return before, after

    def sequence_of_elements(self, item):
        sequence = []
        for i in item:
            sequence.append(i.text)
        return sequence


class SelectablePage(BasePage):
    locator = SelectableLocators()

    def interaction_with_elements(self, element):
        elements = {
            'list': {
                'tab': self.locator.TAB_LIST,
                'item': self.locator.LIST_CONTAINER,
                'active_item': self.locator.LIST_ITEM_ACTION,
            },
            'grid': {
                'tab': self.locator.TAB_GRID,
                'item': self.locator.GRID_CONTAINER,
                'active_item': self.locator.GRID_ITEM_ACTION,
            },
        }
        self.element_is_visible(elements[element]['tab']).click()
        list_item = self.element_are_visible(elements[element]['item'])
        number_of_clicks = self.element_activation(list_item)
        active_item = self.element_are_visible(elements[element]['active_item'])
        return number_of_clicks, len(active_item)

    def element_activation(self, lis):
        amount_elements = random.randint(1, len(lis))
        active_list = random.sample(lis, amount_elements)
        for item in active_list:
            item.click()
        return amount_elements
