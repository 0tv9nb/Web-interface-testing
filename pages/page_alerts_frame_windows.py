import time

from generator.generator import generated_data
from pages.base_page import BasePage
from locators.locators_page_alerts_frame_windows import BrowserWindowsLocators, AlertsLocators, FramesLocators


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
            "promt_button": self.locator.PROMT_BUTTON,
        }
        self.element_is_visible(buttons[button]).click()

    def get_text_alert(self):
        alert = self.switch_to_alert(timeout=10)
        alert_text = alert.text
        alert.accept()
        return alert_text

    def accept_or_close_alert(self, option):
        alert = self.switch_to_alert()
        if option == "Ok":
            alert.accept()
        else:
            alert.dismiss()

    def get_message_from_alert(self, message):
        messages = {
            "confirm_btn_msg": self.locator.CONFIRM_BUTTON_MESSAGE,
            "promt_btn_msg": self.locator.PROMT_BUTTON_MESSAGE,
        }
        return self.element_is_visible(messages[message]).text.split(' ')[-1]

    def checking_prompt_alert(self):
        name = next(generated_data()).first_name
        alert = self.switch_to_alert()
        alert.send_keys(name)
        alert.accept()
        return name


class FramesPage(BasePage):
    locator = FramesLocators()

    def jump_to_frame(self, frame):
        frames = {
            "big_frame": self.locator.BIG_FRAME,
            "smol_frame": self.locator.SMOL_FRAME,
        }
        frame_switch = self.element_is_visible(frames[frame])
        frame_height = frame_switch.get_attribute('height')
        frame_width = frame_switch.get_attribute('width')
        self.switch_to_frame(frame_switch)
        frame_text = self.element_is_visible(self.locator.FRAME_TEXT).text
        self.switch_to_start_window()
        return [frame_text, frame_width, frame_height]
