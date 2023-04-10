import time

import allure

from generator.generator import generated_data
from pages.base_page import BasePage
from locators.locators_page_alerts_frame_windows import BrowserWindowsLocators, AlertsLocators, FramesLocators, \
    NestedFramesLocators, ModalDialogsLocators


class BrowserWindowsPage(BasePage):
    locator = BrowserWindowsLocators()

    @allure.step('click button')
    def click_button(self, button):
        buttons = {
            "new_tab": self.locator.NEW_TAB,
            "new_window": self.locator.NEW_WINDOW,
            "new_window_message": self.locator.NEW_WINDOW_MESSAGE,
        }
        self.element_is_visible(buttons[button]).click()
        time.sleep(2)

    @allure.step('checking transition to new window')
    def checking_transition_to_new_window(self, num_windows=2):
        self.switch_to_new_window(num_windows)

        url = self.url_comparison('https://demoqa.com/sample')
        self.switch_to_start_window()
        return url


class AlertsPage(BasePage):
    locator = AlertsLocators()

    @allure.step('click button')
    def click_button(self, button):
        buttons = {
            "alert_button": self.locator.ALERT_BUTTON,
            "timer_alert_button": self.locator.TIMER_ALERT_BUTTON,
            "confirm_button": self.locator.CONFIRM_BUTTON,
            "promt_button": self.locator.PROMT_BUTTON,
        }
        self.element_is_visible(buttons[button]).click()

    @allure.step('get text alert')
    def get_text_alert(self):
        alert = self.switch_to_alert(timeout=10)
        alert_text = alert.text
        alert.accept()
        return alert_text

    @allure.step('accept or close alert')
    def accept_or_close_alert(self, option):
        alert = self.switch_to_alert()
        if option == "Ok":
            alert.accept()
        else:
            alert.dismiss()

    @allure.step('get message from alert')
    def get_message_from_alert(self, message):
        messages = {
            "confirm_btn_msg": self.locator.CONFIRM_BUTTON_MESSAGE,
            "promt_btn_msg": self.locator.PROMT_BUTTON_MESSAGE,
        }
        return self.element_is_visible(messages[message]).text.split(' ')[-1]

    @allure.step('checking prompt alert')
    def checking_prompt_alert(self):
        name = next(generated_data()).first_name
        alert = self.switch_to_alert()
        alert.send_keys(name)
        alert.accept()
        return name


class FramesPage(BasePage):
    locator = FramesLocators()

    @allure.step('jump to frame')
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


class NestedFramesPage(BasePage):
    locator = NestedFramesLocators()

    @allure.step('move to frame')
    def move_to_frame(self, frame):
        frames = {
            "outer_frame": self.locator.OUTER_FRAME,
            "inner_frame": self.locator.INNER_FRAME,
        }
        frame_switch = self.element_is_visible(frames[frame])
        self.switch_to_frame(frame_switch)

    @allure.step('get text frame')
    def get_text_frame(self):
        frame_text = self.element_is_visible(self.locator.FRAME_TEXT).text
        return frame_text


class ModalDialogsPage(BasePage):
    locator = ModalDialogsLocators()

    @allure.step('checking small module')
    def checking_small_module(self):
        self.element_is_visible(self.locator.SMALL_MODAL_BUTTON).click()
        small_modal_title = self.element_is_visible(self.locator.SMALL_MODAL_TITEL).text
        small_modal_text = self.element_is_visible(self.locator.MODAL_TEXT).text
        self.element_is_visible(self.locator.SMALL_MODAL_CLOSE_BUTTON).click()
        return [small_modal_title, len(small_modal_text)]

    @allure.step('checking large module')
    def checking_large_module(self):
        self.element_is_visible(self.locator.LARGE_MODAL_BUTTON).click()
        large_modal_title = self.element_is_visible(self.locator.LARGE_MODAL_TITEL).text
        large_modal_text = self.element_is_visible(self.locator.MODAL_TEXT).text
        self.element_is_visible(self.locator.LARGE_MODAL_CLOSE_BUTTON).click()
        return [large_modal_title, len(large_modal_text)]
