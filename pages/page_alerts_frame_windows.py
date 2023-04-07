import time

from pages.base_page import BasePage
from locators.locators_page_alerts_frame_windows import BrowserWindowsLocators, AlertsLocators


class BrowserWindowsPage(BasePage):
    locator = BrowserWindowsLocators()

    def click_button(self, button):
        buttons = {
            "new_tab": self.locator.NEW_TAB,
            "new_window": self.locator.NEW_WINDOW,
            "new_window_message": self.locator.NEW_WINDOW_MESSAGE,
        }
        self.element_is_visible(buttons[button]).click()
        time.sleep(2)

    def checking_transition_to_new_window(self, num_windows=2):
        self.switch_to_new_window(num_windows)

        url = self.url_comparison('https://demoqa.com/sample')
        self.switch_to_start_window()
        return url


class AlertsPage(BasePage):
    locator = AlertsLocators()

    def click_button(self, button):
        buttons = {
            "alert_button": self.locator.ALERT_BUTTON,
            "timer_alert_button": self.locator.TIMER_ALERT_BUTTON,
            "confirm_button": self.locator.CONFIRM_BUTTON,
            "promt_button": self.locator.PROMT_BUTTON_MESSAGE,
        }
        self.element_is_visible(buttons[button]).click()
        time.sleep(2)

    def get_text_alert(self):
        alert = self.switch_to_alert()
        alert_text = alert.text
        alert.accept()
        print(alert_text)
        return alert_text


