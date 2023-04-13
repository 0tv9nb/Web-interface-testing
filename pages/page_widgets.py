import time

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.locators_page_widgets import AccordianLocators, AutoCompleteLocators
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


class AutoCompletePage(BasePage):
    locator = AutoCompleteLocators()

    def color_input(self, in_type, num_colors=1):
        inputs = {
            'multiple': self.locator.MULTIPLE_COLOR_INPUT,
            'single': self.locator.SINGLE_COLOR_INPUT
        }
        colors_list = ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta",
                       "Aqua"]
        gen_color = next(generated_color(colors_list, num_colors))
        colors = gen_color.color
        multi_input = self.element_is_clickable(inputs[in_type])
        for color in colors:
            multi_input.send_keys(color[:2])
            time.sleep(1)
            multi_input.send_keys(Keys.ENTER)

