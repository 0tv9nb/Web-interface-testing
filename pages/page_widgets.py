import time

from locators.locators_page_widgets import AccordianLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locator = AccordianLocators()

    def checking_the_accordion(self):
        section_first = self.element_is_visible(self.locator.SECTION_HEADING_FIRST)
        # section_first.click()
        print(section_first.text)
        text_first = self.element_is_visible(self.locator.SECTION_CONTENT_FIRST).text
        print(text_first)
        time.sleep(2)
        section_second = self.element_is_visible(self.locator.SECTION_HEADING_SECOND)
        section_second.click()
        print(section_second.text)
        text_first = self.element_is_visible(self.locator.SECTION_CONTENT_SECOND).text
        print(text_first)
        time.sleep(2)
        section_third = self.element_is_visible(self.locator.SECTION_HEADING_THIRD)
        section_third.click()
        print(section_third.text)
        text_first = self.element_is_visible(self.locator.SECTION_CONTENT_THIRD).text
        print(text_first)
        time.sleep(2)

