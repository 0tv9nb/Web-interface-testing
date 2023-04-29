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

    def interaction_with_elements(self):
        self.element_is_visible(self.locator.TAB_LIST).click()
        list_item = self.element_are_visible(self.locator.LIST_CONTAINER)
        for i in list_item:
            i.click()
            time.sleep(1)
        self.element_is_visible(self.locator.TAB_GRID).click()
        grid_item = self.element_are_visible(self.locator.GRID_CONTAINER)
        for j in grid_item:
            j.click()
            time.sleep(1)
