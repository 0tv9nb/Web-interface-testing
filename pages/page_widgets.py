import time

from selenium.common import TimeoutException

from locators.locators_page_widgets import AccordianLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locator = AccordianLocators()

    def checking_section_accordion(self, section):
        sections = {
            'first': {
                'element': self.locator.SECTION_HEADING_FIRST,
                'text': self.locator.SECTION_CONTENT_FIRST
            },
            'second': {
                'element': self.locator.SECTION_HEADING_SECOND,
                'text': self.locator.SECTION_CONTENT_SECOND
            },
            'third': {
                'element': self.locator.SECTION_HEADING_THIRD,
                'text': self.locator.SECTION_CONTENT_THIRD
            },
        }
        section_head = self.element_is_visible(sections[section]['element'])
        section_head.click()
        title = section_head.text
        try:
            content_text = self.element_is_visible(sections[section]['text'], 8).text
        except TimeoutException:
            section_head.click()
            content_text = self.element_is_visible(sections[section]['text'], 8).text
        return [title, len(content_text)]
