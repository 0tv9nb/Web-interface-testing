import time

from pages.page_elements import MainPage, TextBoxPage, CheckBoxPage


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
