import random
import time

from pages.page_elements import MainPage, TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage


class TestTrial:
    def test_trial(self, driver):
        test_page = MainPage(driver, 'https://demoqa.com/')
        test_page.open()
        title = test_page.window_title_check()
        assert title == 'DEMOQA', 'wrong page'


class TestTextBox:
    def test_text_box(self, driver):
        text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box')
        text_box_page.open()
        data = text_box_page.filling_text_fields()
        output_data = text_box_page.getting_output()
        assert data == output_data, 'input does not match output'


class TestCheckBox:
    def test_expand_collaps_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        check_box_page.reveal_all_check_box()
        expand_check_box = check_box_page.number_of_check_box()
        check_box_page.hide_all_check_box()
        collaps_check_box = check_box_page.number_of_check_box()
        print(expand_check_box, collaps_check_box)
        assert expand_check_box == 17, 'not all checkboxes are open'
        assert collaps_check_box == 1, 'not all checkboxes are hidden'

    def test_check_box(self, driver):
        check_box_page = CheckBoxPage(driver, 'https://demoqa.com/checkbox')
        check_box_page.open()
        check_box_page.reveal_all_check_box()
        check_box_page.click_random_check_box()
        selected_check_box = check_box_page.getting_output()
        active_check_box = check_box_page.search_for_active_check_box()
        assert selected_check_box == active_check_box, 'not all active checkboxes are displayed'


class TestRadioButton:
    def test_radio_button(self, driver):
        radio_button_page = RadioButtonPage(driver, 'https://demoqa.com/radio-button')
        radio_button_page.open()
        radio_button_page.check_radio_button('Yes')
        output_yes = radio_button_page.getting_output()
        radio_button_page.check_radio_button('Impressive')
        output_impressive = radio_button_page.getting_output()
        radio_button_page.check_radio_button('No')
        output_no = radio_button_page.getting_output()
        assert output_yes == 'Yes', 'Yes, is not pressed'
        assert output_impressive == 'Impressive', 'Impressive, is not pressed'
        assert output_no == 'No', 'No, is not pressed'


class TestWebTables:
    def test_adding_record_to_table(self, driver):
        web_table_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        input_data = web_table_page.filling_out_the_form(1)
        output_data = web_table_page.table_data_output()
        for i in input_data:
            assert i in output_data, 'there is no entered data in the table'

    def test_search_function(self, driver):
        web_table_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        input_data = web_table_page.filling_out_the_form(1)
        data = input_data[random.randint(0, len(input_data) - 1)]
        web_table_page.table_search(data)
        output_data = web_table_page.search_related_data()
        assert data == output_data, 'search is not working properly'

    def test_updating_data_in_a_table(self,driver):
        web_table_page = WebTablesPage(driver, 'https://demoqa.com/webtables')
        web_table_page.open()
        updat_data=web_table_page.update_data()
        output_data = web_table_page.table_data_output()
        print(output_data)
        print(updat_data)
        assert updat_data in output_data, 'data has not been changed'