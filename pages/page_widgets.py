import time
from datetime import datetime

from selenium.common import TimeoutException
from selenium.webdriver import Keys

from generator.generator import generated_color
from locators.locators_page_widgets import AccordianLocators, AutoCompleteLocators, DatePickerLocators
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
            multi_input.send_keys(color[:3])
            multi_input.send_keys(Keys.ENTER)
        return colors

    def checking_entered_colors(self, in_type):
        output_values = {
            'multiple': self.locator.ENTERED_MULTI_COLOR,
            'single': self.locator.ENTERED_SINGLE_COLOR
        }
        colors_list = []
        try:
            colors = self.element_are_visible(output_values[in_type])
        except TimeoutException:
            return colors_list
        for color in colors:
            colors_list.append(color.text)
        return colors_list

    def clear_input_field(self, in_type):
        remove_buttons = self.element_are_presents(self.locator.REMOVE_BUTTON)
        remove_buttons[in_type].click()

    def remove_color(self):
        colors = self.element_are_visible(self.locator.REMOVE_COLOR)
        for color in colors:
            color.click()
            break


class DatePickerPage(BasePage):
    locator = DatePickerLocators()

    def getting_date(self, element):
        elements = {
            'date': self.locator.SELECT_DATE_INPUT,
            'date_time': self.locator.DATE_AND_TIME
        }
        get_data = self.element_is_presents(elements[element]).get_attribute('value')
        return get_data

    def current_date(self):
        now = datetime.now()
        return now.strftime('%m/%d/%Y')

    def current_date_with_time(self):
        now = datetime.now()
        hour = now.strftime(f'%I')
        if int(hour) < 10:
            hour = hour.replace('0', '')
        return f"{now.strftime(f'%B %d, %Y ')}{hour}"

    def data_entry_in_select_date(self):
        day = 29
        month = 'May'
        year = '2022'
        self.element_is_visible(self.locator.SELECT_DATE_INPUT).click()
        self.option_select(month, self.locator.SELECT_DATE_MONTH)
        time.sleep(3)
        self.option_select(year, self.locator.SELECT_DATE_YEAR)
        time.sleep(3)
        locat = (
            "css selector", f"div[class^='react-datepicker__day react-datepicker__day--0{day}'][aria-label~='{month}']")
        self.element_is_visible(locat).click()
        time.sleep(3)
        month = self.convert_month_to_number(month)
        return f'{month}/{day}/{year}'

    @staticmethod
    def convert_month_to_number(month):
        months = {
            "January": '01',
            "February": '02',
            "March": '03',
            "April": '04',
            "May": '05',
            "June": '06',
            "July": '07',
            "August": '08',
            "September": '09',
            "October": '10',
            "November": '11',
            "December": '12',
        }
        return months[month]
