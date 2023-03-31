import random

from generator.generator import generated_data
from locators.locators_page_elements import TextBoxLocators, CheckBoxLocators, RadioButtonLocators, WebTablesLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    """First test, checked the work """

    def window_title_check(self):
        window_title = self.driver.title
        return window_title


class TextBoxPage(BasePage):
    locators = TextBoxLocators()

    def filling_text_fields(self):
        gen_data = next(generated_data())
        full_name = gen_data.full_name
        mail = gen_data.mail
        current_address = gen_data.current_address
        permanent_address = gen_data.permanent_address
        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(mail)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        self.element_is_visible(self.locators.SUBMIT).click()
        return [full_name, mail, current_address, permanent_address]

    def getting_output(self):
        output_data = self.element_is_visible(self.locators.OUTPUT).text
        data = output_data.split('\n')
        return [i.split(':')[1] for i in data]


class CheckBoxPage(BasePage):
    locators = CheckBoxLocators()

    def reveal_all_check_box(self):
        self.element_is_visible(self.locators.EXPAND_ALL).click()

    def hide_all_check_box(self):
        self.element_is_visible(self.locators.COLLAPSE_ALL).click()

    def number_of_check_box(self):
        active_check_box = self.element_are_visible(self.locators.CHECK_BOX_LIST)
        return len(active_check_box)

    def click_random_check_box(self):
        check_box_list = self.element_are_visible(self.locators.CHECK_BOX_LIST)
        i = 21
        while i != 0:
            check_box = check_box_list[random.randint(0, 16)]
            check_box.click()
            i -= 1

    def getting_output(self):
        result = self.element_is_visible(self.locators.RESULT).text
        return str(result.lower().split('\n')[1:]).replace(' ', '')

    def search_for_active_check_box(self):
        active_list = []
        active_check_box = self.element_are_visible(self.locators.ACTIVE_CHECK_BOX)
        for box in active_check_box:
            active_box = box.find_element("xpath", self.locators.ANCESTOR_ACTIVE_CHECK_BOX)
            active_list.append(active_box.text)
        return str(active_list).lower().replace(' ', '').replace('.doc', '')


class RadioButtonPage(BasePage):
    locators = RadioButtonLocators()

    def check_radio_button(self, like):
        likes = {'Yes': self.locators.RADIO_YES,
                 "Impressive": self.locators.RADIO_IMPRESSIVE,
                 "No": self.locators.RADIO_NO
                 }
        self.element_is_visible(likes[like]).click()

    def getting_output(self):
        return self.element_is_visible(self.locators.OUTPUT_SELECTED).text

class WebTablesPage(BasePage):
    locators=WebTablesLocators()
    def filling_out_the_form(self):
        self.element_is_visible(self.locators.ADD_BUTTON).click()
        self.element_is_visible(self.locators.FIRST_NAME).send_keys('Sasha')
        self.element_is_visible(self.locators.LAST_NAME).send_keys('Aga')
        self.element_is_visible(self.locators.EMAIL).send_keys('aga@mail.ru')
        self.element_is_visible(self.locators.AGE).send_keys(12)
        self.element_is_visible(self.locators.SALARY).send_keys(111)
        self.element_is_visible(self.locators.DEPARTMENT).send_keys('doctor')
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()