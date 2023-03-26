from pages.base_page import BasePage


class MainPage(BasePage):
    ''' First test, checked the work '''

    def window_title_check(self):
        window_title = self.driver.title
        return window_title
