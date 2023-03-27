from generator.generator import generated_data
from locators.locators_page_elements import TextBoxLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    ''' First test, checked the work '''

    def window_title_check(self):
        window_title = self.driver.title
        return window_title


class TextBoxPage(BasePage):
    locators = TextBoxLocators()

    def filling_text_fields(self):
        gen_data=next(generated_data())
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
