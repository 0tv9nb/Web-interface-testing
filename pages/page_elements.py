import os
import random
import time
import requests as requests
from generator.generator import generated_data, generated_file
from locators.locators_page_elements import TextBoxLocators, CheckBoxLocators, RadioButtonLocators, WebTablesLocators, \
    ButtonsLocators, LinkLocators, UploadAndDownloadLocators
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
    locators = WebTablesLocators()

    def filling_out_the_form(self, count=2):
        data = []
        while count > 0:
            gen_data = next(generated_data())
            first_name = gen_data.first_name
            last_name = gen_data.last_name
            mail = gen_data.mail
            age = gen_data.age
            salary = gen_data.salary
            department = gen_data.department
            self.element_is_visible(self.locators.ADD_BUTTON).click()
            self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
            self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
            self.element_is_visible(self.locators.EMAIL).send_keys(mail)
            self.element_is_visible(self.locators.AGE).send_keys(age)
            self.element_is_visible(self.locators.SALARY).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
            count -= 1
            data.append([first_name, last_name, str(age), mail, str(salary), department])
        return data

    def table_data_output(self):
        table_data = self.element_are_presents(self.locators.ROW_DATA)
        data = []
        for i in table_data:
            data.append(i.text.splitlines())
        return data

    def table_search(self, data):
        search_name = data[random.randint(0, 5)]
        self.element_is_visible(self.locators.SEARCH).send_keys(search_name)

    def search_related_data(self):
        delete_button = self.element_is_visible(self.locators.DELETE)
        row = delete_button.find_element('xpath', self.locators.ROW_PERENTS)
        return row.text.splitlines()

    def update_data(self):
        self.element_is_visible(self.locators.EDIT).click()
        gen_data = next(generated_data())
        first_name = gen_data.first_name
        last_name = gen_data.last_name
        mail = gen_data.mail
        age = gen_data.age
        salary = gen_data.salary
        department = gen_data.department
        first_name_cl = self.element_is_visible(self.locators.FIRST_NAME)
        first_name_cl.clear()
        first_name_cl.send_keys(first_name)
        last_name_cl = self.element_is_visible(self.locators.LAST_NAME)
        last_name_cl.clear()
        last_name_cl.send_keys(last_name)
        mail_cl = self.element_is_visible(self.locators.EMAIL)
        mail_cl.clear()
        mail_cl.send_keys(mail)
        age_cl = self.element_is_visible(self.locators.AGE)
        age_cl.clear()
        age_cl.send_keys(age)
        salary_cl = self.element_is_visible(self.locators.SALARY)
        salary_cl.clear()
        salary_cl.send_keys(salary)
        department_cl = self.element_is_visible(self.locators.DEPARTMENT)
        department_cl.clear()
        department_cl.send_keys(department)
        self.element_is_visible(self.locators.SUBMIT_BUTTON).click()
        return [first_name, last_name, str(age), mail, str(salary), department]

    def delete_data(self):
        self.element_is_visible(self.locators.DELETE).click()
        deletion_messages = self.element_is_visible(self.locators.NO_DATA).text
        return deletion_messages

    def choose_number_of_rows(self, lis):
        numbers_row = []
        for i in lis:
            self.option_select(f"{i} rows", self.locators.SELECT_LIST)
            lines = self.element_are_visible(self.locators.ROW_DATA)
            numbers_row.append(len(lines))
        return numbers_row


class ButtonsPage(BasePage):
    locators = ButtonsLocators()

    def button_clicks(self):
        buttons = self.element_are_visible(self.locators.BUTTONS)
        self.action_double_click(buttons[0])
        self.action_right_click(buttons[1])
        buttons[2].click()

    def message_on_click(self):
        double_click_messege = self.element_is_visible(self.locators.DOUBLE_CLICK_MESSAGE).text
        right_click_messege = self.element_is_visible(self.locators.RIGHT_CLICK_MESSAGE).text
        click_messege = self.element_is_visible(self.locators.CLICK_MESSAGE).text
        return [double_click_messege, right_click_messege, click_messege]


class LinksPage(BasePage):
    locators = LinkLocators()

    def check_new_tab_simple_link(self):
        simpl_link = self.element_is_visible(self.locators.SIMPLE_LINK)
        link_href = simpl_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simpl_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            self.element_are_visible(self.locators.TEST)[0].click()
            time.sleep(5)
            return link_href, url
        else:
            return link_href, request.status_code

    def check_new_tab_bed_request(self, url):
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_visible(self.locators.BAD_REQUEST).click()
        else:
            return request.status_code


class UploadAndDownloadPage(BasePage):
    locators = UploadAndDownloadLocators()

    def upload_file(self):
        file_name, path = generated_file()
        self.element_is_visible(self.locators.UPLOAD_FILE).send_keys(path)
        time.sleep(2)
        os.remove(path)
        upload_name = self.element_is_visible(self.locators.UPLOAD_INFA).text
        return file_name.split('\\')[-1], upload_name.split('\\')[-1]
