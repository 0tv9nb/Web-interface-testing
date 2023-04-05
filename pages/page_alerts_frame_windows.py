import time

from pages.base_page import BasePage
from locators.locators_page_alerts_frame_windows import BrowserWindowsLocators


class BrowserWindowsPage(BasePage):
    locator = BrowserWindowsLocators()

    def click_button(self, button):
        buttons = {
            "new_tab": self.locator.NEW_TAB,
            "new_window": self.locator.NEW_WINDOW,
            "new_window_message": self.locator.NEW_WINDOW_MESSAGE
        }
        self.element_is_visible(buttons[button]).click()
        time.sleep(2)
