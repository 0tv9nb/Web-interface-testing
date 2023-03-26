from pages.page_elements import MainPage


class TestTrial:
    def test_trial(self, driver):
        test_page = MainPage(driver, 'https://demoqa.com/')
        test_page.open()
        title = test_page.window_title_check()
        print(title)
