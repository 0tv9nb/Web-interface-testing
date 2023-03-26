import time

from pages.page_elements import MainPage, TextBoxPage


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
        time.sleep(5)
        print(data)
