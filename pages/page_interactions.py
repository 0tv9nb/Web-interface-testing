import time

from locators.locators_page_interactions import SortableLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locator = SortableLocators()

    def mixing_elements(self):
        self.element_is_visible(self.locator.TAB_LIST).click()
        item_list = self.element_are_visible(self.locator.ITEM_LIST)
        self.swap_elements(item_list[0], item_list[1])
        self.element_is_visible(self.locator.TAB_GRID).click()
        item_grid = self.element_are_visible(self.locator.ITEM_GRID)
        self.swap_elements(item_grid[0], item_grid[1])
