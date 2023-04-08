from pages.page_alerts_frame_windows import BrowserWindowsPage, AlertsPage


class TestBrowserWindows:
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


class TestAlerts:
    def test_alerts(self, driver):
        alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
        alerts_page.open()
        alerts_page.click_button("alert_button")
        alert_button_text = alerts_page.get_text_alert()
        assert alert_button_text == 'You clicked a button', 'text in alert does not match'
        alerts_page.click_button("timer_alert_button")
        timer_alert_button_text = alerts_page.get_text_alert()
        assert timer_alert_button_text == 'This alert appeared after 5 seconds', 'text in timer_alert does not match'

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

    def test_confirm_alert(self, driver):
        alerts_page = AlertsPage(driver, 'https://demoqa.com/alerts')
        alerts_page.open()
        alerts_page.click_button("promt_button")
        name_in = alerts_page.checking_prompt_alert()
        name_out = alerts_page.get_message_from_alert('promt_btn_msg')
        assert name_out == name_in, 'name does not match'
