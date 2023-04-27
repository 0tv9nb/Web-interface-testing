import time

from locators.locators_page_interactions import SortableLocators
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
        self.swap_elements(item[0], item[1])
        after = self.sequence_of_elements(item)
        return before, after

    def sequence_of_elements(self, item):
        sequence = []
        for i in item:
            sequence.append(i.text)
        return sequence
