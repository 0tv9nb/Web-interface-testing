import allure

from pages.page_alerts_frame_windows import BrowserWindowsPage, AlertsPage, FramesPage, NestedFramesPage, \
    ModalDialogsPage


@allure.suite("Alerts Frames Windows")
class TestAlertsFramesWindows:
    @allure.feature('Browser Windows')
    class TestBrowserWindows:
        @allure.title('Check browser windows')
        def test_browser_windows(self, driver):
            browser_windows_page = BrowserWindowsPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            browser_windows_page.click_button("new_tab")
            url_tab = browser_windows_page.checking_transition_to_new_window(2)
            assert url_tab, 'new tab not opened'
            browser_windows_page.click_button("new_window")
            url_window = browser_windows_page.checking_transition_to_new_window(3)
            assert url_window, 'new window not opened'
            # browser_windows_page.click_button("new_window_message")
            # url_window_message=browser_windows_page.checking_transition_to_new_window(4)
            # assert url_window_message

    @allure.feature('Alerts')
    class TestAlerts:
        @allure.title('Check alerts')
        def test_alerts(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alerts_page.click_button("alert_button")
            alert_button_text = alerts_page.get_text_alert()
            assert alert_button_text == 'You clicked a button', 'text in alert does not match'
            alerts_page.click_button("timer_alert_button")
            timer_alert_button_text = alerts_page.get_text_alert()
            assert timer_alert_button_text == 'This alert appeared after 5 seconds', 'text in timer_alert does not match'

        @allure.title('Check promt alert')
        def test_promt_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alerts_page.click_button("confirm_button")
            alerts_page.accept_or_close_alert('Ok')
            message_ok = alerts_page.get_message_from_alert('confirm_btn_msg')
            assert message_ok == 'Ok', 'confirmation failed'
            alerts_page.click_button("confirm_button")
            alerts_page.accept_or_close_alert('Cancel')
            message_cancel = alerts_page.get_message_from_alert('confirm_btn_msg')
            assert message_cancel == 'Cancel', "alert didn't close"

        @allure.title('Check confirm alert')
        def test_confirm_alert(self, driver):
            alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alerts_page.open()
            alerts_page.click_button("promt_button")
            name_in = alerts_page.checking_prompt_alert()
            name_out = alerts_page.get_message_from_alert('promt_btn_msg')
            assert name_out == name_in, 'name does not match'

    @allure.feature('Frames')
    class TestFrames:
        @allure.title('Check frame')
        def test_frame(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            big_frame_data = frame_page.jump_to_frame('big_frame')
            assert big_frame_data == ['This is a sample page', '500px', '350px'], 'switch to big frame failed'
            smol_frame_data = frame_page.jump_to_frame('smol_frame')
            assert smol_frame_data == ['This is a sample page', '100px', '100px'], 'switch to smol frame failed'

    @allure.feature('Nested Frames')
    class TestNestedFrames:
        @allure.title('Check nested frames')
        def test_nested_frame(self, driver):
            nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            nested_frame_page.move_to_frame("outer_frame")
            outer_frame_text = nested_frame_page.get_text_frame()
            assert outer_frame_text == 'Parent frame', 'jump to outer frame failed'
            nested_frame_page.move_to_frame("inner_frame")
            inner_frame_text = nested_frame_page.get_text_frame()
            assert inner_frame_text == 'Child Iframe', 'jump to inner frame failed'

    @allure.feature('Modal Dialogs')
    class TestModalDialogs:
        @allure.title('Check modal dialogs')
        def test_modal_dialog(self, driver):
            modal_dialog_page = ModalDialogsPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog_page.open()
            small_data = modal_dialog_page.checking_small_module()
            large_data = modal_dialog_page.checking_large_module()
            assert small_data[0] == 'Small Modal' and small_data[1] > 0, 'small modal it works incorrectly'
            assert large_data[0] == 'Large Modal' and large_data[1] > 0, 'large modal it works incorrectly'
